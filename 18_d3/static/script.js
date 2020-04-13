// References
// https://bl.ocks.org/d3noob/402dd382a51a4f6eea487f9a35566de0

fetch("/data")
    .then((response) => response.json())
    .then((data) => {
        // Example date entry: "1967-01-07"
        const parseDate = d3.timeParse("%Y-%m-%d");

        // Need to convert the date entry into something d3 can read
        for(const entry of data){
            entry.date = parseDate(entry.date);
        }
        drawGraph(data);
        console.log(data);
    })
    .catch((e) => {
        alert("Failed to get data from the server. See console for more information");
        console.log(e)
    });

const width = 500;
const height = 500;

// Scaling for graph
const scaleX = d3.scaleTime().range([0, width]);
// [height, 0] so that (0,0) is located bottom left
const scaleY = d3.scaleLinear().range([height, 0]);

const line = d3.line()
    .x(d => scaleX(d.date))
    .y(d => scaleY(d.count));

const graph = d3.select("#container")
    .append("svg")
    .attr("width", width + 300)
    .attr("height", height + 300)
    .append("g")
    .attr("transform", "translate(100, 100)");

/**
 * Data is formatted as:
 [
    {count: 208000, date: "1967-01-07"},
    {count: 207000, date: "1967-01-14"},
    ...
 ]
 * @param data
 */
function drawGraph(data){
    // get the domain and range of the data set
    const startDate = data[0].date;
    let endDate = data[data.length - 1].date;
    let maxInitialClaims = 0;
    for(const entry of data){
        maxInitialClaims = Math.max(maxInitialClaims, entry.count);
    }
    console.log(endDate, maxInitialClaims);
    // set the max X and max Y value for graph
    scaleX.domain([startDate, endDate]);
    scaleY.domain([0, maxInitialClaims]);

    // draw the graph
    graph.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", line);

    // add x axis
    graph.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(scaleX));

    graph.append("g")
        .call(d3.axisLeft(scaleY));
    console.log("finish");
}

function clearGraph(){
    d3.select("#container svg > *").remove();
}