
function addToCart(milk) {
    $.get('/add_to_cart', {milk: milk}, function(data) {
        $('#cart').html(" Item added to cart!");
         $('.checkout a span').html(data.count);
    });
}

$( document).ready(function() {
    console.log('hello i am ready');
    $.get("/update_cart_count", function(count) {
        $('.checkout a span').html(count);
    });
});

$('.buy_button').on('click', function() {
    var milk = $(this).data('tooltip');
    addToCart(milk);
});


