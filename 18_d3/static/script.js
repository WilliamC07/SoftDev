fetch("/data")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
    })
    .catch((e) => {
        alert(e);
    });

console.log("works");
