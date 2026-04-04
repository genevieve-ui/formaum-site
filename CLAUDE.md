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

## LinkedIn Post Voice (Proven Format)

Based on Genevieve's highest-performing post (VFX throwback, went viral on LinkedIn + Instagram). Study this structure before writing any LinkedIn content.

### The Post That Worked

```
(2017 Throwback)... Every VFX studio I've talked to runs on some version of this stack:
ShotGrid for shot tracking, a spreadsheet for bids, email for client comms, Slack for
internal, and one rogue whiteboard with outdated thumbnail printouts.

My issue has always been that none of them talk to each other. So people becomes the glue.
They pull stale data from ShotGrid, update the spreadsheets, DM artists endlessly, all
while running on minimal sleep. Then a surprise trailer drops and the hero shot has never
been touched.

That glue was me. I wasn't doing creative work. I was the manual integration layer between
five platforms. I used live that life, a lot of people still do and now I build the AI
layer that runs 24/7 so nobody has to.
```

### Why It Worked — Structural Analysis

1. **Personal anchor first.** Opens with a time reference that grounds it in lived experience, not theory. "(2017 Throwback)" — not "5 tips for..." or "Did you know..."
2. **Industry-specific stack list.** Names the actual tools. ShotGrid, spreadsheets, email, Slack, whiteboard. People see their own desk. The specificity creates recognition.
3. **3 short paragraphs.** Not 10. Not a thread. Three. Each one has a single emotional beat:
   - Para 1: "Here's what everyone's running on" (recognition)
   - Para 2: "Here's why it's broken" (pain)
   - Para 3: "That was me. Now I fix it." (transformation)
4. **"That glue was me."** The pivot sentence. Shifts from observer to participant. This is where the reader goes from "she gets it" to "she lived it."
5. **No CTA.** No "book a call." No "DM me." The authority IS the CTA. People reach out because of the post, not because they were asked to.
6. **Casual grammar.** "I used live that life" (typo left in), "a lot of people still do" — not polished. Real.
7. **Had a photo.** A picture of Genevieve on a chair, funny pose. Every post without a photo underperforms.

### LinkedIn Post Rules (Derived)

- **Always include a photo.** Posts without photos underperform significantly. Photo of Genevieve preferred. Candid/personality > corporate headshot.
- **3 paragraphs max for the main body.** Each paragraph is one beat: recognition → pain → transformation.
- **Open with a personal anchor.** A year, a throwback, a moment. "Last week I...", "(2019)...", "Three months into this build..."
- **Name the actual tools/platforms.** Specificity creates recognition. "Monday.com, Make.com, Twilio" not "various tools."
- **One pivot sentence.** The moment that shifts from "this is the industry" to "this was me." Keep it short. Under 10 words.
- **No explicit CTA.** The post IS the CTA. If someone wants to hire you, they'll click your profile. Don't cheapen it with "DM me."
- **Link to blog post as a comment or final line** — not mid-post. And only sometimes. The post should stand alone.
- **Character count target:** 600-900 characters. Not a thread. Not a novel. A moment.
- **Tone:** First-person, past tense for the story, present tense for the lesson. Warm but direct. Zero marketing language.

### What NOT to Do on LinkedIn

- No "I'm thrilled to announce..."
- No bullet-heavy listicles
- No hashtag walls (3-5 max, at the end)
- No generic advice posts ("5 ways to improve your CRM")
- No posts without a photo
- No posts that read like they were written by AI
- No "engagement bait" questions ("Who else deals with this? 🙋")

### Approved LinkedIn Post Templates (Locked April 2026)

These 3 posts were approved after multiple rounds of iteration. Use them as the reference for all future LinkedIn content. Match the structure, length, and tone exactly.

**Template 1: The Frustration Arc (personal history → client work now)**
```
Every production I worked on, I had the same thought. "It doesn't need to be like this."

Five platforms. None of them talking. People manually copying data between tools because
nobody built the bridge. I'd sit in dailies knowing the whole system was held together by
someone's memory and a spreadsheet that hadn't been updated since Tuesday.

Nothing changed. Because the people who felt the pain weren't the people who could fix
the infrastructure. They were too busy being the infrastructure.

Now I get to be the person who fixes it. Currently migrating a client off Monday.com,
Typeform, AWS, Make.com, and Twilio into one GHL system. Twilio stays — but it runs
inside GHL now. Native tools wherever possible. One login. One source of truth. The kind
of setup I spent years wishing someone would build for me.
```

**Template 2: The Lifestyle Proof (automation → freedom)**
```
I've automated 85% of my business. And climbing.

Two years ago I was the manual integration layer between five platforms at a VFX studio.
Now I build the AI layer that replaces that job — for other people's businesses.

The irony is I had to do it for myself first. Every client intake, every follow-up
sequence, every invoice, every onboarding step — automated. Not because I'm lazy. Because
I spent a decade watching smart people burn out doing work a system should handle.

I spend more time in the garden now. That's the metric nobody puts on a dashboard but
it's the one that matters.
```

**Template 3: The Business Move (buying back time)**
```
Hired a personal assistant this month.

Not because the business is too big. Because my time is too expensive to spend on the
wrong things. Every hour I spend on admin is an hour I'm not building systems for clients
or closing the next deal.

Same logic I give every client: if a human is doing a job a system could handle, you're
paying a person rate for a machine task. I automated 85% of my own business first. The PA
handles the 15% that actually needs a person — scheduling, coordination, the stuff that
requires judgment, not just execution.

Buy your time back. Then buy your freedom. That's the order.
```

### How to Generate New Posts From These Templates

1. Pick a template (Frustration Arc, Lifestyle Proof, or Business Move)
2. Swap in the new topic/data but keep the same emotional beats
3. 3 paragraphs. Personal anchor → pain/recognition → pivot/transformation
4. 600-900 characters
5. Always include a photo note (remind Genevieve to attach a photo)
6. 3-5 hashtags at the end, no hashtag walls
7. Blog link as final line only if relevant — post should stand alone without it

## Blog Build System

To add a new blog post:
1. Create a JSON config file in `/blog/` with: slug, title, subtitle, meta_description, keywords, blog_label, reading_time, breadcrumb_label, content_html, faq
2. Run `python3 blog/build.py blog/{slug}.json`
3. Add the post to `blog/index.html`
4. Add nav link on main site if not already present
5. Commit and push
