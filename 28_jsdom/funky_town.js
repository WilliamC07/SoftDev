document.getElementById("fib").addEventListener("click", () => console.log(fibonacci(5)))
document.getElementById("gcd").addEventListener("click", () => console.log(gcd(204, 44)))
document.getElementById("randomStudent").addEventListener("click", () => console.log(randomStudent()))

var fibonacci = function(n) {
    if (n == 0) {
        return 0;
    }
    else {
        if (n == 1 || n == 2) {
            return 1;
        }
    }
    return fibonacci(n-2) + fibonacci(n-1);
}

var gcd = (a, b) => {
    var greatest = 1;
    for(var i = 1; i <= Math.min(a,b); i++) {
        if ((a % i == 0) && (b % i == 0)) {
            greatest = i;
        }
    }
    return greatest;

}

var students = ["Dub Cao", "Coyote", "Matthew", "Blobfish"]
var randomStudent = function() {
    return students[parseInt(Math.random() * students.length)];
}
