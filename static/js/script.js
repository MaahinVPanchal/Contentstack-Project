let menu = document.querySelector("#menu-icon");
let navlist = document.querySelector(".navlist");
let scrollDown = document.querySelector(".scroll-down");
let developerSection = document.getElementById("developer-section");

menu.onclick = () => {
  menu.classList.toggle("bx-x");
  navlist.classList.toggle("open");
};

// ScrollReveal for animations
const sr = ScrollReveal({
  distance: "65px",
  duration: 2600,
  delay: 450,
  reset: true,
});

sr.reveal(".hero-text", { delay: 200, origin: "top" });
sr.reveal(".hero-img", { delay: 450, origin: "top" });
sr.reveal(".icons", { delay: 500, origin: "left" });
sr.reveal(".scroll-down", { delay: 500, origin: "left" });

// Toggle Developer Section Visibility
scrollDown.onclick = (event) => {
  event.preventDefault(); // Prevent the default anchor click behavior
  if (
    developerSection.style.display === "none" ||
    developerSection.style.display === ""
  ) {
    developerSection.style.display = "block"; // Show the developer section
    scrollDown.style.display = "none"; // Optionally hide the scroll-down arrow after clicking
  } else {
    developerSection.style.display = "none"; // Hide if clicked again
    scrollDown.style.display = "block"; // Show the scroll-down arrow again
  }
};

// Toggle Details for Team Members
const arrows = document.querySelectorAll(".arrow");

arrows.forEach((arrow) => {
  arrow.addEventListener("click", function (event) {
    event.preventDefault();
    const details = this.nextElementSibling;
    if (details.style.display === "none" || !details.style.display) {
      details.style.display = "block";
      this.innerHTML = '<i class="bx bx-up-arrow"></i> Hide Details';
    } else {
      details.style.display = "none";
      this.innerHTML = '<i class="bx bx-down-arrow"></i> See Details';
    }
  });
});
