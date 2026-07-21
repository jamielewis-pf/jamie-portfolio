/* Jamie Lewis — portfolio interactions
   Copy-email, scroll reveal, nav state. Vanilla, no deps. */
(function () {
  "use strict";

  /* ---- Nav: background on scroll ---- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 24); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- Copy email (not mailto) ---- */
  function flashCopied(btn) {
    var original = btn.dataset.label || btn.textContent.trim();
    btn.dataset.label = original;
    btn.classList.add("copied");
    var span = btn.querySelector(".btn-label") || btn;
    span.textContent = "Copied ✓";
    setTimeout(function () { span.textContent = original; btn.classList.remove("copied"); }, 1800);
  }
  function showToast(msg) {
    var toast = document.getElementById("toast");
    if (!toast) return;
    toast.querySelector(".toast-msg").textContent = msg;
    toast.classList.add("show");
    setTimeout(function () { toast.classList.remove("show"); }, 2200);
  }
  document.querySelectorAll("[data-copy-email]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var email = btn.getAttribute("data-copy-email");
      var done = function () { flashCopied(btn); showToast(email + " copied to clipboard"); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(email).then(done).catch(function () { legacyCopy(email); done(); });
      } else { legacyCopy(email); done(); }
    });
  });
  function legacyCopy(text) {
    var t = document.createElement("textarea");
    t.value = text; t.setAttribute("readonly", ""); t.style.position = "absolute"; t.style.left = "-9999px";
    document.body.appendChild(t); t.select();
    try { document.execCommand("copy"); } catch (e) {}
    document.body.removeChild(t);
  }

  /* ---- Reveal on scroll ---- */
  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Current year ---- */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
