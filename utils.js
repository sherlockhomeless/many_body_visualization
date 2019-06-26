function create_canvas() {
    var canvas = d3.select("#graph")
        .append("svg")
        .attr("width", "100%")
        .attr("height", "100%")
        .append("g");
    return canvas;
}