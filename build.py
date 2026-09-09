#!/usr/bin/env python3
"""
The Stacks — page generator.
Run `python3 build.py` from the site root after editing content.py.
Produces:
  ap-csp/index.html          course overview
  ap-csp/big-idea-N.html     Big Idea overview + topic list
  ap-csp/N-M.html            one page per CED topic
  nav-data.js                sidebar tree
"""
import html
import os
import content as csp
import content_csa as csa
from depth import DEPTH_CSP
from depth_csa import DEPTH_CSA
import traces

ROOT = os.path.dirname(os.path.abspath(__file__))

# Each course: (slug, course dict, list of unit dicts, singular unit word)
COURSES = [
    ("ap-csp", csp.COURSE, csp.BIG_IDEAS, "Big Idea", DEPTH_CSP),
    ("ap-csa", csa.COURSE, csa.UNITS, "Unit", DEPTH_CSA),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600'
         '&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')


def shell(title, page, body, base="../", extra_scripts=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — The Stacks</title>
{FONTS}
<link rel="stylesheet" href="{base}styles.css">
<script>
(function(){{try{{var t=localStorage.getItem("stacks-theme");if(t)document.documentElement.setAttribute("data-theme",t);var c=localStorage.getItem("stacks-cb");if(c==="1")document.documentElement.setAttribute("data-cb","1");}}catch(e){{}}}})();
</script>
</head>
<body data-page="{page}" data-base="{base}">

<div class="mobile-topbar">
  <a class="wordmark" href="{base}index.html">The Stacks</a>
  <button id="sidebar-toggle" aria-expanded="false" aria-controls="sidebar">Menu</button>
</div>

<div class="shell">
  <aside id="sidebar">
    <div class="sidebar-inner">
      <div class="site-header">
        <div class="wrap">
          <a class="wordmark" href="{base}index.html">The Stacks<small>free AP Computer Science notes</small></a>
        </div>
      </div>
      <input id="sidebar-search" class="sidebar-search" type="search" placeholder="Search this site" aria-label="Search pages">
      <nav id="sidebar-tree" aria-label="Course navigation"></nav>
      <div class="sidebar-controls">
        <label class="switch-row">
          <span class="switch-label">Dark mode</span>
          <span class="switch"><input type="checkbox" id="theme-toggle" role="switch" aria-label="Toggle dark mode"><span class="switch-track"></span></span>
        </label>
        <label class="switch-row">
          <span class="switch-label">Color-blind friendly</span>
          <span class="switch"><input type="checkbox" id="cb-toggle" role="switch" aria-label="Toggle color-blind friendly palette"><span class="switch-track"></span></span>
        </label>
      </div>
      <div class="sidebar-foot">Built by a high school student, one unit at a time.</div>
    </div>
  </aside>

  <div class="content-col">
    <main>
{body}
    </main>
    <footer class="site-footer">
      <div class="wrap">Notes track the College Board Course and Exam Description. AP&reg; is a trademark of the College Board, which was not involved in producing and does not endorse this site.</div>
    </footer>
  </div>
</div>

<script src="{base}nav-data.js"></script>
<script src="{base}search-index.js"></script>
<script src="{base}nav.js"></script>
<script src="{base}theme.js"></script>
{extra_scripts}
</body>
</html>
"""


def topic_slug(bi_num, t_num):
    return f"{bi_num}-{t_num}.html"


def render_question(q, idx):
    opts = "".join(
        f'<li><span class="opt-letter">{letter}</span> {o}</li>'
        for letter, o in zip("ABCD", q["options"])
    )
    return f"""
<div class="question">
  <div class="q-stem"><span class="q-num">Q{idx}</span> {q["stem"]}</div>
  <ol class="q-options">{opts}</ol>
  <details class="q-answer">
    <summary>Show answer</summary>
    <p><strong>Answer: {q["answer"]}.</strong> {q["explanation"]}</p>
  </details>
</div>"""


import re as _re


def _plain(html_text):
    """Strip tags/entities down to plain, whitespace-collapsed text."""
    t = _re.sub(r"<[^>]+>", " ", html_text or "")
    t = (t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
           .replace("&rsquo;", "'").replace("&ndash;", "-").replace("&mdash;", "-")
           .replace("&middot;", "-").replace("&hellip;", "...").replace("&reg;", "")
           .replace("&larr;", "<-").replace("&rarr;", "->").replace("&ge;", ">=")
           .replace("&le;", "<=").replace("&ne;", "!=").replace("&times;", "x")
           .replace("&quot;", '"').replace("&#39;", "'"))
    t = _re.sub(r"\s+", " ", t).strip()
    return t


def topic_search_text(bi, t, d):
    parts = [t.get("lede", "")]
    parts += t.get("points", [])
    if t.get("example"):
        parts.append(t["example"])
    if t.get("tip"):
        parts.append(t["tip"])
    parts += d.get("deeper", [])
    parts += d.get("mistakes", [])
    for q in t.get("questions", []):
        parts.append(q.get("stem", ""))
        parts += q.get("options", [])
        parts.append(q.get("explanation", ""))
    for k, v in t.get("vocab", []):
        parts.append(f"{k}: {v}")
    return _plain(" ".join(parts))


def render_search_index():
    entries = {}
    for slug, course, units, unit_word, depth in COURSES:
        for bi in units:
            n = bi["num"]
            unit_url = f"{slug}/unit-{n}.html"
            entries[unit_url] = _plain(bi.get("lede", "") + " " + " ".join(bi.get("understandings", [])))
            for t in bi["topics"]:
                key = f"{n}.{t['num']}"
                d = depth.get(key, {})
                url = f"{slug}/{topic_slug(n, t['num'])}"
                entries[url] = topic_search_text(bi, t, d)
    lines = ["/* Generated by build.py — a plain-text search index built from",
             "   the same content/depth data every page is rendered from. */", "",
             "const SEARCH_INDEX = {"]
    for url, text in entries.items():
        safe = text.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'  "{url}": "{safe}",')
    lines += ["};", ""]
    return "\n".join(lines)


def render_tracer(tid):
    return (f'<div class="tracer" data-trace-id="{tid}"></div>'
            f'<p class="tracer-hint">Step through with the buttons, or use the &larr; &rarr; keys. Changed variables are highlighted.</p>')


def trace_scripts(tids):
    if not tids:
        return ""
    data = "{" + ",".join(f'"{tid}": {traces.trace_json(tid)}' for tid in tids) + "}"
    return f'<script>window.TRACES = {data};</script>\n<script src="{{base}}tracer.js"></script>'


def render_topic(slug, unit_word, depth, bi, t, prev_t, next_t):
    bi_num = bi["num"]
    num = f"{bi_num}.{t['num']}"
    d = depth.get(num, {})
    points = "".join(f"<li>{p}</li>" for p in t["points"])
    example = f"""
<section class="block">
  <h2>Worked example</h2>
  {t["example"]}
</section>""" if t.get("example") else ""
    tip = f'<div class="callout"><strong>Exam tip:</strong> {t["tip"]}</div>' if t.get("tip") else ""
    deeper = "".join(f"<li>{p}</li>" for p in d.get("deeper", []))
    dsec = f"""
<section class="block">
  <h2>Going deeper</h2>
  <p class="block-note">The nuance, edge cases, and connections that turn a 3 into a 5.</p>
  <ul class="points">{deeper}</ul>
</section>""" if deeper else ""
    mistakes = "".join(f"<li>{m}</li>" for m in d.get("mistakes", []))
    msec = f"""
<section class="block">
  <h2>Mistakes that cost points</h2>
  <ul class="mistakes">{mistakes}</ul>
</section>""" if mistakes else ""
    tid = d.get("trace")
    tsec = f"""
<section class="block">
  <h2>Trace it yourself</h2>
  {render_tracer(tid)}
</section>""" if tid else ""
    questions = "".join(render_question(q, i + 1) for i, q in enumerate(t.get("questions", [])))
    qsec = f"""
<section class="block">
  <h2>Practice questions</h2>
  <p class="block-note">Written in the style of the real exam. Try each one before revealing the answer.</p>
  {questions}
</section>""" if questions else ""
    vocab = "".join(
        f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in t.get("vocab", [])
    )
    vsec = f"""
<section class="vocab">
  <h2>Key vocabulary</h2>
  <dl>{vocab}</dl>
</section>""" if vocab else ""

    prev_link = (f'<a href="{topic_slug(bi_num, prev_t["num"])}"><span class="dir">Previous</span>{bi_num}.{prev_t["num"]} {prev_t["title"]}</a>'
                 if prev_t else f'<a href="unit-{bi_num}.html"><span class="dir">Up</span>{unit_word} {bi_num} overview</a>')
    next_link = (f'<a class="to-right" href="{topic_slug(bi_num, next_t["num"])}"><span class="dir">Next</span>{bi_num}.{next_t["num"]} {next_t["title"]}</a>'
                 if next_t else f'<a class="to-right" href="unit-{bi_num}.html"><span class="dir">Back to</span>{unit_word} {bi_num} overview</a>')

    body = f"""
<div class="article-eyebrow"><a href="unit-{bi_num}.html">{unit_word.upper()} {bi_num}: {bi["title"].upper()}</a> &middot; TOPIC {num}</div>
<h1 class="article-title"><span class="title-num">{num}</span> {t["title"]}</h1>
<p class="article-lede">{t["lede"]}</p>

<section class="block">
  <h2>What you need to know</h2>
  <ul class="points">{points}</ul>
</section>
{example}
{tsec}
{tip}
{dsec}
{msec}
{qsec}
{vsec}

<div class="pager">
  {prev_link}
  {next_link}
</div>"""
    extra = trace_scripts([tid]).replace("{base}", "../") if tid else ""
    return shell(f"{num} {t['title']}", f"{slug}/{topic_slug(bi_num, t['num'])}", body, extra_scripts=extra)


def render_big_idea(slug, unit_word, bi, prev_bi, next_bi):
    n = bi["num"]
    rows = "".join(
        f"""<a class="toc-entry" href="{topic_slug(n, t['num'])}">
  <span class="toc-num">{n}.{t['num']}</span>
  <span class="toc-label">{t['title']}</span>
  <span class="toc-leader"></span>
  <span class="toc-page">{t.get('blurb', '')}</span>
</a>""" for t in bi["topics"]
    )
    eus = "".join(f"<li>{e}</li>" for e in bi.get("understandings", []))
    prev_link = f'<a href="unit-{prev_bi["num"]}.html"><span class="dir">Previous</span>{unit_word} {prev_bi["num"]}: {prev_bi["title"]}</a>' if prev_bi else '<a href="index.html"><span class="dir">Up</span>Course overview</a>'
    next_link = f'<a class="to-right" href="unit-{next_bi["num"]}.html"><span class="dir">Next</span>{unit_word} {next_bi["num"]}: {next_bi["title"]}</a>' if next_bi else '<a class="to-right" href="index.html"><span class="dir">Back to</span>Course overview</a>'

    body = f"""
<div class="article-eyebrow">{unit_word.upper()} {n} &middot; {bi["weight"]} OF THE EXAM &middot; {len(bi["topics"])} TOPICS</div>
<h1 class="article-title">{bi["title"]}</h1>
<p class="article-lede">{bi["lede"]}</p>

<section class="block">
  <h2>What the College Board expects you to walk away understanding</h2>
  <ul class="points">{eus}</ul>
</section>

<section class="block">
  <h2>Topics in this {unit_word}</h2>
  <nav aria-label="Topics">{rows}</nav>
</section>

<section class="block">
  <h2>Night-before review</h2>
  <p class="block-note">Every key term and exam tip from this {unit_word.lower()} on one printable page.</p>
  <a class="toc-entry" href="cheat-{n}.html"><span class="toc-num">&#9633;</span><span class="toc-label">{unit_word} {n} cheat sheet</span><span class="toc-leader"></span><span class="toc-page">print</span></a>
</section>

<div class="pager">
  {prev_link}
  {next_link}
</div>"""
    return shell(f"{unit_word} {n}: {bi['title']}", f"{slug}/unit-{n}.html", body)


def render_cheat(slug, unit_word, bi):
    n = bi["num"]
    cards = ""
    for t in bi["topics"]:
        vocab = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in t.get("vocab", []))
        tip = f'<div class="cheat-tip"><strong>Tip:</strong> {t["tip"]}</div>' if t.get("tip") else ""
        cards += f"""<div class="cheat-topic">
  <h3><span class="tnum">{n}.{t['num']}</span>{t['title']}</h3>
  <dl>{vocab}</dl>
  {tip}
</div>"""
    body = f"""
<div class="article-eyebrow"><a href="unit-{n}.html">{unit_word.upper()} {n}: {bi["title"].upper()}</a> &middot; CHEAT SHEET</div>
<h1 class="article-title">{bi["title"]} — the one-page version</h1>
<p class="article-lede">Every key term and every exam tip from the {len(bi["topics"])} topics in this {unit_word.lower()}. Print it, fold it, read it on the bus.</p>
<button type="button" class="print-btn" onclick="window.print()">Print this page</button>

<section class="block">
  <div class="cheat-grid">{cards}</div>
</section>

<div class="pager">
  <a href="unit-{n}.html"><span class="dir">Back to</span>{unit_word} {n} overview</a>
  <span></span>
</div>"""
    return shell(f"{unit_word} {n} cheat sheet", f"{slug}/cheat-{n}.html", body)


def render_tracer_index(slug, course):
    tids = [tid for tid, tr in traces.TRACES.items() if tr["course"] == slug]
    widgets = "".join(f"""
<section class="block">
  <h2>{traces.TRACES[tid]["title"]}</h2>
  {render_tracer(tid)}
</section>""" for tid in tids)
    body = f"""
<div class="course-eyebrow">{course["title"].upper()}</div>
<h1 class="course-title">Code tracer</h1>
<div class="course-intro"><p>Step through real exam-style code one line at a time and watch every variable change. This is the skill behind most of the multiple-choice section — every trace below was recorded by actually running the program, so what you see is exactly what happens.</p></div>
{widgets}
<div class="pager">
  <a href="index.html"><span class="dir">Back to</span>{course["title"]}</a>
  <span></span>
</div>"""
    extra = trace_scripts(tids).replace("{base}", "../")
    return shell(f"Code tracer — {course['title']}", f"{slug}/tracer.html", body, extra_scripts=extra)


def render_course(slug, course, units, unit_word):
    rows = "".join(
        f"""<a class="toc-entry" href="unit-{bi['num']}.html">
  <span class="toc-num">{bi['num']}</span>
  <span class="toc-label">{bi['title']}</span>
  <span class="toc-leader"></span>
  <span class="toc-page">{bi['weight']}</span>
</a>""" for bi in units
    )
    plural = "Big Ideas" if unit_word == "Big Idea" else "units"
    body = f"""
<div class="course-eyebrow">AP COMPUTER SCIENCE</div>
<h1 class="course-title">{course["title"]}</h1>
<div class="course-intro">{course["intro"]}</div>

<section class="block">
  <h2>The {len(units)} {plural}</h2>
  <p class="block-note">Weight shown is that {unit_word.lower()}'s share of the multiple-choice exam.</p>
  <nav aria-label="{plural}">{rows}</nav>
</section>

{course["exam_format"]}
{course["five_tips"]}

<section class="block">
  <h2>Practice tracing</h2>
  <p class="block-note">Interactive, step-by-step walkthroughs of the loops, lists, and recursion the exam asks you to trace by hand.</p>
  <a class="toc-entry" href="tracer.html"><span class="toc-num">&#9654;</span><span class="toc-label">Code tracer</span><span class="toc-leader"></span><span class="toc-page">interactive</span></a>
</section>
"""
    return shell(course["title"], f"{slug}/index.html", body)


def render_nav_data():
    lines = ['/* Generated by build.py — edit content.py / content_csa.py, not this file. */', '', 'const NAV_TREE = [',
             '  { label: "Home", url: "index.html" },']
    for slug, course, units, unit_word, _depth in COURSES:
        lines += ['  {', f'    label: "{course["title"]}",', f'    url: "{slug}/index.html",', '    children: [']
        lines += ['      {', '        label: "Code tracer",', f'        url: "{slug}/tracer.html",', '      },']
        for bi in units:
            n = bi["num"]
            lines.append('      {')
            lines.append(f'        label: "{n}. {bi["title"]}",')
            lines.append(f'        url: "{slug}/unit-{n}.html",')
            lines.append('        children: [')
            for t in bi["topics"]:
                safe = t["title"].replace('"', '\\"')
                lines.append(f'          {{ label: "{n}.{t["num"]} {safe}", url: "{slug}/{topic_slug(n, t["num"])}" }},')
            lines.append(f'          {{ label: "Cheat sheet", url: "{slug}/cheat-{n}.html" }},')
            lines.append('        ],')
            lines.append('      },')
        lines += ['    ],', '  },']
    lines += ['];', '']
    return "\n".join(lines)


def main():
    for slug, course, units, unit_word, depth in COURSES:
        out = os.path.join(ROOT, slug)
        os.makedirs(out, exist_ok=True)
        for old in os.listdir(out):
            if old.endswith(".html"):
                os.remove(os.path.join(out, old))
        with open(os.path.join(out, "index.html"), "w") as f:
            f.write(render_course(slug, course, units, unit_word))
        for i, bi in enumerate(units):
            prev_bi = units[i - 1] if i > 0 else None
            next_bi = units[i + 1] if i + 1 < len(units) else None
            with open(os.path.join(out, f"unit-{bi['num']}.html"), "w") as f:
                f.write(render_big_idea(slug, unit_word, bi, prev_bi, next_bi))
            with open(os.path.join(out, f"cheat-{bi['num']}.html"), "w") as f:
                f.write(render_cheat(slug, unit_word, bi))
            topics = bi["topics"]
            for j, t in enumerate(topics):
                prev_t = topics[j - 1] if j > 0 else None
                next_t = topics[j + 1] if j + 1 < len(topics) else None
                with open(os.path.join(out, topic_slug(bi["num"], t["num"])), "w") as f:
                    f.write(render_topic(slug, unit_word, depth, bi, t, prev_t, next_t))
        with open(os.path.join(out, "tracer.html"), "w") as f:
            f.write(render_tracer_index(slug, course))
        total = sum(len(bi["topics"]) for bi in units)
        print(f"{slug}: course page, {len(units)} {unit_word.lower()} pages, {len(units)} cheat sheets, {total} topic pages, tracer")
    with open(os.path.join(ROOT, "nav-data.js"), "w") as f:
        f.write(render_nav_data())
    with open(os.path.join(ROOT, "search-index.js"), "w") as f:
        f.write(render_search_index())
    print("nav-data.js and search-index.js written")


if __name__ == "__main__":
    main()
