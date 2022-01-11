$('.btn-category').click(function() {
  if($(this).hasClass('more') == true) {
    $(this).hide();
    $('.btn-category.hide').show();
  } else if($(this).hasClass('active') == false) {
    $('.btn-category').removeClass('active');
    $(this).addClass('active');
  } 
});