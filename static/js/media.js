function open_image_input() {
  $('#imageInput').click();
}

function open_images_input() {
  $('#imagesInput').click();
}

$('#imageInput').change(function() {
  var file = this.files[0];
  var reader = new FileReader();
  reader.onloadend = function() {
      $('#thumbnailImage').css('background-image', 'url("' + reader.result + '")');
  }
  if (file) {
      reader.readAsDataURL(file);
  } else {}
});

$('#imagesInput').change(function() {
  var $preview = $('#preview');
  $img_count = $('.img-count');

  if ($img_count.text() == "10") {
      alert("사진은 10장까지 등록할 수 있습니다.");
  } else {
      if (this.files) $.each(this.files, readAndPreview);
      $img_count.text(String($('.uploaded-img').length + 1))
  }

  function readAndPreview(i, file) {
      var tmp_images = []
      if (!/\.(jpe?g|png|gif)$/i.test(file.name)) {
          return alert(file.name + " 파일은 이미지 형식이 아닙니다.");
      }

      var reader = new FileReader();
      $(reader).on("load", function() {

          $preview.prepend(
              $(
                  "<div />", {
                      class: "uploaded-img",
                      style: "background-image: url('" + this.result + "' )",
                  }
              )
          );

          $body = $('body');
          $modalImg = $('#imgView');

          $('.uploaded-img').on('click', function () {
            $body.addClass('modal_in');
            $modalImg.fadeIn(300);
            $body.css('padding-right', getScrollWidth());
            // var img_url = $(this).css("background-image");
            var img_url = $(this).css("background-image").replace(/^url\(['"](.+)['"]\)/, '$1');

            // console.log(img_url);
            $('#imgView').find('.img-wrap img').attr('src', img_url);
          });

          $('.close_btn, .modal_dim').on('click', function () {
            var speed = 300;
            $modalImg.fadeOut(speed);
            setTimeout(function () {
              $body.removeClass('modal_in');
              $body.css('padding-right', 0)
            }, speed)
          });

          function getScrollWidth() {
            var body = document.querySelector('body');
            var scrollDiv = document.createElement('div');
            scrollDiv.className = 'fake_sjwidth';
            body.appendChild(scrollDiv);
            var scrollbarWidth = $(document).height() > $(window).height() ? scrollDiv.offsetWidth - scrollDiv.clientWidth :
              0;

            body.removeChild(scrollDiv);
            return scrollbarWidth;
          }
      });
      reader.readAsDataURL(file);
  }
});