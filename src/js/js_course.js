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
if (phoneBtn) {
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
  
}

if (lessonBtn) {
  lessonBtn.addEventListener("mouseenter", function (event) {
    // highlight the mouseenter target
    event.target.style.transform = 'scale(1.1)';
  }, false);
  lessonBtn.addEventListener("mouseleave", function (event) {
    // highlight the mouseenter target
    event.target.style.transform = 'scale(1.0)';
  }, false);
  
}
if (arrowTopBtn){
  arrowTopBtn.onclick = function() {
    window.scrollTo(pageXOffset, 0);
  };
 
  window.addEventListener('scroll', function() {
    arrowTopBtn.hidden = (pageYOffset < document.documentElement.clientHeight);
  });
}



async function fetchEvents(name) {
  try {
    const response = await fetch('https://script.google.com/macros/s/AKfycbyDdXCV34b6Y1fWpi7H-TKahOOe2olSkE6emOr8aLXZ6XpVGHMrajAvA08bAUbd4tE-EA/exec');
  const events = await response.json();
  const eventsList = document.getElementById('events');
  // Знайти найближчу подію з назвою "Фронтенд - Саша"
  const targetEvent = events
    .filter(event => event.title === name)
    .sort((a, b) => new Date(a.startTime) - new Date(b.startTime))[0];

  if (targetEvent) {
    const eventDate = new Date(targetEvent.startTime);
    const formattedDate = eventDate.toLocaleDateString('uk-UA', { day: 'numeric', month: 'long' });
    const formattedTime = eventDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });


    // Оновити HTML-елемент
    document.getElementById('eventDate').innerHTML += formattedDate;
    document.getElementById('eventTime').innerHTML += formattedTime;
  } else {
    console.log('Подія', name,' не знайдена');
  }
} catch (error) {
  console.error('Error fetching events:', error);
}}
