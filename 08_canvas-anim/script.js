// "Eric and Justin Eat Cows" Eric Lau William Cao Justin Shaw
// SoftDev1 pd1
// K08 -- What is it saving the screen from?
// 2020-02-13

const canvas = document.getElementById('playground');
const context = canvas.getContext('2d');
const stopButton = document.getElementById('stop');
const animateCircleButton = document.getElementById('animateCircle');
const animateMovieButton = document.getElementById('animateMovie');

const canvasWidth = canvas.width;
const canvasHeight = canvas.height;

const movieLogo = new Image();
movieLogo.src = "dvd.png";
const movieWidth = 125;
const movieHeight = 100;
// coordinate of the movie logo
let movieX = 0;
let movieY = 0;
// velocity of the movie logo moving
let deltaX = 1;
let deltaY = 1;

/**
 * The current frame the circle animation is at. This is not used for the movie logo animation
 * @type {number}
 */
let animationFrame = 0;
let animationMode = ""; // "c" or "m"

/**
 * This is shared between the movie logo movement and circle animation.
 * Used for canceling the animation.
 */
let animationID;

const drawCircle = (radius) => {
    context.fillStyle = "#D8E4FF";
    context.beginPath();
    context.arc(200, 200, radius, 0, 2 * Math.PI);
    context.closePath();
    context.fill();
};

const drawMovie = () => {
    context.clearRect(0, 0, canvasWidth, canvasHeight);
    context.drawImage(movieLogo, movieX, movieY, movieWidth, movieHeight);
};

const animateCircle = () => {
    animationFrame++;

    let radius = (animationFrame) % 400;
    context.clearRect(0, 0, canvasWidth, canvasHeight);
    if (radius <= 200) {
        // grow the circle
        drawCircle(radius);
    } else {
        // shrink the circle
        drawCircle(Math.abs(200 - radius + 200));
    }
    animationID = window.requestAnimationFrame(animateCircle);
};

const animateMovie = () => {
    drawMovie();

    movieX += deltaX;
    movieY += deltaY;

    if(movieX === 0 || movieX === canvasWidth - movieWidth){
        deltaX *= -1;
    }
    if(movieY === 0|| movieY === canvasHeight - movieHeight){
        deltaY *= -1;
    }

    animationID = window.requestAnimationFrame(animateMovie);
};

const stopAnimation = () => {
    window.cancelAnimationFrame(animationID);
    animationMode = "";
};

stopButton.addEventListener('click', stopAnimation);

animateCircleButton.addEventListener('click', () => {
    // Stop all other animation
    stopAnimation();

    // Start/continue the circle animation
    if(animationMode !== "c"){
        animationID = window.requestAnimationFrame(animateCircle);
        animationMode = "c";
    }
});

animateMovieButton.addEventListener('click', () => {
    // Stop all other animation
    stopAnimation();

    if(animationMode !== "m"){
        // Starting position resets each time we start the animation again
        movieX = Math.floor(Math.random() * (canvasWidth - movieWidth));
        movieY = Math.floor(Math.random() * (canvasHeight - movieHeight));

        // Starting velocity resets each time we start the animation again
        deltaX = 1;
        deltaY = 1;

        // Start the movie animation.
        animationID = window.requestAnimationFrame(animateMovie);
        animationMode = "m";
    }
});