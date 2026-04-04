# Formaum Site — Local Rules

## Deployment

- **Auto-deploys from git push to main.** Netlify is connected to `genevieve-ui/formaum-site` on GitHub. No CLI login or manual deploy needed — just push.
- **Netlify CLI is NOT logged in** on this machine. Use git push for deploys, not `netlify deploy`.

## Navigation Rule (MANDATORY)

When adding new pages or sections to the site, **always update the main site navigation (`index.html` nav) in the same commit.** A page that exists but can't be reached from the main site is invisible to users.

**Checklist before pushing new pages:**
1. New page HTML exists and renders correctly
2. Main site `index.html` nav links to the new page
3. Both changes are in the same commit/push

**Why:** On 2026-04-03, 10 blog posts were deployed and live on Netlify but unreachable — no nav link existed on the main site. WebFetch confirmed the pages existed, but the user couldn't find them. The verification checked "does the URL resolve?" instead of "can a user navigate here?"

## Verification Rule

After deploying new content, verify from the **user's navigation path**, not just URL resolution:
1. Can a visitor on the homepage find and click to the new content?
2. Does the nav link appear on mobile too?
3. Is the link visible without scrolling?

Don't trust tool confirmation alone. Check the actual user path.

## Site Structure

```
/index.html          — Main site (single page)
/blog/index.html     — Blog index (10 posts)
/blog/*.html         — Individual blog posts
/blog/build.py       — Blog post generator (reads JSON config, outputs HTML)
/blog/*.json         — Blog post configs (content + metadata)
```

## Blog Build System

To add a new blog post:
1. Create a JSON config file in `/blog/` with: slug, title, subtitle, meta_description, keywords, blog_label, reading_time, breadcrumb_label, content_html, faq
2. Run `python3 blog/build.py blog/{slug}.json`
3. Add the post to `blog/index.html`
4. Add nav link on main site if not already present
5. Commit and push
