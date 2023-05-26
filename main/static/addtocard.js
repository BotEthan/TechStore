// Add to cart function
function addToCart(productId) {
    // Get the user ID from the HTML template context
    var userId = '{{ user.id }}';
    
    // Send an AJAX POST request to the server to add the product to the basket model
    $.ajax({
      url: 'main:add_to_cart',
      method: 'POST',
      data: {
        user_id: userId,
        product_id: productId,
        quantity: 1,
        csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      success: function(response) {
        // Display a popup saying "Added to basket"
        alert("Added to basket");
      },
      error: function(xhr, status, error) {
        // Display an error message if the request fails
        alert("Error: " + error);
      }
    });
  }
  
$(document).ready(function() {
    $('.btn-add-to-cart').click(function(event) {
        var productId = $(this).attr('id').split('-')[3]; // get the product ID from the button ID
        addToCart(productId); // call the addToCart function with the product ID
    });
});