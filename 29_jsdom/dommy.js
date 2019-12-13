// William Cao and Joseph Yusufov
// SoftDev pd2
// K29 -- Sequential Progression III: Season of the Witch
// 2019-12-16

/**
 * @param e {Event} (First parameter given from EventTarget.addEventListener)
 */
const changeHeading = (e) => document.getElementById("h").innerHTML = e.target.innerHTML;

/**
 * @param e {Event} (First parameter given from EventTarget.addEventListener)
 */
const removeItem = (e) => e.target.remove();

const handleListEvent = (node) => {
    node.addEventListener('mouseover', changeHeading);
    node.addEventListener('mouseout', () => document.getElementById("h").innerHTML = "Hello World!");
    node.addEventListener('click', removeItem);
};

Array.from(document.getElementsByTagName("li"))
    .filter((item) => item.parentNode.id === "thelist")
    .forEach(handleListEvent);
/**
 * @param e {Event} (First parameter given from EventTarget.addEventListener)
 */
const addItem = function (e) {
    const list = document.getElementById("thelist");
    const item = document.createElement("li");
    item.innerHTML = "WORD";
    handleListEvent(item);
    list.appendChild(item);
};

const button = document.getElementById("b");
button.addEventListener('click', addItem);

const fib = function (n) {
    return n < 2 ?
        1 :
        fib(n - 1) + fib(n - 2);
};

const addFib = () => {
    const list = document.getElementById("fiblist");
    const children = list.childNodes;
    const item = document.createElement("li");
    item.innerHTML = fib(children.length - 1); // Minus one because every element has one child for text element
    list.appendChild(item);
};

/**
 * Optimized fib (dynamic programming)
 */
const addFib2 = () => {
    const fibList = document.getElementById("fiblist");
    const calculatedFibValues = fibList.childNodes;
    const nextFibItem = document.createElement("li");
    // length is always greater than 1 (from a text node automatically placed by browser)
    const length = calculatedFibValues.length;

    // If we are given 2 fib numbers already, we can calculate by just adding the last two numbers
    nextFibItem.innerHTML = length > 2 ?
        nextFibItem.innerHTML = parseInt(calculatedFibValues[length - 2].innerHTML) + parseInt(calculatedFibValues[length - 1].innerHTML) :
        "1";

    fibList.appendChild(nextFibItem);
};

const fb = document.getElementById("fb");
fb.addEventListener("click", addFib2);
