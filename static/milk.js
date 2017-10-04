
function success(data) {
    //process data for shopping page
    console.log(data);
    var vegetarianDiet = [];
    var veganDiet = [];
    var omnivore = [];
    var glutenFree = [];
    var vegetarianDiet2 = [];
    var veganDiet2 = [];
    var glutenFree2 = [];
    var vegetarianDiet3 = [];
    var veganDiet3 = [];
    var glutenFree3 = [];
    data.forEach(function(milk){
        if (milk.diet_name ==='Vegetarian' && milk.baby_age <= 2) {
            vegetarianDiet.push(milk);
        } else if (milk.diet_name ==='Vegan'&& milk.baby_age <= 2){
            veganDiet.push(milk);
            console.log(veganDiet);
        } else if(milk.diet_name ==='Gluten-Free'&& milk.baby_age <=2){
            glutenFree.push(milk);
            console.log(glutenFree);
        } else if(milk.diet_name ==='Omnivore'){
            omnivore.push(milk);
        }
    });
}

function getRequest(){
    $.get("/milk.json",success);
}

getRequest();