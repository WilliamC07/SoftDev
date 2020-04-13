/**
 * William Cao, Henry Liu, Ethan Chen -- HEW
 * SoftDev pd1
 * K18 -- Come Up For Air
 * 2020-04-21
 */

// References
// https://bl.ocks.org/d3noob/402dd382a51a4f6eea487f9a35566de0

const width = 800;
const height = 500;
const animationDuration = 30; // in seconds
const updatesPerSecond = 20;
let data;

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
    setScaling(data, scaleX, scaleY);

    // draw the graph
    graph.append("path")
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", line(data));

    // add x axis
    graph.append("g")
        .attr("transform", "translate(0," + height + ")")
        .attr("class", "x-axis")
        .call(d3.axisBottom(scaleX));

    // add y axis
    graph.append("g")
        .attr("class", "y-axis")
        .call(d3.axisLeft(scaleY));
}

function updateGraph(data){
    // reference
    // https://bl.ocks.org/d3noob/7030f35b72de721622b8

    setScaling(data, scaleX, scaleY);
    const graph = d3.select("#container svg g").transition();
    const duration = 1000 / updatesPerSecond;
    graph.select("path")
        .duration(duration)
        .attr("d", line(data));
    graph.select(".x-axis")
        .duration(duration)
        .call(d3.axisBottom(scaleX));
    graph.select(".y-axis")
        .duration(duration)
        .call(d3.axisLeft(scaleY));
}

function setScaling(data, scaleX, scaleY){
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
}

let partitionAmount;
let currentIndex = 0;
fetch("/data")
    .then((response) => response.json())
    .then((entries) => {
        // Example date entry: "1967-01-07"
        const parseDate = d3.timeParse("%Y-%m-%d");

        // Need to convert the date entry into something d3 can read
        for(const entry of entries){
            entry.date = parseDate(entry.date);
        }
        // update global variable
        data = entries;

        partitionAmount = Math.floor(data.length / (animationDuration * updatesPerSecond));
        drawGraph(data.slice(currentIndex, partitionAmount));
        currentIndex += partitionAmount;
    })
    .catch((e) => {
        alert("Failed to get data from the server. See console for more information");
        console.log(e)
    });

d3.select("#start")
    .on("click", () => {
        setInterval(() => {
            // Need to use Math.min to check bounds
            updateGraph(data.slice(0, Math.min(data.length - 1, currentIndex + partitionAmount)));
            currentIndex += partitionAmount;

            // end this interval once we got all data to screen
            if(currentIndex >= data.length - 1) return;
        }, animationDuration / 1000 * updatesPerSecond + 1000 / updatesPerSecond);
    });