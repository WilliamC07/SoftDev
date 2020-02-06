// The Cows -- Tiffany Cao and William Cao
// SoftDev1 pd1
// K04 -- I See a Red Door...
// 2020-02-05

var c = document.getElementById("slate")
var ctx = c.getContext("2d");
var mode = "rectangle"; // "rectangle" or "dot"
var modeDisplay = document.getElementById("modeDisplay");

document.getElementById("clear").addEventListener("click", () => {
    ctx.fillStyle = "#fff";
    ctx.fillRect(0, 0, c.width, c.height);
});

document.getElementById("switch").addEventListener("click", () => {
    if(mode === "rectangle"){
        mode = "dot";
    }else{
        mode = "rectangle";
    }
    modeDisplay.innerHTML = mode;
});

c.addEventListener("click", (e) => {
    var x = e.offsetX;
    var y = e.offsetY;
    // console.log('clicked');
    if(mode === "rectangle"){
        ctx.fillStyle = "red";
        ctx.fillRect(x, y, 50, 100);
    }else{
        ctx.beginPath();
        ctx.arc(x, y, 5, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fillStyle = "blue";
        ctx.fill();
    }
});