/*
 * William Cao & Ethan Chen
 * SoftDev1 pd1
 * K06 -- Dot Dot Dot
 * 2020-02-11
 */
const canvas = document.getElementById("playground");
const context = canvas.getContext("2d");
let previousPoint = undefined; // [x, y]

// can clear canvas
document.getElementById("clear").addEventListener("click", () => {
    context.fillStyle = "white";
    context.fillRect(0, 0, canvas.width, canvas.height);
    // Do not continue drawing line off of what was clicked before clear
    previousPoint = undefined;
});

// can draw dots and connect previous
canvas.addEventListener("click", (e) => {
    const clickedPoint = [e.offsetX, e.offsetY];
    // draw a point for where the user clicked
    context.fillStyle = "blue";
    context.fillStyle = "blue";
    context.beginPath();
    context.arc(...clickedPoint, 5, 0, 2 * Math.PI);
    context.stroke();
    context.fill();
    // connect to previous point if one exists
    if(previousPoint != undefined){
        // there is a previous point
        context.beginPath();
        context.moveTo(...previousPoint);
        context.lineTo(...clickedPoint);
        context.stroke();
    }
    previousPoint = clickedPoint;
});
