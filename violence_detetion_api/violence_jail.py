from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
from PIL import Image
import io
from transformers import pipeline

app=FastAPI()
yolo_model = YOLO('pth')
def load_image(image_data):
    return Image.open(io.BytesIO(image_data))

@app.post("/detect-plant")
async def detect_plant(file: UploadFile=File(...)):
    image_data=await file.read()
    image = load_image(image_data)
    results= yolo_model.predict(image)
    detected_nature=[]
    for prediction in results:
        nature_class= prediction['class_name']
        if nature_class=='violence':
            return JSONRespnse(content={'trigger':nature_class})
        detected_nature.append(plant_class)
    return JSONResponse(content={"detected_plants": detected_nature})
