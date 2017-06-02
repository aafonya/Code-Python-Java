//Asynchronous - in the background, not requiring page refresh
//Javascript
//And
//XML - data format, similar to JSON - recently JSON became more popular than XML
//    - JSON become the industry standard data format

//AJAX - web development technicque to send and retrieve data in the background without refreshing the page



// create var that points towards html button element
var btn = document.getElementById("btn");
//create var that points towrds our div in the html
var animalContainer = document.getElementById("animal-info");
//create var for counting the number of clicks
var pageCounter = 1;




//setting up an element listener - when the button gets clicked
btn.addEventListener("click", function () {

    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-' + pageCounter + '.json');
    ourRequest.onload = function () {

        //errorhandling
        if (ourRequest.status >= 200 && ourRequest.status < 400) {
            //console.log(ourRequest.responseText);
            var ourData = JSON.parse(ourRequest.responseText);
            renderHTML(ourData);
        } else {
            console.log("We connected to the server but it returned an error.")
        }

    };

    ourRequest.onerror = function () {
        console.log("Connection error");
    };

    ourRequest.send();
    pageCounter++;
    if (pageCounter > 3) {
        btn.classList.add("hide-me");
    }
});

//add HTML to the page
function renderHTML(data) {
    var htmlString = "";

    for (i = 0; i < data.length; i++) {
        htmlString += "<p>" + data[i].name + " is a " + data[i].species + " that likes to eat ";

        for (ii = 0; ii < data[i].foods.likes.length; ii++) {
            if (ii === 0) {
                htmlString += data[i].foods.likes[ii];
            } else {
                htmlString += " and " + data[i].foods.likes[ii];
            }
        }

        htmlString += ' and dislikes ';

        for (ii = 0; ii < data[i].foods.dislikes.length; ii++) {
            if (ii === 0) {
                htmlString += data[i].foods.dislikes[ii];
            } else {
                htmlString += " and " + data[i].foods.dislikes[ii];
            }

        }
        htmlString += ".</p>"
    }

    /*var x;
    for (x in data) {
        htmlString += "<p>" + data[x].name + "is a" + x.species + ".</p>";
    } */

    animalContainer.insertAdjacentHTML('beforeend', htmlString);
};

