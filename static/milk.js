
function success(data) {
    //process data for shopping page
    //come back and make this more dry
    //items with a console.log need data made for them
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
        } else if(milk.diet_name ==='Vegetarian'&& milk.baby_age >2 && milk.baby_age <=6) {
            vegetarianDiet2.push(milk);
        } else if(milk.diet_name ==='Vegan'&& milk.baby_age >2 && milk.baby_age <=6) {
            veganDiet2.push(milk);
        } else if(milk.diet_name ==='Gluten-Free'&& milk.baby_age >2 && milk.baby_age <=6) {
            glutenFree2.push(milk);
        } else if(milk.diet_name === 'Vegetarian' && milk.baby_age > 6) {
            vegetarianDiet3.push(milk);
        } else if(milk.diet_name === 'Vegan' && milk.baby_age > 6) {
            veganDiet3.push(milk);
            console.log(veganDiet3);
        } else if(milk.diet_name === 'Gluten-Free' && milk.baby_age > 6) {
            glutenFree3.push(milk);
        }
    });
}

function getRequest(){
    $.get("/milk.json",success);
}

getRequest();