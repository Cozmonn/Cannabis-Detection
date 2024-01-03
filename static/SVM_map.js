window.onload = init;
function init(){      
  var map = new ol.Map({
  target: 'map',
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    })
  ],
  view: new ol.View({
    center: ol.proj.fromLonLat([-5.01034, 35.0999992]),
    zoom: 12
  })
});

var stamenTerrain = new ol.layer.Tile({
  title: 'Layers',
  source: new ol.source.XYZ({
    url:'https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
    attributions:'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
  }),
  visible:false,
});
var Satellite = new ol.layer.Tile({
  title: 'Layers',
  visible:false,
  source: new ol.source.XYZ({
  attributions: ['Powered by Esri',
             'Source: Esri, DigitalGlobe, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community'],
  attributionsCollapsible: true,
  url: 'https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
  maxZoom: 23
})
  
});
var untiled = new ol.layer.Tile({
  title: 'cannabis',
  visible:false,
  source: new ol.source.TileWMS({
    url: 'http://localhost:8080/geoserver/SVM_algorihtm/wms',
    params: {'LAYERS': 'SVM_algorihtm:cannabirass',
    serverType:'geoserver',
    transition: 3
    }
  }),
  zIndex:100
});

var untiledforestpoly = new ol.layer.Tile({
  title: 'Forest',
  visible:false,
  source: new ol.source.TileWMS({
    url: 'http://localhost:8080/geoserver/SVM_algorihtm/wms',
    params: {'LAYERS': 'SVM_algorihtm:forest'},
    serverType:'geoserver',
    transition: 3
  }),
  zIndex:100
});

var SurfaceSollocation = new ol.layer.Tile({
  title: 'Surface Sol',
  visible:false,
  source: new ol.source.TileWMS({
  url: 'http://localhost:8080/geoserver/SVM_algorihtm/wms',
  params:{'LAYERS':'SVM_algorihtm:surfacesol'},
  serverType:'geoserver',
  transition: 3
  }),
  zIndex:100
});


untiled.setOpacity(0.5);
SurfaceSollocation.setOpacity(0.7);

const baseLayerGroup = new ol.layer.Group({
  title: 'Layers',
  layers:[
  stamenTerrain, Satellite
  ]
})

const Feature = new ol.layer.Group({
  title: 'Component',
  layers:[
    untiled, SurfaceSollocation, untiledforestpoly
  ]
})
map.addLayer(Feature);

Satellite.set('title', 'Satellite');
stamenTerrain.set('title', 'stamenTerrain');

map.addLayer(baseLayerGroup);
var layerSwitcher = new ol.control.LayerSwitcher({
    activationMode: 'click',
    startActive: false,
    groupSelectStyle: 'children'
});

map.addControl(layerSwitcher);
layerSwitcher.on('show', (evt) => {
  console.log('show', evt);
});

//Scale-Echèlle
var scalecontrol = new ol.control.ScaleLine({});
map.addControl(scalecontrol);
//Mouse Mapping
var MouseMapping = new ol.control.MousePosition({
  className: 'MouseMapping',
  projection:'EPSG:4326',
  coordinateFormat: function (coordinate) {return ol.coordinate.format(coordinate, '{y}, {x}', 6);}
});

map.addControl(MouseMapping);    

}