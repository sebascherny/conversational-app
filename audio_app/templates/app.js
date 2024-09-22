const recordBtn = document.getElementById("recordBtn");
const statusText = document.getElementById("status");
const responseAudio = document.getElementById("responseAudio");

let mediaRecorder;
let audioChunks = [];

recordBtn.addEventListener("click", () => {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
        recordBtn.textContent = "Record Audio";
    } else {
        startRecording();
    }
});

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();

        recordBtn.textContent = "Stop Recording";
        statusText.textContent = "Recording...";

        audioChunks = [];

        mediaRecorder.addEventListener("dataavailable", (event) => {
            audioChunks.push(event.data);
        });

        mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(audioChunks);
            sendAudio(audioBlob);
        });
    });
}

function sendAudio(audioBlob) {
    let base_url = "wss://localhost:8000/";
    if (PROD_URL != null) {
        base_url = PROD_URL;
    }
    const url = base_url + "ws/audio/";
    const socket = new WebSocket(url);
    
    socket.onopen = function () {
        statusText.textContent = "Sending audio...";
        socket.send(audioBlob);
    };

    socket.onmessage = function (event) {
        const audioUrl = URL.createObjectURL(new Blob([event.data]));
        responseAudio.src = audioUrl;
        responseAudio.play();
        statusText.textContent = "Response received!";
    };

    socket.onclose = function () {
        console.log("Connection closed.");
    };

    socket.onerror = function (error) {
        console.error("WebSocket error:", error);
    };
}
