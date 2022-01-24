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
        });
        reader.readAsDataURL(file);
    }
});