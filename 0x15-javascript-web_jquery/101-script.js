$(function () {
  // Add a new item when the user clicks on DIV#add_item
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  // Remove the last item when the user clicks on DIV#remove_item
  $('#remove_item').click(function () {
    $('.my_list li:last').remove();
  });

  // Clear all items when the user clicks on DIV#clear_list
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
