const recordBtn = document.getElementById("recordBtn");
const stopBtn = document.getElementById("stopBtn");
const status = document.getElementById("status");

let mediaRecorder;

let audioChunks = [];

recordBtn.addEventListener("click", async () => {

    try {

        const stream = await navigator.mediaDevices.getUserMedia({
            audio: true
        });

        status.innerHTML = "🎙️ Recording...";

        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = (event) => {
            console.log(event.data);
            audioChunks.push(event.data);
        };

        mediaRecorder.start();

        console.log("Recorder created!");
        console.log("State:", mediaRecorder.state);

        status.innerHTML = "🎙️ Recording...";

    }

    catch(error) {

        status.innerHTML = "❌ Microphone access denied.";

        console.log(error);

    }

});
stopBtn.addEventListener("click", () => {

    mediaRecorder.stop();

    status.innerHTML = "⏹️ Recording stopped.";

    mediaRecorder.onstop = () => {

        const audioBlob = new Blob(audioChunks, {
            type: "audio/webm"
        });

        const formData = new FormData();

        formData.append("audio",audioBlob,"recording.webm");

        fetch("/record", {method: "POST",body: formData})
        .then(response => response.text())
        .then(data => {
        console.log(data);

    });
    }

});