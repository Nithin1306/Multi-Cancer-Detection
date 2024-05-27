from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL =  tf.keras.models.load_modelLung = tf.keras.models.load_model("C:/Users/Nithin/Desktop/Multi-Organ-Detetction/Backend/Models/Lung")

CLASS_NAMES = ["Ardenocarcinoma","Large cell carcinoma" ,"Normal", "Squamous Cell Carcinoma"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    # Open image using PIL
    with Image.open(BytesIO(data)) as img:
        # Rescale the image to 256x256 while preserving aspect ratio
        img.thumbnail((256, 256))

        # Convert the image to numpy array and normalize its values to [0, 1]
        image = np.array(img) / 255.0

    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())

    if image.shape[2] == 4:
        image = image[:, :, :3]
    
    # Resize the image to 256x256
    image = tf.image.resize(image, (256, 256))
    
    # Expand dimensions to create a batch of size 1
    img_batch = tf.expand_dims(image, 0)
    
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)