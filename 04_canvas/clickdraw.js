// The Cows -- Tiffany Cao and William Cao
// SoftDev1 pd1
// K04 -- I See a Red Door...
// 2020-02-05

var c = document.getElementById("slate")
var ctx = c.getContext("2d");
var mode = "rectangle"; // "rectangle" or "dot"
var modeDisplay = document.getElementById("modeDisplay");
var drawingInstructions = [];

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
    var x = e.pageX - c.offsetLeft;
    var y = e.pageY - c.offsetTop;
    drawingInstructions.push(x);
    drawingInstructions.push(y);

    // console.log('clicked');
    if(mode === "rectangle"){
        if(drawingInstructions.length === 4){
            ctx.fillStyle = "#ff0000";
            let xPos = drawingInstructions.shift();
            let yPos = drawingInstructions.shift();
            let width = drawingInstructions.shift() - xPos;
            let height = drawingInstructions.shift() - yPos;
            ctx.fillRect(xPos, yPos, width, height);
        }
    }else{
        ctx.fillRect(drawingInstructions.shift(), drawingInstructions.shift(), 3, 3);
    }
});