// William Cao and Joseph Yusufov 
// SoftDev pd2 
// K29 -- Sequential Progression III: Season of the Witch 
// 2019-12-13 
var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e.target.innerHTML;
};

var removeItem = function(e) {
    e.target.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
    lis[i].addEventListener( 'mouseover', changeHeading);
    lis[i].addEventListener( 'mouseout', () => {
	document.getElementById("h").innerHTML = "Hello World!";
    });

    lis[i].addEventListener( 'click', removeItem);
    
}

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    //var listen = item.addEventListener;
    item.addEventListener( 'mouseover', changeHeading); 
    item.addEventListener( 'mouseout', () => document.getElementById("h").innerHTML = "Hello World!");
    item.addEventListener( 'click', removeItem);
    list.appendChild(item);        
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if ( n < 2 ) {
	return 1;
    } else {
	return fib(n-1) + fib(n-2);
    }
};

var addFib = function(e) {
    // console.log(e);
    var list = document.getElementById("fiblist");
    var children = list.childNodes;
    var item = document.createElement("li");
    item.innerHTML = fib(children.length - 1); // Minus one because every element has one child.
    list.appendChild(item);
};

var addFib2 = function(e) {
    // console.log(e);
    var list = document.getElementById("fiblist");
    var children = list.childNodes;
    var item = document.createElement("li");
    var length = children.length;

    if (length > 2) {
	item.innerHTML = parseInt(children[length - 2].innerHTML) + parseInt(children[length - 1].innerHTML); // Minus one because every element has one child.
    } else {
	item.innerHTML = "1"; // Minus one because every element has one child.	
    }
    list.appendChild(item);
};

var fb = document.getElementById("fb");
fb.addEventListener( "click", addFib2 );
