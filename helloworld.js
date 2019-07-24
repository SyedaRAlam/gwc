// console.log("Hello World");
//
// var h1tag = document.getElementsByTagName("h1")[0];
// var loc = document.getElementsByClassName("headings")[3];
var adjectives = ["cute", "funny", "nice", "adorable", "B-Baller", "lovely", "wonderful", "athletic"]
var pos = 0;


var loc = document.getElementById("adjective");
function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos = 0;
  }
}

Math.random()
var x = document.getElementsByTagName("body")[0]
function colorfulBackground(){
  x.setAttribute("style", `background-color : rgb(${Math.floor(Math.random()*256)}, ${Math.floor(Math.random()*256)}, ${Math.floor(Math.random()*256)})`)
}

var foz = document.getElementById("the name")
// console.log(foz)
function changeFontColor(){
  foz.setAttribute("style", "color : red")
}


var poz = 0
var fonts = ["'Bonbon', cursive", "'Geostar', cursive", "'Hanalei', cursive", "'Butcherman', cursive"];
function fontChange(){
  // console.log("gfdgd");
  // foz.setAttribute("style",`font-family: ${fonts[poz]}`);
  foz.style.fontFamily = fonts[poz];
    // console.log("gfdgd")
  poz ++;
  if (poz >= fonts.length){
    poz = 0;
  }
}
