$(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
