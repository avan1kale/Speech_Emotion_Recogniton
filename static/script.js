const recordBtn = document.getElementById("recordBtn");
const status = document.getElementById("status");
const emotion = document.getElementById("emotion");
const confidence = document.getElementById("confidence");

let mediaRecorder;
let audioChunks = [];
let isRecording = false;

recordBtn.addEventListener("click", async () => {

    // START RECORDING
    if (!isRecording) {

        try {

            const stream = await navigator.mediaDevices.getUserMedia({
                audio: true
            });

            mediaRecorder = new MediaRecorder(stream);

            audioChunks = [];

            mediaRecorder.ondataavailable = (event) => {
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = () => {

                const audioBlob = new Blob(audioChunks, {
                    type: "audio/webm"
                });

                const formData = new FormData();

                formData.append(
                    "audio",
                    audioBlob,
                    "recording.webm"
                );

                status.innerHTML = "⏳ Processing...";

                console.log("Sending request to /record...");

                fetch("/record", {
                    method: "POST",
                    body: formData
                })
                .then(response => {
                     console.log("Status:", response.status);
                    return response.json();
                })
                .then(data => {

                    console.log(data);
                    console.log("emotion element:", emotion);
                    console.log("confidence element:", confidence);
                    console.log("status element:", status);
                    console.log("recordBtn element:", recordBtn);

                    emotion.innerHTML = data.emotion;
                    confidence.innerHTML = data.confidence + "%";

                    status.innerHTML = "✅ Prediction Complete";

                    recordBtn.innerHTML = "🎙️ Start Recording";

                    isRecording = false;
                })
                .catch(error => {
                    console.log(error);

                    status.innerHTML = "❌ Error";

                    recordBtn.innerHTML = "🎙️ Start Recording";

                    isRecording = false;
                });

            };

            mediaRecorder.start();

            isRecording = true;

            recordBtn.innerHTML = "⏹️ Stop Recording";

            status.innerHTML = "🎙️ Recording...";

        }

        catch (error) {

            status.innerHTML = "❌ Microphone access denied.";

            console.log(error);

        }

    }

    // STOP RECORDING
    else {

        mediaRecorder.stop();

        status.innerHTML = "⏹️ Recording stopped.";

    }

});