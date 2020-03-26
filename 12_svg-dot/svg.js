/*
William Cao && Ethan Chen; Team Ethan Eats Cows
SoftDev pd1
K12 -- Connect the Dots
2020-03-30
 */

const svg = document.getElementById("vimage");
const clearButton = document.getElementById("clear");
const points = [];  // array of points as [x, y, x, y, x, y ...]

svg.addEventListener('click', (e) => {
    points.push(e.offsetX, e.offsetY);
    // draw circle
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", String(e.offsetX));
    circle.setAttribute("cy", String(e.offsetY));
    circle.setAttribute("r", "5");
    circle.setAttribute("fill", "red");
    circle.setAttribute("stroke", "black");
    svg.appendChild(circle);

    if(points.length >= 4){
        // draw line
        const lastTwoPoints = points.slice(points.length - 4);

        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", String(lastTwoPoints.shift()));
        line.setAttribute("y1", String(lastTwoPoints.shift()));
        line.setAttribute("x2", String(lastTwoPoints.shift()));
        line.setAttribute("y2", String(lastTwoPoints.shift()));
        line.setAttribute("stroke", "yellow");
        line.setAttribute("stroke-width", "2");
        svg.appendChild(line);
    }
});

clearButton.addEventListener('click', () => {
    points.length = 0;

    while(svg.hasChildNodes()){
        svg.removeChild(svg.firstChild);
    }
});