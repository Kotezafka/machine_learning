const vegaEmbed = require('vega-embed');

vegaEmbed('#view', './my_dashboard.json')
.then(result => console.log(result))
.catch(error => console.error(error));
