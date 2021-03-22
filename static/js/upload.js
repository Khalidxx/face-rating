function readURL(input) {
  if (input.files && input.files[0]) {

    var reader = new FileReader();

    reader.onload = function(e) {
      $('.image-upload-wrap').hide();

      $('.file-upload-image').attr('src', e.target.result);
      $('.file-upload-content').show();

      $('.image-title').html(input.files[0].name);

      $(".rate-content").show();
    };

    reader.readAsDataURL(input.files[0]);

  } else {
    removeUpload();
  }
}
  
function removeUpload() {
  $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content').hide();
  $(".rate-content").hide()
  $('.image-upload-wrap').show();
}

$('.image-upload-wrap').bind('dragover', function () {
  $('.image-upload-wrap').addClass('image-dropping');
});

$('.image-upload-wrap').bind('dragleave', function () {
  $('.image-upload-wrap').removeClass('image-dropping');
});

function rateImage() {
  var file = $(".file-upload-input")[0].files[0];
  
  const fd = new FormData();
  fd.append('image', file);
  

  fetch(`${window.origin}/rate`, {
    method: "POST",
    body: fd,
    cache: "no-cache",
    // headers: new Headers({
    //   "content-type": "application/json"
    // })
  })
  .then(function(response) {
    if (response.status !== 200) {
      console.log(`Looks like there was a problem. Status code: ${response.status}`);
      return;
    }
    response.json().then(function(data) {
      console.log(data);
    });
  })
  .catch(function(error) {
    console.log("Fetch error: " + error);
  });



  // if (file) {
  //   reader.readAsDataURL(file);
  //   console.log(file)
  // } else {
  //   preview.src = "";
  // }
}
  