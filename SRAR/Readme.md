# SRAR Assignment

In this repository you will find the code to run a Mask detection model built on YoloV5 pytorch framework. It is highly recommended that you need to have a system which can install pytorch package.

## Requirements 

#### System Requirements
```
Python >= 3.6
Windows 10 
Nvidia GPU (must!)
```

#### Packages Required
```
absl-py==0.13.0
cachetools==4.2.2
certifi==2021.5.30
charset-normalizer==2.0.1
colorama==0.4.4
cycler==0.10.0
google-auth==1.32.1
google-auth-oauthlib==0.4.4
grpcio==1.38.1
idna==3.2
kiwisolver==1.3.1
Markdown==3.3.4
matplotlib==3.4.2
numpy==1.21.0
oauthlib==3.1.1
opencv-python==4.5.3.56
pandas==1.3.0
Pillow==8.3.1
protobuf==3.17.3
pyasn1==0.4.8
pyasn1-modules==0.2.8
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2021.1
PyYAML==5.4.1
requests==2.26.0
requests-oauthlib==1.3.0
rsa==4.7.2
scipy==1.7.0
seaborn==0.11.1
six==1.16.0
tensorboard==2.5.0
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.0
thop==0.0.31.post2005241907
torch==1.9.0
torchvision==0.10.0
tqdm==4.61.2
typing-extensions==3.10.0.0
urllib3==1.26.6
Werkzeug==2.0.1
```

## Steps to run the object detection file 

### 1. Download the repository on your system and unzip the repository.

### 2. Open Command line and navigate to the folder path.

### 3. Create a Virtual environment

To create the virtual environment in the command line enter the below command. It will create a virtual env 'srar' in your folder.
```
pip3 install virtualenv
virtualenv srar
```

### 4. Activate the environment

To Activate the environment run the following command in cmd.

```
srar\Scripts\activate
```

### 5. Install the necessary packages

The below command will install all the necessary packages
```
pip install -r requirements.txt
```
### 6. Run the detection model

In the command line execute the python file
```
python detect_model.py
```

## Information about the detect_model.py file

The detect_model.py file will gain access to your webcam and start detecting mask and no mask labels. It will also count the number of people wearing and not wearing masks and display it on the screen.

#### If you want to change the source from webcam to a video file.

Open the detect_model.py file in your text editor or IDE and make changes to the line 33
```
source = '0'
```

to 

```
source = 'YOUR VIDEO FILE PATH'
```

The source is initially set to value '0' which is for webcam.

#### To close the detection screen.

While executing the code if you want to close the screen or video. Press 'Q' on your keyboard it will automatically end the detection. 
