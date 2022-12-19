// scripts.js
var graphviz = d3.select("#graph").graphviz().on("initEnd", render);

function render() {
    var dot = dots[0].join('');
    // scale graph to fit in the window
    const width = window.innerWidth / 1.5 - 22;
    const height = window.innerHeight / 1.5;
    graphviz
        .width(width)
        .height(height)
        .fit(true)
        .renderDot(dot)
}
var result = document.getElementById("resultGraph").textContent;
var dots = [
    [
        result,
    ]
];
