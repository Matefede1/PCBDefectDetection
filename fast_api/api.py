from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response

import numpy as np
import cv2
import io
from face_rec.face_detection import annotate_face
from face_rec.face_detection import annotate_face
from prediction import run_yolov5_detection
from transfo_text_img import array_to_image
from transfo_text_img import save_image


app = FastAPI()

# # Allow all requests (optional, good for development purposes)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

@app.get("/")
def index():
    return {"status": "ok"}

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image from the fast api
    contents = await img.read()
    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

    #Save image from the POST (linea 240 en el file predict.py)
    # add line240
    #cv2.imwrite('../yolov5/runs/detect/exp/image.jpeg', im0)
    output_path='./img_output/image.jpeg'
    save_image(cv2_img, output_path)

     #Do the prediction
    run_yolov5_detection('./img_output/image.jpeg')

    # where is the image after the prediction
    image_path = '../yolov5/runs/detect/exp/image.jpeg'

    # Read the image i
    annotated_img = cv2.imread(image_path)

    ### Responding with the image
    im = cv2.imencode('.png', annotated_img)[1] # extension depends on which format is sent from Streamlit
    return Response(content=im.tobytes(), media_type="image/png")
