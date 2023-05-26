function scrollToElement(element) {
    console.log("Scrolling to contact...");
    $('html, body').animate({
      scrollTop: $(element).offset().top
    }, 1000);
  }

$(document).ready(function() {
    // Attach mouseenter and mouseleave event handlers to the images
    $(".card-img-top").on({
      mouseenter: function() {
        $(this).attr("data-original", $(this).attr("src")); // store original image path
        $(this).fadeOut(200, function(){
            $(this).attr("src", $(this).attr("alt")).fadeIn(200); // set alt image path
        });
      },
      mouseleave: function() {
        $(this).fadeOut(200, function(){
            $(this).attr("src", $(this).attr("data-original")).fadeIn(200); // set original image path
        })
      }
    });
  });