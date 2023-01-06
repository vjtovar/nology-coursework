"use strict";
var bombLocation = Math.floor(Math.random() *9)
var treasureLocation = Math.floor(Math.random() *9)
var turns = 3



while(bombLocation === treasureLocation) {
    treasureLocation = Math.floor(Math.random() *9)
}

const treasure = (location) =>{
    if(turns > 0) {
        if(location === treasureLocation) {
            document.getElementById(location).innerHTML = "&#x1F3C6"
            alert("You found the treasure!")
            turns = 0
        } else if(location === bombLocation) {
            document.getElementById(location).innerHTML = "&#x1F480"
            alert("You Died!")
            turns = 0
        } else {
            document.getElementById(location).innerHTML = "&#x274C"
            turns = turns -1;
        }
    } else {
        alert("You have run out of turns!")
    }
}