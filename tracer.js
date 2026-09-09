/* ============================================================
   The Stacks — code tracer widget
   Plays back pre-recorded traces (see traces.py). Each
   <div class="tracer" data-trace-id="..."> is populated from
   window.TRACES[id]. Keyboard: ← → to step, Home/End to jump.
   ============================================================ */

(function () {
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function build(el, trace) {
    var idx = 0;
    var steps = trace.steps;

    el.innerHTML =
      '<div class="tracer-head">' +
        '<div class="tracer-title">' + esc(trace.title) + '</div>' +
        (trace.intro ? '<div class="tracer-intro">' + esc(trace.intro) + '</div>' : '') +
      '</div>' +
      '<div class="tracer-body">' +
        '<pre class="tracer-code"></pre>' +
        '<div class="tracer-side">' +
          '<div class="tracer-label">Variables</div>' +
          '<table class="tracer-vars"><tbody></tbody></table>' +
          '<div class="tracer-label">Output</div>' +
          '<pre class="tracer-out"></pre>' +
        '</div>' +
      '</div>' +
      '<div class="tracer-note"></div>' +
      '<div class="tracer-controls">' +
        '<button type="button" class="tracer-btn" data-act="first" aria-label="First step">&#8676;</button>' +
        '<button type="button" class="tracer-btn" data-act="prev" aria-label="Previous step">&#8592; Back</button>' +
        '<span class="tracer-count"></span>' +
        '<button type="button" class="tracer-btn tracer-btn-primary" data-act="next" aria-label="Next step">Step &#8594;</button>' +
        '<button type="button" class="tracer-btn" data-act="last" aria-label="Last step">&#8677;</button>' +
      '</div>';

    var codeEl = el.querySelector(".tracer-code");
    var varsEl = el.querySelector(".tracer-vars tbody");
    var outEl = el.querySelector(".tracer-out");
    var noteEl = el.querySelector(".tracer-note");
    var countEl = el.querySelector(".tracer-count");

    // Code lines rendered once; highlight toggled per step.
    codeEl.innerHTML = trace.code.map(function (line, i) {
      return '<span class="tracer-line" data-line="' + i + '"><span class="tracer-ln">' + (i + 1) + '</span>' + esc(line || " ") + '</span>';
    }).join("\n");
    var lineEls = codeEl.querySelectorAll(".tracer-line");

    function render() {
      var s = steps[idx];
      for (var i = 0; i < lineEls.length; i++) {
        lineEls[i].classList.toggle("is-active", i === s.line);
      }
      var prevVars = idx > 0 ? steps[idx - 1].vars : [];
      var prevMap = {};
      prevVars.forEach(function (p) { prevMap[p[0]] = p[1]; });
      varsEl.innerHTML = s.vars.length
        ? s.vars.map(function (v) {
            var changed = prevMap[v[0]] !== v[1];
            return '<tr' + (changed ? ' class="is-changed"' : '') + '><td class="tracer-vname">' + esc(v[0]) + '</td><td class="tracer-vval">' + esc(v[1]) + '</td></tr>';
          }).join("")
        : '<tr><td class="tracer-empty" colspan="2">nothing yet</td></tr>';
      outEl.textContent = s.out || "";
      noteEl.textContent = s.note || "";
      countEl.textContent = (idx + 1) + " / " + steps.length;
      el.querySelector('[data-act="prev"]').disabled = idx === 0;
      el.querySelector('[data-act="first"]').disabled = idx === 0;
      el.querySelector('[data-act="next"]').disabled = idx === steps.length - 1;
      el.querySelector('[data-act="last"]').disabled = idx === steps.length - 1;
    }

    function go(n) {
      idx = Math.max(0, Math.min(steps.length - 1, n));
      render();
    }

    el.addEventListener("click", function (e) {
      var b = e.target.closest("[data-act]");
      if (!b) return;
      var a = b.getAttribute("data-act");
      if (a === "next") go(idx + 1);
      else if (a === "prev") go(idx - 1);
      else if (a === "first") go(0);
      else if (a === "last") go(steps.length - 1);
    });

    el.setAttribute("tabindex", "0");
    el.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { go(idx + 1); e.preventDefault(); }
      else if (e.key === "ArrowLeft") { go(idx - 1); e.preventDefault(); }
      else if (e.key === "Home") { go(0); e.preventDefault(); }
      else if (e.key === "End") { go(steps.length - 1); e.preventDefault(); }
    });

    render();
  }

  var nodes = document.querySelectorAll(".tracer[data-trace-id]");
  for (var i = 0; i < nodes.length; i++) {
    var id = nodes[i].getAttribute("data-trace-id");
    if (window.TRACES && window.TRACES[id]) build(nodes[i], window.TRACES[id]);
  }
})();
