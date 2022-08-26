// let index = 0;

// function getData() {
//   console.log("tock");
//   fetch(`/api/${index}`)
//   .then(function (response) {
//         return response.json();
//     }).then(function (text) {
//         console.log('GET response text:');
//         console.log(text); 
//     });
// }

// setInterval(getData, 10000)

mapboxgl.accessToken = 'pk.eyJ1IjoicnViaWM0IiwiYSI6ImNrY3Vla3R1ZjF0YnYyeXQ2c243eWVpeHEifQ.Hgj0BjhuuOAowR_pE97V_Q';

const geojson = {
  'type': 'FeatureCollection',
  'features': [
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.22263, 45.75634]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Piata 700'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.217045, 45.75659]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Circumvalatiunii'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.213752, 45.756908]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Mendeleev'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.209051, 45.756685]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Hasdeu'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.204381, 45.757615]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Uta'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.201038, 45.757519]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Lapusneanu'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.194473, 45.756774]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Alexandrescu (Amzei)'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.192474, 45.755755]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Madona'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.189942, 45.752242]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Taborului'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.189805, 45.751220]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Razboieni'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.186133, 45.751489]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Ciresului'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.183034, 45.751631]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Rosetti'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.185915, 45.755011]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Banul Severinului'
      }
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.185373, 45.757132]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Grigore Ureche'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.184859, 45.759839]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Rarau'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.187380, 45.760307]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Ciocarliei'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.187722, 45.755000]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'I.M.L.'
      } 
    },
    //back route
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.188161, 45.755236]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'I.M.L.'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.185757, 45.750389]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Ciresului'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.189806, 45.751028]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Razboieni'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.190033, 45.752377]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Taborului'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.192081, 45.755409]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Madona'
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.194484, 45.756739]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Alexandrescu (Amzei)'
      } 
    }, 
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.200646, 45.757521]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Lapusneanu' 
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.204240, 45.757542]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Uta'
      } 
    }, 
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.209352, 45.756600]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Hasdeu' 
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.213553, 45.756918]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Bogdanestilor' 
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.216711, 45.756569]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Circumvalatiunii' 
      } 
    },
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [21.223106, 45.756241]
      },
      'properties': {
        'title': 'Mapbox',
        'description': 'Piata 700' 
      } 
    }
  ]
};

const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/light-v10',
  center: [21.22263, 45.75634],
  zoom: 15
});

function updateMap() {
  
  const boxes = document.querySelectorAll('.marker');

  boxes.forEach(box => {
    box.remove();
  });
  
  // add markers to map
  let index = 0;
  fetch('/api')
  .then(function (response) {
        return response.json();
  }).then(function (text) {
      // console.log('GET response text:');
      //console.log(text);

      for (const feature of geojson.features) {
        // create a HTML element for each feature
        const el = document.createElement('div');
        
        el.textContent = `${text[index][1]}: ${text[index][0]} min.`;
        if(index > 16) {
          el.className = 'markerBack';
        }
        else {
          el.className = 'marker';
        }
        index++;
        // make a marker for each feature and add it to the map
        new mapboxgl.Marker(el)
          .setLngLat(feature.geometry.coordinates)
          .setPopup(
            new mapboxgl.Popup({ offset: 25 }) // add popups
              .setHTML(
                `<h3>${feature.properties.title}</h3><p>${feature.properties.description}</p>`
              )
          )
          .addTo(map);
      }
    
  });
  
}
updateMap();
setInterval(updateMap, 60000)

    
