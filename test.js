document.addEventListener('DOMContentLoaded', function() {
    var url = document.getElementById('share');
    var num = document.getElementById('phone-number');
    var carrier = document.getElementById('carrier');

    var btn = document.getElementById('add');
    btn.addEventListener('click', function() {
        var send = require('./connector.js');
        send(num.value, carrier.value, url.value);
        console.log("Sent");
        
    });
});

