// "Eric and Justin Eat Cows" Eric Lau William Cao Justin Shaw
// SoftDev1 pd1
// K08: What is it saving the screen from?
// 2020-02-13

// WHen you click the stop, the dvd will start again randomly somewhere

const canvas = document.getElementById('playground');
const context = canvas.getContext('2d');
const stopButton = document.getElementById('stop');
const animateCircleButton = document.getElementById('animateCircle');
const animateMovieButton = document.getElementById('animateMovie');
const movieLogo = new Image();
movieLogo.src = "dvd.png";
const movieWidth = 125;
const movieHeight = 100;
const canvasWidth = canvas.width;
const canvasHeight = canvas.height;
let movieX = 0;
let movieY = 0;
// default move down right
let deltaX = 1;
let deltaY = 1;

/**
 * The current frame the animation is at
 * @type {number}
 */
let animationTime = 0;
let animationMode = ""; // "c" or "m"

/**
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
    if(animationMode !== "m"){
        return;
    }

    context.clearRect(0, 0, 400, 400);
    context.drawImage(movieLogo, movieX, movieY, movieWidth, movieHeight);
};

const animateCircle = () => {
    if(animationMode !== "c"){
        return;
    }

    animationTime++;

    let radius = (animationTime) % 400;
    context.clearRect(0, 0, 400, 400);
    if (radius <= 200) {
        drawCircle(radius);
    } else {
        drawCircle(Math.abs(200 - radius + 200));
    }
    animationID = window.requestAnimationFrame(animateCircle);
};

const animateMovie = () => {
    drawMovie(150, 150);

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

const stop = () => {
    window.cancelAnimationFrame(animationID);
    animationMode = "";
}

stopButton.addEventListener('click', stop);

animateCircleButton.addEventListener('click', () => {
    // Stop all other animation
    stop();

    // Start/continue the circle animation
    if(animationMode !== "c"){
        animationID = window.requestAnimationFrame(animateCircle);
        animationMode = "c";
    }
});

animateMovieButton.addEventListener('click', () => {
    // Stop all other animation
    stop();

    if(animationMode !== "m"){
        // Start the movie animation.
        // Starting position resets each time
        movieX = Math.floor(Math.random() * (canvasWidth - movieWidth));
        movieY = Math.floor(Math.random() * (canvasHeight - movieHeight));
        // Starting velocity resets each time
        deltaX = 1;
        deltaY = 1;
        animationID = window.requestAnimationFrame(animateMovie);
        animationMode = "m";
    }
});