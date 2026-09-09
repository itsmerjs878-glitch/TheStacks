/* ============================================================
   The Stacks — sidebar nav renderer + search
   Handles a 3-level tree: course -> Big Idea/Unit -> topic.
   Search matches BOTH the page title and the full page text
   (via window.SEARCH_INDEX, built at site-build time from the
   same content every page is rendered from) — so searching a
   word that only appears in a topic's notes still finds it.
   ============================================================ */

(function () {
  const mount = document.getElementById("sidebar-tree");
  const searchInput = document.getElementById("sidebar-search");
  if (!mount) return;

  const base = document.body.dataset.base || "";
  const currentPage = document.body.dataset.page || "";
  const INDEX = window.SEARCH_INDEX || {};

  function textMatch(item, q) {
    if (!item.url) return false;
    const t = INDEX[item.url];
    return !!t && t.toLowerCase().includes(q);
  }

  function titleMatch(item, q) {
    return item.label.toLowerCase().includes(q);
  }

  function matches(item, q) {
    return titleMatch(item, q) || textMatch(item, q);
  }

  function subtreeMatches(item, q) {
    if (matches(item, q)) return true;
    return (item.children || []).some((c) => subtreeMatches(c, q));
  }

  function containsCurrent(item) {
    if (item.url === currentPage) return true;
    return (item.children || []).some(containsCurrent);
  }

  function snippet(item, q) {
    const t = INDEX[item.url];
    if (!t) return "";
    const lower = t.toLowerCase();
    const i = lower.indexOf(q);
    if (i === -1) return "";
    const start = Math.max(0, i - 40);
    const end = Math.min(t.length, i + q.length + 60);
    let s = t.slice(start, end);
    if (start > 0) s = "\u2026" + s;
    if (end < t.length) s = s + "\u2026";
    return s;
  }

  function highlight(text, q) {
    const span = document.createElement("span");
    const lower = text.toLowerCase();
    let idx = 0, pos;
    while ((pos = lower.indexOf(q, idx)) !== -1) {
      span.appendChild(document.createTextNode(text.slice(idx, pos)));
      const mark = document.createElement("mark");
      mark.textContent = text.slice(pos, pos + q.length);
      span.appendChild(mark);
      idx = pos + q.length;
    }
    span.appendChild(document.createTextNode(text.slice(idx)));
    return span;
  }

  function buildRow(item, depth, opts, query) {
    const row = document.createElement(item.url ? "a" : "div");
    let cls = "nav-row";
    if (depth === 1) cls += " nav-row-child";
    if (depth === 2) cls += " nav-row-grandchild";
    if (item.locked) cls += " nav-row-locked";
    if (item.url && item.url === currentPage) cls += " nav-row-current";
    row.className = cls;
    if (item.url) row.href = base + item.url;

    const wrap = document.createElement("span");
    wrap.className = "nav-row-main";

    const label = document.createElement("span");
    label.className = "nav-row-label";
    label.textContent = item.label;
    wrap.appendChild(label);

    const isContentOnlyMatch = query && !titleMatch(item, query) && textMatch(item, query);
    if (isContentOnlyMatch) {
      const snip = document.createElement("span");
      snip.className = "nav-row-snippet";
      snip.appendChild(highlight(snippet(item, query), query));
      wrap.appendChild(snip);
    }

    row.appendChild(wrap);

    if (item.locked) {
      const tag = document.createElement("span");
      tag.className = "nav-row-tag";
      tag.textContent = "soon";
      row.appendChild(tag);
    }

    if (opts && opts.collapsible) {
      const caret = document.createElement("button");
      caret.className = "nav-caret";
      caret.type = "button";
      caret.setAttribute("aria-label", "Toggle section");
      caret.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        opts.group.classList.toggle("is-collapsed");
      });
      row.appendChild(caret);
    }
    return row;
  }

  function render(filterText) {
    mount.innerHTML = "";
    const q = (filterText || "").trim().toLowerCase();

    NAV_TREE.forEach((top) => {
      if (q && !subtreeMatches(top, q)) return;
      mount.appendChild(buildRow(top, 0, null, q));

      (top.children || []).forEach((bi) => {
        if (q && !subtreeMatches(bi, q)) return;
        const group = document.createElement("div");
        group.className = "nav-group";
        const hasKids = (bi.children || []).length > 0;
        const expanded = q ? true : containsCurrent(bi);
        if (hasKids && !expanded) group.classList.add("is-collapsed");

        group.appendChild(buildRow(bi, 1, hasKids ? { collapsible: true, group } : null, q));

        (bi.children || []).forEach((t) => {
          if (q && !matches(t, q) && !matches(bi, q)) return;
          group.appendChild(buildRow(t, 2, null, q));
        });
        mount.appendChild(group);
      });
    });

    if (q && mount.children.length === 0) {
      const empty = document.createElement("div");
      empty.className = "nav-empty";
      empty.textContent = "No pages match \u201c" + filterText + "\u201d";
      mount.appendChild(empty);
    }
  }

  render("");

  if (searchInput) {
    let t;
    searchInput.addEventListener("input", (e) => {
      clearTimeout(t);
      const val = e.target.value;
      t = setTimeout(() => render(val), 60);
    });
  }

  const toggle = document.getElementById("sidebar-toggle");
  const sidebar = document.getElementById("sidebar");
  if (toggle && sidebar) {
    toggle.addEventListener("click", () => {
      const isOpen = sidebar.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
    mount.addEventListener("click", (e) => {
      if (e.target.closest("a") && !e.target.closest(".nav-caret") && window.innerWidth <= 860) {
        sidebar.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }
})();
