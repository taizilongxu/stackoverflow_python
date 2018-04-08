export function c3 (id, body) {
    // bind to element
    body.bindto = '#' + id;
    return `c3.generate(${JSON.stringify(body)});`;
};

export function highcharts (id, body) {
    // http://www.highcharts.com/docs/getting-started/your-first-chart
    body.chart = body.chart || {};
    body.chart.renderTo = id;
    return `new Highcharts.Chart(${JSON.stringify(body)});`;
};
