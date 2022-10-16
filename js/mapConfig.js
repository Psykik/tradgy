let map;

  function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 41.6611, lng: -91.5302 },
      zoom: 8,
    });
  }

  window.initMap = initMap;

