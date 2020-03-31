/*
William Cao && Ethan Chen; Team Ethan Eats Cows
SoftDev pd1
K13 -- Ask Circles [Change || Die]
2020-03-31
 */

const svg = document.getElementById("vimage");
const clearButton = document.getElementById("clear");
const radius = 20;
const [canvasWidth, canvasHeight] = [svg.clientWidth, svg.clientHeight];

svg.addEventListener('click', (e) => {
    createNewCircle(e.offsetX, e.offsetY);
});

const handleFirstClick = (e) => {
    // Only want action to be done on the HTMLElement we clicked on, so use currentTarget

    e.currentTarget.setAttribute("fill", "#00FFFF");
    e.currentTarget.addEventListener("click", handleSecondClick);

    // Stop from making more circles and clicking circle underneath
    e.stopPropagation();
};

const handleSecondClick = (e) => {
    // Only remove what the event listener is attached to
    svg.removeChild(e.currentTarget);

    // Make sure circle doesn't go out of bounds
    const [cx, cy] = [Math.random() * (canvasWidth - 2 * radius) + radius, Math.random() * (canvasWidth - 2 * radius) + radius];
    createNewCircle(cx, cy);
};

const createNewCircle = (cx, cy) => {
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", String(cx));
    circle.setAttribute("cy", String(cy));
    circle.setAttribute("r", String(radius));
    circle.setAttribute("fill", "red");
    circle.setAttribute("stroke", "black");
    circle.addEventListener("click", handleFirstClick);
    svg.appendChild(circle);
};

clearButton.addEventListener('click', () => {
    while(svg.hasChildNodes()){
        svg.removeChild(svg.firstChild);
    }
});