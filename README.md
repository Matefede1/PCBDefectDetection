

#Links
 - Access the notebooks https://drive.google.com/drive/folders/14FmaoQ2mHIwcwJXi3L6quu_Wgx01i9Cn?usp=drive_link


# Data analysis
- Document here the project: Matefede1/PCBDefectDetection
- Description: Customize a Object Detection Neural Network into a Defect Detection model to improve manufacture process at different critical stages
- Data Source: xxxxxx (to be completed)
- Type of model: yolov5 (to be completed) 

# Package 
- fast_api 
- datasets
- prueba_streamlit
- yolov5

# Data

- Datasets/images/train
- Datasets/images/val
- Datasets/labels/train
- Datasets/labes/val

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
```

# Install

Go to `https://github.com/Matefede1/PCBDefectDetection/` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:


Clone the project and install it:

```bash
git clone git@github.com:Matefede1/PCBDefectDetection.git #clone
cd PCBDefectDetectio
pip install -r requirements.txt #install
```

# Use the service

The launch local service 


```bash
cd fast_api
uvicorn api:app --reload #launch the API server en localhost 

cd ../prueba_streamlit
streamlit run app.py   #launch the local server 
```


