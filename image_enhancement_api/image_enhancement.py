from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import io
app=FastAPI()
def enhance_image(image:np.ndarray,sharpness:float=1.0,color:float=1.0,noise_reduction:bool=False)->np.ndarray:
    if sharpness != 1.0:
        kernel = np.array([[0, -1, 0],
                           [-1, 5 * sharpness, -1],
                           [0, -1, 0]])
        image = cv2.filter2D(image,-1,kernel)
    if color != 1.0:
        hsv_image = cv2.cvtColor(image,cv2.COLOR_RGB2HLS)
        hsv_image[...,1]=cv2.multiply(hsv_image[...,1],color)
        image = cv2.cvtColor(hsv_image,cv2.COLOR_RGB2HLS)
    if noise_reduction:
        image = cv2.GaussianBlur(image,(3,3),0)
    return image

@app.post("/enhance-image/")
async def enhance_image_api(file:UploadFile = File(...),sharpness:float=1.0,color:float=1.0,noise_reduction:bool=False):
    try:
        # Load image
        image_data = await file.read()
        image_array = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        # Enhance image
        enhanced_image = enhance_image(image, sharpness, color, noise_reduction)
        # Encode the enhanced image back to bytes
        _, img_encoded = cv2.imencode('.jpg', enhanced_image)
        img_byte_arr = img_encoded.tobytes()
        return JSONResponse(content={"message": "Image enhanced successfully.", "filename": file.filename})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)