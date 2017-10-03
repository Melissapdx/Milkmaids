"use strict";

function showMilk() {
    $.get("/milk.json",function(results){
        $.('#product').html(results);
});

$('.buy').on('click',showMilk);