
function addToCart(milk) {
    $.get('/add_to_cart', {milk: milk}, function(data) {
        $('body').html(data);
    });
}

$('.buy_button').on('click', function() {
    var milk = $(this).data('tooltip');
    addToCart(milk);
});