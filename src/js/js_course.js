new WOW().init();

function slowScroll(id) {
  var offset = 0;
  $('html, body').animate({
    scrollTop: $(id).offset().top - offset
  }, 1000);
  return false;
}

let phoneBtn = document.getElementById("phonebtn");
let lessonBtn = document.getElementById("lessonBtn");

phoneBtn.addEventListener("mouseenter", function (event) {
  // highlight the mouseenter target
  event.target.classList.add("heartBeat");
  event.target.style.color = '#ffbf00';
}, false);
phoneBtn.addEventListener("mouseleave", function (event) {
  // highlight the mouseenter target
  event.target.classList.remove("heartBeat");
  event.target.style.color = '#f2f7f7';

}, false);

lessonBtn.addEventListener("mouseenter", function (event) {
  // highlight the mouseenter target
  event.target.style.transform = 'scale(1.1)';
}, false);
lessonBtn.addEventListener("mouseleave", function (event) {
  // highlight the mouseenter target
  event.target.style.transform = 'scale(1.0)';
}, false);