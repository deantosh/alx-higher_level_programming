$(document).ready(function () {
  const langCode = $('#language_code').val();
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;
  $.get(url, function (data) {
    $('#hello').text(data.hello);
  });
});
