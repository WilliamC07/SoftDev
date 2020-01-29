// Mohidul Abedin, William Cao
// SoftDev1 pd2
// K28 -- Sequential Progression II: Electric Boogaloo
// 2019-12-12

document.getElementById("fib").addEventListener("click", (event) => handle_click(event, fibonacci(5)));
document.getElementById("gcd").addEventListener("click", (event) => handle_click(event, gcd(204, 44)));
document.getElementById("randomStudent").addEventListener("click", (e) => handle_click(event, randomStudent()));

var handle_click = (event, answer) => {
    // https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentElement
    // https://developer.mozilla.org/en-US/docs/Web/API/EventListener
    var answer_display = document.createElement("p");
    answer_display.innerHTML = "The answer is " + answer;
    event.target.insertAdjacentElement('afterend', answer_display);
}

var fibonacci = function(n) {
    var compute = (n) => {
        if (n == 0) {
            return 0;
        }
        else {
            if (n == 1 || n == 2) {
                return 1;
            }
        }
        return compute(n-2) + compute(n-1);
    }

    var answer = compute(n);
    console.log("The sequence value is ", answer);
    return answer;
}

var gcd = (a, b) => {
    var greatest = 1;
    for(var i = 1; i <= Math.min(a,b); i++) {
        if ((a % i == 0) && (b % i == 0)) {
            greatest = i;
        }
    }
    console.log(`The greatest common factor of ${a} and ${b} is ${greatest}`);
    return greatest;

}

var students = ["Dub Cao", "Coyote", "Matthew", "Blobfish"]
var randomStudent = function() {
    var student = students[parseInt(Math.random() * students.length)];
    console.log("Randomly selected student:", student);
    return student;
}
