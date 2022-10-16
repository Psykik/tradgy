let map;

  function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 39.828175, lng:  -98.5795 },
      zoom: 4.8,
    });
  }

  window.initMap = initMap;

