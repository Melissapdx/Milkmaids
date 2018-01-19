
//displays message letting user know item was added to cart and increments count with ajax
function addToCart(milk) {
    $.get('/add_to_cart', {milk: milk}, function(data) {
        if(data.error !== undefined){
            $('#cart').html(data.error);
        } else {
            $('#cart').html(" Item added to cart!");
            $('.checkout a span').html(data.count);
        }
    });
}

//reloads customer cart count on page
$( document).ready(function() {
    $.get("/update_cart_count", function(count) {
        $('.checkout a span').html(count);
    });
});
//ajax call when user clicks button
$('.buy_button').on('click', function() {
    var milk = $(this).data('tooltip');
    addToCart(milk);
});
//shows or hides items on product page based on what user clicks on
$('.milk-nav a').on('click',function() {
    var milkDiet = $(this).data('milktype');//storing diet name string from data 
    var selectDiv = $('#' + milkDiet);
    selectDiv.siblings().hide();
    selectDiv.show();
});


//removes item from customers cart, user clicks on button and div is removed from cart 
$('.remove').on('click',function(){
    $(this).closest('.cart-item').remove();
});

