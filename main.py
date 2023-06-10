import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
import requests

app = FastAPI()

class Item(BaseModel):
    url: str

model = tf.keras.models.load_model('./model/WasteClassificationModel.h5')
# classes = ['Aluminium', 'Carton', 'Glass', 'Organic Waste', 'Other Plastics', 'Paper and Cardboard', 'Plastic', 'Textiles', 'Wood']

@app.get("/")
def hello_world():
    return {"message": "Hello, world!"}

@app.post("/predict")
async def classify_image(item:Item):
    img_data = requests.get(item.url).content
    with open('./temp/img.jpg', 'wb') as handler:
        handler.write(img_data)

    path = "./temp/img.jpg"
    image = tf.keras.preprocessing.image.load_img(path, target_size=(256, 256))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = np.expand_dims(image_array, 0)
    predictions = model.predict(image_array).tolist()
    return {"predictions": predictions}

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
