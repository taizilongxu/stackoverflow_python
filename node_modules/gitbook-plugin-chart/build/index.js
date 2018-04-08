'use strict';

var _uuidCounter = 0;
function uuid() {
    return "plugin-chart-" + ++_uuidCounter;
};

function c3(id, body) {
    // bind to element
    body.bindto = '#' + id;
    return 'c3.generate(' + JSON.stringify(body) + ');';
};

function highcharts(id, body) {
    // http://www.highcharts.com/docs/getting-started/your-first-chart
    body.chart = body.chart || {};
    body.chart.renderTo = id;
    return 'new Highcharts.Chart(' + JSON.stringify(body) + ');';
};

var chartFns = Object.freeze({
    c3: c3,
    highcharts: highcharts
});

var FORMAT_YAML = 'yaml';

var chartScriptFn = function chartScriptFn() {};

module.exports = {
    book: {
        assets: './assets'
    },
    hooks: {
        init: function init() {
            var pluginConfig = this.config.get('pluginsConfig.chart');
            var type = pluginConfig.type;
            chartScriptFn = chartFns[type];
        }
    },
    blocks: {
        chart: {
            process: function process(blk) {
                var id = uuid();
                var body = {};
                try {
                    // get string in {% chart %}
                    var bodyString = blk.body.trim();
                    if (blk.kwargs.format === FORMAT_YAML) {
                        // load yaml into body:
                        body = require('js-yaml').safeLoad(bodyString);
                    } else {
                        // this is pure JSON
                        body = JSON.parse(bodyString);
                    }
                } catch (e) {
                    console.error(e);
                }
                var scripts = chartScriptFn(id, body);
                return '<div>\n                    <div id="' + id + '"></div>\n                    <script>' + scripts + '</script>\n                </div>';
            }
        }
    }
};