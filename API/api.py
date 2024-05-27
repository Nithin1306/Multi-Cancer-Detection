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

Lung = tf.keras.models.load_model(r"C:\Users\Nithin\Desktop\Model.h5")
Brain = tf.keras.models.load_model("C:/Users/Nithin/Desktop/Multi-Organ-Detetction/Backend/Models/Brain")
Kidney = tf.keras.models.load_model("C:/Users/Nithin/Desktop/Multi-Organ-Detetction/Backend/Models/Kidney")
Breast = tf.keras.models.load_model("C:/Users/Nithin/Desktop/Multi-Organ-Detetction/Backend/Models/Breast/Breast_Cancer.h5")


LUNG_CLASS_NAMES = ["Adenocarcinoma","Large cell carcinoma" ,"Normal", "Squamous Cell Carcinoma"]
BRAIN_CLASS_NAMES = ["Glioma", "Meningioma", "No tumor", "Pituitary"]
BREAST_CLASS_NAMES = ["Benign", "Malignant", "Normal",""]
KIDNEY_CLASS_NAMES = ["Cyst","Normal","Stone","Tumor"]



@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray: 
    with Image.open(BytesIO(data)) as img:
        img.thumbnail((256, 256))
        image = np.array(img) / 255.0
    return image





#Lung
@app.post("/predict1")
async def predict1(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    if image.shape[2] == 4:
        image = image[:, :, :3]
    image = tf.image.resize(image, (256, 256))
    img_batch = tf.expand_dims(image, 0)
    predictions = Lung.predict(img_batch)
    predicted_class = LUNG_CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


#Brain
@app.post("/predict2")
async def predict2(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    if image.shape[2] == 4:
        image = image[:, :, :3]
    image = tf.image.resize(image, (224, 224))
    img_batch = tf.expand_dims(image, 0)
    predictions = Brain.predict(img_batch)
    predicted_class = BRAIN_CLASS_NAMES[np.argmax(predictions[0])]
    print(np.argmax(predictions[0]))
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

#Breast
@app.post("/predict3")
async def predict3(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    if image.shape[2] == 4:
        image = image[:, :, :3]
    image = tf.image.resize(image, (256, 256))
    img_batch = tf.expand_dims(image, 0)
    predictions = Breast.predict(img_batch)
    
    predicted_class = BREAST_CLASS_NAMES[np.argmax(predictions[0])]
    print(np.argmax(predictions[0]))
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

#Kidney
@app.post("/predict4")
async def predict4(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    if image.shape[2] == 4:
        image = image[:, :, :3]
    image = tf.image.resize(image, (256, 256))
    img_batch = tf.expand_dims(image, 0)
    predictions = Kidney.predict(img_batch)
    predicted_class = KIDNEY_CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

#Skin
#@app.post("/predict5")
#async def predict5(file: UploadFile = File(...)):
#    image = read_file_as_image(await file.read())
#    if image.shape[2] == 4:
 #       image = image[:, :, :3]
#    image = tf.image.resize(image, (256, 256))
#    img_batch = tf.expand_dims(image, 0)
 #   predictions = Skin.predict(img_batch)
    
  #  predicted_class = SKIN_CLASS_NAMES[np.argmax(predictions[0])]
  #  print(np.argmax(predictions[0]))
 #   confidence = np.max(predictions[0])
 #   return {
   #     'class': predicted_class,
   #     'confidence': float(confidence)
  #  }



if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

