/* Fade in on scroll effect */
/* $(document).ready(function() {
  var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
  if (!isMobile) {
      $(window).scroll( function(){
        $('.linguaFade').each( function(i){
            
            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            if( bottom_of_window > bottom_of_object ){
                
                $(this).animate({'opacity':'1'},1200);                  
            }        
        });  
    }); 
  }
}); */
/* Accept privacy agreement to submit form */
$( document ).ready(function() {
  $('#privacy-btn').hide();
  $('#id_agree').change(function(){
    if ( document.getElementById('id_agree').checked == true ){
      $('#privacy-btn').show();
    }
    else {
      $('#privacy-btn').hide();
    }
  })
});

/* Maps */
/* Get latitude and longitute values from template */
var lat = document.getElementById('lat').innerHTML;
var long = document.getElementById('long').innerHTML;

var mymap = L.map('mapid').setView([lat, long], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoibGluZ3VhIiwiYSI6ImNqcnhjZXc4ejBrMWM0YXBrYnpmeDFmeDgifQ.CNQ1eaCszfeuByLLZT0vjg'
}).addTo(mymap);

/* var greenIcon = L.icon({
  iconUrl: 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.gNFiO1vpZ66eHRt_T1oB9gHaHW%26pid%3D15.1&f=1',
  shadowUrl: 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.gNFiO1vpZ66eHRt_T1oB9gHaHW%26pid%3D15.1&f=1',

  iconSize:     [50, 50], // size of the icon
  shadowSize:   [50, 64], // size of the shadow
  iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
  shadowAnchor: [4, 62],  // the same for the shadow
  popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});
{icon: greenIcon}) to add after [lat, long] */

var marker = L.marker([lat, long]).addTo(mymap);
marker.bindPopup("<b>Hello student!</b><br>University adderss.").openPopup();

/* Faqs */
const items = document.querySelectorAll(".accordion a");

function toggleAccordion(){
  this.classList.toggle('active');
  this.nextElementSibling.classList.toggle('active');
}

items.forEach(item => item.addEventListener('click', toggleAccordion));

/* Profile section */
$(document).ready(function(){
  $('[data-toggle="offcanvas"]').click(function(){
      $("#navigation").toggleClass("hidden-xs");
  });
});