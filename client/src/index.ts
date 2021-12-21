import { Stomp, messageCallbackType } from '@stomp/stompjs/esm6';

console.log("script starting")
const onError =  function() {
    console.log('error');
};

const onMessage: messageCallbackType = function(m) {
    console.log('Received message', m.body)
    const doc = document.getElementById("root")
    if (doc) {
        doc.innerHTML += m.body + '<br />'
    }
}

const onConnect = function() {
    console.log('connected');
    client.subscribe('/topic/websocket', onMessage)
};

const onClose = function() {
    console.log('closed');
}

const client = Stomp.client('ws://127.0.0.1:15674/ws');
client.reconnectDelay = 1000;
client.connect('user', 'password', onConnect, onError, onClose, '/');
