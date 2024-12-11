const slides = document.querySelectorAll(".slider .slide");
let currentIndex = 0;

function showNextImage() {
  slides[currentIndex].classList.remove("active");

  currentIndex = (currentIndex + 1) % slides.length; // Nächster Index

  slides[currentIndex].classList.add("active");
}

// Starte den Bildwechsel alle 3 Sekunden
setInterval(showNextImage, 5000);

// Aktiviere das erste Bild und dessen Bildunterschrift
slides[currentIndex].classList.add("active");

function openMenu() {
  document.getElementById("sideMenu").style.width = "250px"; /* Menü öffnen */
}

function closeMenu() {
  document.getElementById("sideMenu").style.width = "0"; /* Menü schließen */
}
