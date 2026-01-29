// static/js/main.js

// 1. Initialize on load
const initTheme = () => {
  if (
    localStorage.theme === "dark" ||
    (!("theme" in localStorage) &&
      window.matchMedia("(prefers-color-scheme: dark)").matches)
  ) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
};
initTheme(); // Run immediately

// 2. Toggle function (Global scope)
function toggleTheme() {
  const html = document.documentElement;
  if (html.classList.contains("dark")) {
    html.classList.remove("dark");
    localStorage.theme = "light";
  } else {
    html.classList.add("dark");
    localStorage.theme = "dark";
  }
}

// Open Service Modal
function openServiceModal(serviceId) {
  const overlay = document.getElementById("service-modal-overlay");
  const modalContent = document.getElementById("modal-" + serviceId);

  // Show overlay
  overlay.classList.remove("hidden");
  setTimeout(() => overlay.classList.add("opacity-100"), 10);

  // Show specific content
  modalContent.classList.remove("hidden");
  setTimeout(() => modalContent.classList.add("scale-100"), 10);

  // Prevent body scroll
  document.body.style.overflow = "hidden";
}

// Close Service Modal
function closeServiceModal() {
  const overlay = document.getElementById("service-modal-overlay");
  const allContents = document.querySelectorAll(".service-modal-content");

  overlay.classList.remove("opacity-100");
  allContents.forEach((c) => c.classList.remove("scale-100"));

  setTimeout(() => {
    overlay.classList.add("hidden");
    allContents.forEach((c) => c.classList.add("hidden"));
    document.body.style.overflow = "auto"; // Re-enable scroll
  }, 300);
}

// Close on clicking overlay (outside the box)
window.onclick = function (event) {
  const overlay = document.getElementById("service-modal-overlay");
  if (event.target == overlay) {
    closeServiceModal();
  }
};
