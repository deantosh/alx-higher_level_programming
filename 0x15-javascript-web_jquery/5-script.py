/* global $ */
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('ul.my_list').append($('<li>').text('Item'));
  });
});
