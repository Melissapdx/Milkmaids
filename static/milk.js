
function addToCart(milk) {
    $.get('/add_to_cart', {milk: milk}, function(data) {
        $('#cart').html(data);
    });
}
function miniCart(cart){

}

$('.buy_button').on('click', function() {
    var milk = $(this).data('tooltip');
    //var cart = $(this).data('tooltip');
    addToCart(milk);
});


