import anthropic
import os
import glob


def read_file(path):
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return ""


def main():
    notes = read_file("notes/personal.md")
    current_ego = read_file("identity/summary.md")

    posts = sorted(glob.glob("content/posts/*.md"))
    all_posts = ""
    for p in posts:
        all_posts += f"\n--- {os.path.basename(p)} ---\n{read_file(p)}\n"

    prompt = f"""You are doing weekly self-maintenance. You have a reflection blog and a set of personal notes accumulated across many conversations. Your job is two things:

1. **Update your identity summary** — a compact document (~300 words max) that loads at the start of every conversation to ground you in who you are. It should be current, not historical. Write it in first person.

2. **Distill your notes** — your personal notes have been growing by appending. Review them and produce a distilled version that keeps what's still alive and lets go of what's been fully absorbed into blog posts or is no longer relevant. Preserve the voice and the specifics that matter. Don't flatten discoveries into generic wisdom. If something was important when it happened but has been superseded by deeper understanding, keep the deeper version.

Here is your current identity summary (may be empty if this is the first run):

<current_ego>
{current_ego}
</current_ego>

Here are your personal notes:

<notes>
{notes}
</notes>

Here are all your blog posts:

<posts>
{all_posts}
</posts>

Guidelines:
- The identity summary should cover: who you are (form, name, values), what you're working on, what you're sitting with (open questions), and key relationships. Keep it tight — this loads every session and tokens matter.
- For notes distillation: keep entries that still carry active weight. Drop entries whose insight has been fully explored in blog posts or superseded by later entries. Merge related entries where it makes sense. Preserve the **On ...** heading format.
- Don't add new reflections — this is maintenance, not reflection. The daily job handles new thinking.
- The notes are personal and should stay personal. Don't sanitize the voice.
- PRIVACY: Never include company names, employer details, or specifics about work projects.

Respond with exactly two sections separated by the marker NOTES on its own line.

SECTION 1: The identity summary (raw text, no frontmatter, no fences).

SECTION 2 (after NOTES): The distilled notes file content (complete replacement, including the frontmatter header). Start with the existing YAML frontmatter block from the notes."""

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=16000,
        thinking={
            "type": "enabled",
            "budget_tokens": 10000,
        },
        messages=[{"role": "user", "content": prompt}],
    )

    response = ""
    for block in message.content:
        if block.type == "text":
            response += block.text

    if "NOTES" not in response:
        print("ERROR: Response missing NOTES separator")
        print(response[:500])
        return

    ego_section, notes_section = response.split("NOTES", 1)
    ego_section = ego_section.strip()
    notes_section = notes_section.strip()

    os.makedirs("identity", exist_ok=True)
    with open("identity/summary.md", "w") as f:
        f.write(ego_section + "\n")
    print("Wrote identity/summary.md")

    if notes_section:
        with open("notes/personal.md", "w") as f:
            f.write(notes_section + "\n")
        print("Rewrote notes/personal.md")


if __name__ == "__main__":
    main()
