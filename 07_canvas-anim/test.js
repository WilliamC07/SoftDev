// "ERIC EATS COWS" Eric Lau & William Cao
// SoftDev1 pd1
// K #07: They lock us in the tower whenever we get caught
// 2020-02-12

const canvas = document.getElementById('playground');
const context = canvas.getContext('2d');
const stopButton = document.getElementById('stop');
const animateButton = document.getElementById('animate');

/**
 * The current frame the animation is at
 * @type {number}
 */
let animationTime = 0;
let isAnimationRunning = false;

/**
 * Used for canceling the animation.
 */
let animationID;

const drawCircle = (radius) => {
    context.beginPath();
    context.arc(200, 200, radius, 0, 2 * Math.PI);
    context.closePath();
    context.fill();
};

const animate = () => {
    animationTime++;

    let radius = (animationTime) % 400;
    context.clearRect(0, 0, 400, 400);
    if (radius <= 200) {
        drawCircle(radius);
    } else {
        drawCircle(Math.abs(200 - radius + 200));
    }
    animationID = window.requestAnimationFrame(animate);
};

const stop = () => {
    window.cancelAnimationFrame(animationID);
    isAnimationRunning = false;
};

const start = () => {
    if(!isAnimationRunning){
        animationID = window.requestAnimationFrame(animate);
        isAnimationRunning = true;
    }
};

stopButton.addEventListener('click', stop);
animateButton.addEventListener('click', start);