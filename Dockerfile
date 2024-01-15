

####### 👇 OPTIMIZED SOLUTION (x86)👇 #######

# tensorflow base-images are optimized: lighter than python-buster + pip install tensorflow
FROM tensorflow/tensorflow:2.10.0

# OR for apple silicon, use this base image instead
# FROM armswdev/tensorflow-arm-neoverse:r22.09-tf-2.10.0-eigen

#WORKDIR /prod

# We strip the requirements from useless packages like `ipykernel`, `matplotlib` etc...
COPY requirements_api.txt requirements.txt
RUN pip install -r requirements.txt

COPY fast_api fast_api
COPY yolov5 yolov5
#RUN pip install .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


CMD uvicorn fast_api.api:app --host 0.0.0.0 --port 8000
