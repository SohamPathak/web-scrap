/*
 * Parse the data and create a graph with the data.
 */
function parseData(createGraph) {
	Papa.parse("../static/data/spanish-silver.csv", {
		download: true,
		complete: function(results) {
			createGraph(results.data);
		}
	});
}

function createGraph(data) {
	var years = [];
	var silverMinted = [];

	for (var i = 1; i < data.length-1; i++) {
		if (data[i][0] !== undefined && data[i][0] !== null) {
		years.push(data[i][1]);
		silverMinted.push(data[i][2]);
	}
	 else {
	 	years.push(0);
		silverMinted.push(0);
	 }
	}

	console.log(years);
	console.log(silverMinted);

	var chart = c3.generate({
		bindto: '#chart',
	    data: {
	        columns: [
	        	silverMinted
	        ]
	    },
	    axis: {
	        x: {
	            type: 'category',
	            categories: years,
	            tick: {
	            	multiline: false,
                	culling: {
                    	max: 15
                	}
            	}
	        }
	    },
	    zoom: {
        	enabled: true
    	},
	    legend: {
	        position: 'right'
	    }
	});
}

parseData(createGraph);