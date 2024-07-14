const map = L.map("map");

// Basemaps
const baseLayers = {
  OpenStreetMap: L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }
  ),
  CycleOSM: L.tileLayer(
    "https://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png?apikey=YOUR_API_KEY",
    {
      attribution:
        '&copy; <a href="https://www.thunderforest.com/maps/cycle/">Thunderforest</a> contributors',
    }
  ),
  "CartoDB Positron": L.tileLayer(
    "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: "abcd",
    }
  ),
  "Esri Satellite": L.tileLayer(
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    {
      attribution:
        "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
    }
  ),
};

// Add initial basemap
baseLayers["CartoDB Positron"].addTo(map);

// Styles for layers
function getStyle(model) {
  const styles = {
    ns: function (feature) {
      const client = feature.properties.client_gov;
      return {
        color:
          client === "Maxis"
            ? "red"
            : client === "Telekom"
            ? "blue"
            : "#E90074",
        weight: client === "Maxis" ? 3 : 2,
        opacity: 0.9,
        dashArray: client === "Maxis" ? "10, 5" : "5, 5",
      };
    },
    wp: { color: "green", weight: 2, opacity: 0.9, dashArray: "5, 5" },
    pl: { color: "#F4CE14", weight: 2, opacity: 0.9, dashArray: "5, 5" },
    rd: { color: "lightgray", weight: 1, opacity: 0.9 },
    row: { color: "#FFA500", weight: 2, opacity: 0.9, dashArray: "5, 5" },
  };
  return styles[model] || {};
}

// Style function for manhole data
function manholeStyle(feature) {
  if (feature.properties.MANHOLE === "value") {
    return {
      color: "black",
      weight: 2,
      opacity: 1,
      fillOpacity: 0,
    };
  } else {
    return {
      color: "red",
      weight: 2,
      opacity: 1,
      fillOpacity: 0.8,
    };
  }
}

// Popup for layers
function onEachFeature(feature, layer, layerName) {
  const popupContent = `
    <b>${layerName}</b>
    <br>Client: ${feature.properties.client_gov}
    <br>Elevation: ${feature.properties.elevation}m
    <br>Doc Update: ${feature.properties.docupdate}
  `;
  layer.bindPopup(popupContent);

  // Zoom to feature on click
  layer.on("click", function () {
    map.fitBounds(layer.getBounds());
  });
}

// Popup for manhole layer
function onEachManholeFeature(feature, layer) {
  const popupContent = `
    <b>Manhole</b>
    <br>Type: ${feature.properties.MANHOLE}
  `;
  layer.bindPopup(popupContent);

  // Zoom to feature on click
  layer.on("click", function () {
    map.fitBounds(layer.getBounds());
  });
}

// Load and render layers
async function load_data(modelName) {
  const url = `/api/${modelName}/`;
  const response = await fetch(url);
  const data = await response.json();
  return data;
}

async function render_layers() {
  const models = ["ns", "wp", "pl", "rd", "row", "mh"];
  const layerNames = {
    ns: "Network Service",
    wp: "Water Pipeline",
    pl: "Powerline",
    rd: "Road",
    row: "Right of Way",
    mh: "Manholes",
  };

  let layers = [];

  for (const model of models) {
    const data = await load_data(model);
    const layerName = layerNames[model];
    const layer = L.geoJSON(data, {
      style: model === "mh" ? manholeStyle : getStyle(model),
      onEachFeature:
        model === "mh"
          ? onEachManholeFeature
          : (feature, layer) => onEachFeature(feature, layer, layerName),
    }).addTo(map);
    layers.push(layer);
  }

  // Fit map to bounds
  const group = new L.featureGroup(layers);
  map.fitBounds(group.getBounds());

  // Add layers control
  const overlays = {
    "Network Service": layers[0],
    "Water Pipeline": layers[1],
    Powerline: layers[2],
    Road: layers[3],
    "Right of Way": layers[4],
    Manholes: layers[5],
  };

  L.control.layers(baseLayers, overlays, { collapsed: true }).addTo(map);

  // Add Home Button Control to reset viewport to data layers
  const homeButton = L.Control.extend({
    options: { position: "topleft" },
    onAdd: function () {
      const container = L.DomUtil.create(
        "div",
        "leaflet-bar leaflet-control leaflet-control-custom"
      );
      container.style.backgroundColor = "white";
      container.style.width = "30px";
      container.style.height = "30px";
      container.innerHTML = '<i class="fas fa-home fa-lg"></i>';
      container.style.display = "flex";
      container.style.justifyContent = "center";
      container.style.alignItems = "center";
      container.style.cursor = "pointer";
      container.onclick = function () {
        map.fitBounds(group.getBounds());
      };
      return container;
    },
  });
  map.addControl(new homeButton());

  // Add Locate Control plugin
  L.control
    .locate({
      position: "topleft",
      flyTo: true,
      locateOptions: {
        maxZoom: 16,
      },
    })
    .addTo(map);

  // Add Scale Control
  L.control.scale().addTo(map);

  // Add Print Control
  L.easyPrint({
    title: "Print map",
    position: "topleft",
    elementsToHide: "legend",
    sizeModes: ["A4Portrait", "A4Landscape"],
  }).addTo(map);
}

// Initialize the map and render layers
render_layers();
