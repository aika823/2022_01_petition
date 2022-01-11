console.clear();

$('.slide-recommend').on('init', function(event, slick) {
  $('.slide-recommend').find('.slick-current').removeClass('slick-active').addClass('reset-animation');
  setTimeout( function() {
    $('.slide-recommend').find('.slick-current').removeClass('reset-animation').addClass('slick-active');
  }, 1);
  $('.slick-active .graph-bar-percent').animate({"width": $('.slick-current .percent').text()});
});

$('.slide-recommend').slick({
  infinite: false,
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: false,
  dots: true,
  centerMode: true,
  // focusOnSelect: true
  centerPadding:'50px',
  adaptiveHeight:true,
}).on("afterChange", function(){
  $percent = $('.slick-current .percent').text();
$('.slick-current .graph-bar-percent').animate({"width": $percent}, 300);
});

$percent = $('.slick-current .percent').text();
$('.slick-current .graph-bar-percent').animate({"width": $percent}, 300);