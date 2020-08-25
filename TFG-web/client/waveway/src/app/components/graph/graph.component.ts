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
		let predictionPoints = [];
		let dpsLength = 0;
		let xvalue = 0;
		let chart = new CanvasJS.Chart("chartContainer",{
			exportEnabled: true,
			title:{
				text:"Predición da apertura do aparello"
			},
			data: [{
				type: "spline",
				dataPoints : dataPoints,
			},
			{
				type: "spline",
				dataPoints : predictionPoints,
			}]
		});
		
		updateChart()


		function updateChart() {

		$.getJSON("http://localhost:8080/retrieveData?limit=50", function(data) {
			$.each(data, function(key, value) {
				dataPoints.push({
				x: xvalue++,
				y: parseInt(value[1])
				});
				dpsLength++;
			});
			if (dataPoints.length > 21){
				dataPoints.splice(0, dataPoints.length - 50)
			}

		});

		$.getJSON("http://localhost:8080/towdata", function(data) {
			$.each(data, function(key, value) {
				predictionPoints.push({
				x: parseInt(value[0]) + xvalue - 1,
				y: parseInt(value[1]),
				lineColor: "red",
				color: "red"
				});
				dpsLength+=parseInt(value[0]);
			});
			if (predictionPoints.length > 8){
				predictionPoints.splice(0, predictionPoints.length - 8)
			}
			chart.render();
			setTimeout(function(){updateChart()}, 5000);

		});

		}
	}
}
