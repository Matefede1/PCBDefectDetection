

#Links
 - Access the notebooks https://drive.google.com/drive/folders/14FmaoQ2mHIwcwJXi3L6quu_Wgx01i9Cn?usp=drive_link

# Service

Service to detect PCB failure to improve manufacture process and classify the type of manufacturing defects

The service, accessible through API and web site, intended to help sort defective cards by detecting from their image the location and type of defect observed. 

It takes as an input an image to analyzed (jpeg, gif or png) 
And send back an image with the detectection, the analysis and the data as a JSON file.

The program is trained to detect 6 faults: missing hole, mouse bite, open circuit, short, spur, and spurious copper



# Details

- Package: Matefede1/PCBDefectDetection

- Description: Customize a Object Detection Neural Network into a Defect Detection model to improve manufacture process at different critical stages

- From model yolov5 : https://github.com/ultralytics/yolov5
    * YOLOv5 🚀 is the world's most loved vision 
    * trained with 80 classes and coco datasets (188k images for training, 5k images for validation
    * retrained for PCB failure detecture with 6 labels and PCB-defects dataset (xx images for traing, xx images for validation) :
       - https://www.kaggle.com/datasets/akhatova/pcb-defects/code
       - This is a public synthetic PCB dataset containing 1386 images, released by the Open Lab on Human Robot Interaction of Peking University
       - PCB dataset was created using public link from https://github.com/Ixiaohuihuihui/Tiny-Defect-Detection-for-PCB

- Classifaction 
    0: Missing_hole
    1: Mouse_bite
    2: Open_circuit
    3: Short
    4: Spur
    5: Spurious_copper

# Package 

The package contains 4 directories

The dataset used to train the model : dataset
The API web service directpry : fast_api  
The web site directory : prueba_streamlit  
The model used for prediction directory : yolov5  
    
# Data

First, download the dataset from https://drive.google.com/drive/folders/1o7nf0rZ1JBzTNvth6Vs2yKlmt4yN10QQ
Unzip it and rename it datasets

It contains:
- datasets/images/train
- datasets/images/val
- datasets/labels/train
- datasets/labes/val

# Startup the project

The initial setup.

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
```

# Install

Install the project:

Go to `https://github.com/Matefede1/PCBDefectDetection/` 


Clone the project and install it:

```bash
git clone git@github.com:Matefede1/PCBDefectDetection.git #clone
cd PCBDefectDetection
pip install -r requirements.txt #install
```

# Use the service

Launch the service locally 

```bash
cd fast_api
uvicorn api:app --reload #launch the API server en localhost 

cd ../prueba_streamlit
streamlit run app.py   #launch the local server 
```

# Inference

```
#python detect.py --weights runs/train/exp/weights/best.pt --source ../datasets/your_path_to_the_images.jpeg
```

# Add modification


```bash
cd PCBDefectDetection
git add . 
git commit -m "adding work"
git push origin master  
``` 