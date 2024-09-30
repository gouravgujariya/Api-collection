from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import cv2
import os
from deepface import DeepFace

app = FastAPI()

# Path to your face database
DB_PATH = "C:\\Users\\ergou\\PycharmProjects\\pythonProject\\live_attendance\\celeb_db\\Celebrity Faces Dataset-20240917T055200Z-001\\Celebrity Faces Dataset\\DB_celeb"

# HTML for displaying the stream on the front-end
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Face Recognition Stream</title>
    </head>
    <body>
        <h1>Live Face Recognition Stream</h1>
        <video id="video" width="640" height="480" autoplay></video>
        <script>
            const video = document.getElementById('video');

            navigator.mediaDevices.getUserMedia({ video: true })
                .then(stream => {
                    video.srcObject = stream;
                    const ws = new WebSocket('ws://localhost:8000/ws');

                    const mediaRecorder = new MediaRecorder(stream);
                    mediaRecorder.ondataavailable = function(event) {
                        if (event.data.size > 0) {
                            ws.send(event.data);
                        }
                    };

                    mediaRecorder.start(1000);  // Send video frames every second
                });
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # Load the DeepFace.stream for face recognition
    try:
        DeepFace.stream(
            db_path=DB_PATH,
            model_name="Facenet512",  # You can use other models like VGG-Face, ArcFace, etc.
            detector_backend="retinaface",
            distance_metric="euclidean_l2",
            enforce_detection=True,
            source=0,  # Use webcam or replace with the uploaded video stream
            anti_spoofing=True
        )
    except WebSocketDisconnect:
        print("WebSocket disconnected.")
    except Exception as e:
        await websocket.send_text(f"Error: {str(e)}")
        await websocket.close()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
