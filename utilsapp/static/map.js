const map = L.map("map"); // Initial map setup without center and zoom to fit bounds later

// Basemaps
const baseLayers = {
  OpenStreetMap: L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }
  ),
  OpenTopoMap: L.tileLayer("https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png", {
    attribution:
      'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
  }),
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
      const colors = {
        Maxis: "#C80036",
        Telekom: "#2B3467",
        Times: "#FF4191",
      };
      return {
        color: colors[client],
        weight: 0.75,
        opacity: 0.9,
      };
    },
    wp: {
      color: "#1679AB",
      weight: 2,
      opacity: 0.9,
      dashArray: "5 2.5",
    },
    pl: {
      color: "#0A6847",
      weight: 1,
      opacity: 0.9,
      // Custom powerline style
    },
    rd: {
      color: "#686D76",
      weight: 2,
      opacity: 0.9,
    },
    row: {
      color: "#000000",
      weight: 1.5,
      opacity: 2.5,
      dashArray: "1 5",
    },
    mh: function (feature) {
      return {
        color:
          feature.properties.layer !== "prop TTDC MH" ? "red" : "transparent",
        weight: 2,
        opacity: 0.9,
      };
    },
  };
  return styles[model] || {};
}

// Popup for layers
function onEachFeature(feature, layer, layerName) {
  const popupContent = `
    <b>${layerName}</b>
    <br>Client: ${feature.properties.client_gov || "N/A"}
    <br>Elevation: ${feature.properties.elevation || "N/A"}m
    <br>Doc Update: ${feature.properties.docupdate || "N/A"}
  `;
  layer.bindPopup(popupContent);

  // Zoom to feature on click
  layer.on("click", function () {
    map.fitBounds(layer.getBounds(), { maxZoom: 18 }); // Increase maxZoom to 18
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
    mh: "Manhole",
  };

  let layers = [];
  let specificLayers = [];

  for (const model of models) {
    const data = await load_data(model);
    const layerName = layerNames[model];
    const layer = L.geoJSON(data, {
      style: getStyle(model),
      onEachFeature: (feature, layer) =>
        onEachFeature(feature, layer, layerName),
    }).addTo(map);
    layers.push(layer);

    // Add specific layers (excluding `pl` as an example)
    if (model !== "pl") {
      specificLayers.push(layer);
    }
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
    Manhole: layers[5],
  };

  L.control.layers(baseLayers, overlays, { collapsed: true }).addTo(map);

  // Add Home Button Control to reset viewport to specific layers
  const homeButton = L.Control.extend({
    options: { position: "topleft" },
    onAdd: function () {
      const container = L.DomUtil.create(
        "div",
        "leaflet-bar leaflet-control leaflet-control-custom"
      );
      container.innerHTML = '<i class="fas fa-home fa-lg"></i>';
      container.onclick = function () {
        const specificGroup = new L.featureGroup(specificLayers);
        map.fitBounds(specificGroup.getBounds());
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
    position: "left",
    exportOnly: true,
    sizeModes: ["A4Portrait", "A4Landscape"],
  }).addPrintButton("leaflet-control-easyPrint");
}

// Initialize the map with layers
render_layers();
