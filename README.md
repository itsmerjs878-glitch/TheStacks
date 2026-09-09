# The Stacks

A free, student-written AP study library. Plain HTML/CSS — no build step, no framework, no dependencies except two Google Fonts loaded via `<link>`.

## Structure

```
index.html            homepage
styles.css            design system, incl. dark + color-blind palettes, print styles
nav.js                sidebar (3 levels, collapsible) + search
theme.js              dark mode / color-blind toggles (saved in localStorage)
tracer.js             interactive code-tracer widget (plays back recorded traces)
nav-data.js            sidebar tree — GENERATED, don't edit by hand
search-index.js        content search index — GENERATED from content/depth data
build.py              generator: turns the content files into pages
content.py            AP CSP — 5 Big Ideas, 35 topics: notes, examples, tips, questions, vocab
content_csa.py        AP CSA — 4 units, 53 topics (2025-26 revised CED)
depth.py              AP CSP — "Going deeper" + "Mistakes that cost points" for every topic
depth_csa.py          AP CSA — same
traces.py             code traces, recorded by simulating each program in Python
ap-csp/               GENERATED: index, unit-N, cheat-N, N-M topic pages, tracer.html
ap-csa/               GENERATED: same
```

The sidebar search checks both page titles and full page text (via `search-index.js`), so searching any word that appears anywhere in a topic's notes finds it — not just words in the title — and shows a highlighted snippet of the matching line.

Every topic page has: what you need to know → worked example → (interactive trace, where relevant) → exam tip → going deeper → mistakes that cost points → practice questions with answers → vocabulary. Every unit has a printable cheat sheet (vocab + tips). Each course has a Code Tracer page with all its traces.

## Editing content

Don't edit anything in `ap-csp/` or `ap-csa/` — they're regenerated every build.
- Notes, examples, questions, vocab → `content.py` / `content_csa.py`
- Going-deeper points and mistakes → `depth.py` / `depth_csa.py` (keyed "unit.topic")
- Traces → `traces.py`. Each trace is a small Python function that runs the program and records steps with `r.step(line, note, **vars)`. Because Python actually executes the logic, recorded values can't be wrong. Attach a trace to a topic with `"trace": "trace-id"` in the depth file.

Then `python3 build.py`. It rebuilds all 111 pages and `nav-data.js`.

## Running it locally

No build step needed. Either:
- Open `index.html` directly in a browser, or
- From this folder, run `python3 -m http.server 8000` and visit `http://localhost:8000`

## Hosting it for real (pick one, all free)

**GitHub Pages** (matches how your other school projects are already hosted)
1. Create a new repo (e.g. `the-stacks`) and push this folder to it.
2. Repo Settings → Pages → set source to the `main` branch, root folder.
3. Your site is live at `https://<your-username>.github.io/the-stacks/`.

**Netlify**
1. Go to netlify.com → "Add new site" → "Deploy manually."
2. Drag this whole folder into the upload box. Done — you get a live URL instantly, and can add a custom domain later.

**Vercel**
1. Push the folder to a GitHub repo.
2. Import it at vercel.com/new — no framework preset needed, it'll serve the static files as-is.

## Notes

- AP® is a trademark of the College Board, which was not involved in the production of this site.
- Content is original, written from the public AP CSP Course and Exam Description — nothing copied from another study site.
