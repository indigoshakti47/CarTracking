console.log("Running")

const INITIAL_POS = 106;
const NOTIFY_POS = 250;



let latLang = {lat: -34.397, lng: 150.644}

const socket = io();
socket.on('connect', function() {
    socket.emit('message', {data: 'I\'m connected!'});
});

function initMap() {
    const origin = {
        lat: 4.6983613,
        lng: -74.0503179
    };

    const destination = {
        lat: 4.6959902,
        lng: -74.0435466,
    };

    const map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: origin.lat, lng: origin.lng},
        zoom: 16
    });

    let marker = new google.maps.Marker({
        position: origin,
        map: map,
        title: 'Truck',
        icon: '/static/icons8-truck-64.png'
    });

    let circle = new google.maps.Circle({
        strokeColor: '#FF0000',
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#FF0000',
        fillOpacity: 0.35,
        map: map,
        center: destination,
        radius: 200
    });

    let currentLat = origin.lat;
    let currentLng = origin.lng;

    setInterval(() => {
        if (currentLat > destination.lat) {
            currentLat -= 0.00004;
            currentLng += 0.0001;
            marker.setPosition(new google.maps.LatLng(currentLat, currentLng))
        }
    }, 1000)


    socket.on('position_update', payload => {
        console.log("Hola")
        console.log(payload.data)

    })
}