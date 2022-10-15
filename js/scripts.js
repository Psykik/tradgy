/*!
* Start Bootstrap - The Big Picture v5.0.5 (https://startbootstrap.com/template/the-big-picture)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-the-big-picture/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

var heatmapInstance = h337.create({
    container: document.getElementById('heatMap')
  });

  var testData = {
        min: 0,
        max: 100,
        data: [{x: 807, y: 583, value: 65}, {x: 597, y: 285, value: 51}, {x: 217, y: 449, value: 73}, {x: 377, y: 656, value: 58}, {x: 467, y: 509, value: 47}, {x: 487, y: 164, value: 46}, {x: 247, y: 194, value: 35}]
  };
  heatmapInstance.setData(testData);