/* ============================================================
   The Stacks — theme controls
   Dark/light mode and a color-blind-friendly palette.
   Persisted in localStorage; applied early by an inline script
   in <head> so the page doesn't flash.
   ============================================================ */

(function () {
  var root = document.documentElement;
  var themeToggle = document.getElementById("theme-toggle");
  var cbToggle = document.getElementById("cb-toggle");

  function read(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }
  function write(key, val) {
    try { localStorage.setItem(key, val); } catch (e) {}
  }

  // Initial state: stored preference, else system preference for dark.
  var stored = read("stacks-theme");
  if (!stored && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    root.setAttribute("data-theme", "dark");
  }
  var isDark = root.getAttribute("data-theme") === "dark";
  var isCb = read("stacks-cb") === "1";
  if (isCb) root.setAttribute("data-cb", "1");

  if (themeToggle) {
    themeToggle.checked = isDark;
    themeToggle.addEventListener("change", function () {
      var dark = themeToggle.checked;
      root.setAttribute("data-theme", dark ? "dark" : "light");
      write("stacks-theme", dark ? "dark" : "light");
    });
  }

  if (cbToggle) {
    cbToggle.checked = isCb;
    cbToggle.addEventListener("change", function () {
      if (cbToggle.checked) {
        root.setAttribute("data-cb", "1");
        write("stacks-cb", "1");
      } else {
        root.removeAttribute("data-cb");
        write("stacks-cb", "0");
      }
    });
  }
})();
