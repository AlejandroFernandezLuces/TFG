/*app.component.ts*/
import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';
import * as CanvasJS from './canvasjs.min';
//var CanvasJS = require('./canvasjs.min');
 
@Component({
	selector: 'app-graph',
	templateUrl: './graph.component.html'
})
 
export class GraphComponent implements OnInit {
	ngOnInit() {
	let dataPoints = [];
	let dpsLength = 0;
	let chart = new CanvasJS.Chart("chartContainer",{
		exportEnabled: true,
		title:{
			text:"Datos en vivo"
		},
		data: [{
			type: "spline",
			dataPoints : dataPoints,
		}]
	});
	
	$.getJSON("http://localhost:8080/towdata", function(data) {  
		$.each(data, function(key, value){
			dataPoints.push({x: value[0], y: parseInt(value[1])});
		});
		dpsLength = dataPoints.length;
		chart.render();
		updateChart(); 
	});
	function updateChart() {	
		$.getJSON("", function(data) {
		$.each(data, function(key, value) {
			dataPoints.push({
			x: parseInt(value[0]),
			y: parseInt(value[1])
			});
			dpsLength++;
		});
		
		if (dataPoints.length >  20 ) {
      		dataPoints.shift();				
      	}
		chart.render();
		setTimeout(function(){updateChart()}, 1000);
	});
    }
}
}