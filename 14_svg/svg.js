/*
William Cao
SoftDev pd1
K14: Ask Circles [Change || Die] While Moving, etc.
2020-04-01
 */

const svg = document.getElementById("vimage");
const radius = 20;
const [canvasWidth, canvasHeight] = [svg.clientWidth, svg.clientHeight];
/* To differentiate between circles */
const keyAttribute = "data-key";
let keyCounter = 0;
// To keep track of each individual circle position and velocity
// Key: keyAttribute value (a number)
// Value: [[x, y], [velocityX, velocityY]]
const circleMovementData = {};
let animationID;

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
    circle.setAttribute(keyAttribute, String(keyCounter));
    circle.addEventListener("click", handleFirstClick);
    svg.appendChild(circle);

    circleMovementData[keyCounter] = [
        [cx, cy],
        // Randomly choose direction to move ball in ([velocityX, velocityY])
        [randomBoolean() ? -1 : 1, randomBoolean() ? -1 : 1]
    ];
    keyCounter++;
};

const handleMovement = () => {
    for(const circle of svg.children){
        const [position, velocity] = circleMovementData[circle.getAttribute(keyAttribute)];
        position[0] += velocity[0];
        position[1] += velocity[1];

        circle.setAttribute("cx", String(position[0]));
        circle.setAttribute("cy", String(position[1]));

        // Flip ball direction to stop going off screen
        if(position[0] <= radius || position[0] >= canvasWidth - radius){
            velocity[0] *= -1;
        }
        if(position[1] <= radius || position[1] >= canvasHeight - radius){
            velocity[1] *= -1;
        }
    }

    animationID = window.requestAnimationFrame(handleMovement);
};

document.getElementById("clear").addEventListener('click', () => {
    while(svg.hasChildNodes()){
        svg.removeChild(svg.firstChild);
    }
});

document.getElementById("move").addEventListener("click", () => {
    if(animationID === undefined){
        animationID = window.requestAnimationFrame(handleMovement);
    }
});

document.getElementById("stop").addEventListener("click", () => {
    window.cancelAnimationFrame(animationID);
    animationID = undefined;
});


// Helper functions
const randomBoolean = () => {
    // random is [0, 1)
    return Math.random() >= .5;
};