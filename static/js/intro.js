$('.intro1').click(function(){
  $(this).fadeOut(1000);
  $('.intro2').fadeIn(1500);
  setInterval(() => {
    $('.intro2').hide();
  }, 2500);
  setInterval(() => {
    $('.welcome').animate({'height':'70%'}, 500);
    $('.naver').animate({
      'margin-top':'20px',
      'opacity':'1'
    }, 1000);
    $('.kakao').animate({
      'margin-top':'20px',
      'opacity':'1'
    }, 1200);
    $('.google').animate({
      'margin-top':'20px',
      'opacity':'1'
    }, 1400);
  }, 2500);
});