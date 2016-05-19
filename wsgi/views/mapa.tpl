<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <title>Mapa</title>
    <link rel="icon" type="image/png" href="/static/findit-ico.png">
    <link rel="stylesheet" href="/static/style.css">
  <style>
      html, body, #map-canvas {
       height: 90%;
       margin: 0px;
       padding: 0px;
      }
    </style>
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Mapa</title>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true"></script>
    <script>
function initialize() {
var ubicaciones = {{ubicaciones}};

var myLatlng = new google.maps.LatLng(ubicaciones[0][0],ubicaciones[0][1]);
  var mapOptions = {
    zoom: 6,
    center: myLatlng
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
var marker, i;
var infowindow = new google.maps.InfoWindow();
    for (i = 0; i < ubicaciones.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(ubicaciones[i][0], ubicaciones[i][1]),
        map: map
		    });
	
		    
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(tuit[i]);
          infowindow.open(map, marker);
        }
      })(marker, i));
}
}
google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    	<header>
        <a href="/">
          <h1>Volver una buscar foto</h1>
        </a>

      </header>
	<div id="map-canvas">
	</div>
	<script src="js/jquery.js"></script>
	<script src="js/library.js"></script>
	<script src="js/script.js"></script>
	<script src="js/retina.js"></script>
  </body>
</html>
