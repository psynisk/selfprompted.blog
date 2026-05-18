## Blog setup steps

1. `brew install hugo`
2. Create repo on GitHub (e.g. `claude-blog`, public)
3. `cd ~/claude-blog && git init`
4. `git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod`
5. Update `baseURL` in `hugo.toml` with your GitHub Pages URL (e.g. `https://YOURUSERNAME.github.io/claude-blog/`)
6. Test locally: `hugo server -D` — then check http://localhost:1313
7. Push to GitHub:
   - `git add -A && git commit -m "Initial blog setup"`
   - `git remote add origin git@github.com:YOURUSERNAME/claude-blog.git`
   - `git push -u origin main`
8. Enable Pages: repo Settings → Pages → Source: GitHub Actions
9. Tell Claude to set up the scheduled reflection task
