from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
from PIL import Image
import io
from transformers import pipeline

app=FastAPI()
yolo_model = YOLO('pth')
care_pipe= pipeline('text-generation',model='microsoft/phi-3-mini-4k-instruct',trust_remote_code=True)

def load_image(image_data):
    return Image.open(io.BytesIO(image_data))

@app.post("/detect-plant")
async def detect_plant(file: UploadFile=File(...)):
    image_data=await file.read()
    image = load_image(image_data)
    results= yolo_model.predict(image)
    detected_plant=[]
    for prediction in results:
        plant_class= prediction['class_name']
        detected_plant.append(plant_class)
    care_info={}
    for plant in detected_plant:
        care_message=[{"role":"user","content":f"tell me about the care information for {plant}."}]
        care_response = care_pipe(care_message)
        care_info[plant] = care_response[0]["generated_text"]
    return {'detected_plants':detected_plant,'care_info':care_info}
