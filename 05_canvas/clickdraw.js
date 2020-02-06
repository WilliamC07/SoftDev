// The Cows -- Tiffany Cao and William Cao
// SoftDev1 pd1
// K04 -- I See a Red Door...
// 2020-02-05

var c = document.getElementById("slate")
var ctx = c.getContext("2d");
var mode = "rectangle"; // "rectangle" or "dot"
var modeDisplay = document.getElementById("modeDisplay");

document.getElementById("clear").addEventListener("click", (e) => {
    ctx.fillStyle = "#fff";
    ctx.fillRect(0, 0, c.width, c.height);
});

document.getElementById("switch").addEventListener("click", (e) => {
    // preventDefault prevents the default behavior of an element from happening.
    // In this case, the default behavior will refresh the page, which we don't want to happen.
    e.preventDefault();
    if(mode === "rectangle"){
        mode = "dot";
    }else{
        mode = "rectangle";
    }
    modeDisplay.innerHTML = mode;
});

c.addEventListener("click", (e) => {
    // Offset gives the (x, y) coordinate relative to the top left corner of the element clicked on
    var x = e.offsetX;
    var y = e.offsetY;
    if(mode === "rectangle"){
        ctx.fillStyle = "red";
        ctx.fillRect(x, y, 50, 100);
    }else{
        // beginPath() used to draw a line. Use in conjunction with ctx.stroke() to finishing drawing the line
        ctx.beginPath();
        ctx.fillStyle = "blue";
        ctx.arc(x, y, 5, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();
    }
});
