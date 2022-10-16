var map;
var heatmapData = [
new google.maps.LatLng(37.782, -122.447),
new google.maps.LatLng(36.778261, -119.417932),
new google.maps.LatLng(-37.814107, 144.96328),
new google.maps.LatLng(33.867487, 151.20699),
{ location: new google.maps.LatLng(40.416775, -3.70379), weight: 6 },
{ location: new google.maps.LatLng(41.385064, 2.173403), weight: 2 },
{ location: new google.maps.LatLng(52.130661, -3.783712), weight: 2 },
{ location: new google.maps.LatLng(55.378051, -3.435973), weight: 8 },
{ location: new google.maps.LatLng(-40.900557, 174.885971), weight: 6 },
{ location: new google.maps.LatLng(40.714353, -74.005973), weight: 6 }
];
function initializeMap() {
var myMapOptions = {
zoom: 4.3,
center: new google.maps.LatLng(39.828175, -98.5795),
mapTypeId: google.maps.MapTypeId.ROADMAP
};
map = new google.maps.Map(document.getElementById('map'),myMapOptions);
var heatmap = new google.maps.visualization.HeatmapLayer({
data: heatmapData,
dissipating: true,
map: map
});
}
google.maps.event.addDomListener(window, 'load', initializeMap);

