/* $(function(){
  boxRollovers();
});

function boxRollovers()
{
  $selector = $("li");
  XAngle = 0;
  YAngle = 0;
  Z = 50;
  
  $selector.on("mousemove",function(e){
    var $this = $(this);
    var XRel = e.pageX - $this.offset().left;
    var YRel = e.pageY - $this.offset().top;
    var width = $this.width();
  
    YAngle = -(0.5 - (XRel / width)) * 40; 
    XAngle = (0.5 - (YRel / width)) * 40;
    updateView($this.children(".icon"));
  });
  
  $selector.on("mouseleave",function(){
    oLayer = $(this).children(".icon");
    oLayer.css({"transform":"perspective(525px) translateZ(0) rotateX(0deg) rotateY(0deg)","transition":"all 150ms linear 0s","-webkit-transition":"all 950ms linear 0s"});
    oLayer.find("strong").css({"transform":"perspective(525px) translateZ(0) rotateX(0deg) rotateY(0deg)","transition":"all 150ms linear 0s","-webkit-transition":"all 950ms linear 0s"});
  });
}

function updateView(oLayer)
{
  oLayer.css({"transform":"perspective(525px) translateZ(" + Z + "px) rotateX(" + XAngle + "deg) rotateY(" + YAngle + "deg)","transition":"none","-webkit-transition":"none"});
  oLayer.find("strong").css({"transform":"perspective(525px) translateZ(" + Z + "px) rotateX(" + (XAngle / 0.66) + "deg) rotateY(" + (YAngle / 0.66) + "deg)","transition":"none","-webkit-transition":"none"});
}
 */

/* Fade in on scroll effect */
$(document).ready(function() {
  var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
  if (!isMobile) {
      $(window).scroll( function(){
        $('.linguaFade').each( function(i){
            
            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            if( bottom_of_window > bottom_of_object ){
                
                $(this).animate({'opacity':'1'},1000);                  
            }        
        });  
    }); 
  }
});
/* Faqs */
const items = document.querySelectorAll(".accordion a");

function toggleAccordion(){
  this.classList.toggle('active');
  this.nextElementSibling.classList.toggle('active');
}

items.forEach(item => item.addEventListener('click', toggleAccordion));


$("#menu-toggle").click(function(e) {
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});
$("#menu-toggle-2").click(function(e) {
  e.preventDefault();
  $("#wrapper").toggleClass("toggled-2");
  $('#menu ul').hide();
});

$( document ).ready(function() {
  /* Dashboard */
  $(".main-sub-menu").on("click",function(){
    $('.main-sub-menu').find(".fa-angle-right").css({"transform":"rotate(0deg)"});
    $(this).find("ul").slideToggle();
    $(".main-menu .main-sub-menu").removeClass("dashboard-active");
    $(this).addClass("dashboard-active");
    $(this).find(".fa-angle-right").css({"transform":"rotate(90deg)"});
  }); 

  /* Accept privacy agreement to submit form */
  $('#privacy-btn').hide();
  $('#id_agree').change(function(){
    if ( document.getElementById('id_agree').checked == true ){
      $('#privacy-btn').show();
    }
    else {
      $('#privacy-btn').hide();
    }
  })

  //slider
  $('.customer-logos').slick({
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1500,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    responsive: [{
        breakpoint: 768,
        settings: {
            slidesToShow: 4
        }
    }, {
        breakpoint: 520,
        settings: {
            slidesToShow: 3
        }
    }]
  });
});

/* Maps
* If page does't contain lat long, the script will stop
* Add check to see if page is correct or move this at the bottom
*/
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

var address = document.getElementById('address').innerHTML;

var marker = L.marker([lat, long]).addTo(mymap);
marker.bindPopup("<b>Hello student!</b><br>" + address).openPopup();