$(function () {
  // Function to fetch and display the translation
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  // Bind click event to the button
  $('#btn_translate').click(fetchTranslation);

  // Bind keypress event to the input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key pressed
      fetchTranslation();
    }
  });
});
