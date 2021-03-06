# Physio PoseNet
Real-time pose validation for physiotherapy exercises using pre-trained TensorFlow.js model PoseNet

This application has been developed during [Arkathon 2019](https://innoboard.ch/arkathon/hhvalais2019)

## Contents
__frontend/arkathon-frontend__ - the code for the application frontend (Javascript)

__backend/physio-backend__ - the code for the application backend (Python)  

## Deploy

##### Build the docker image
```
cd physio-posenet
docker build -t physioarkathon/physio-backend:0.1.0 .
docker push physioarkathon/physio-backend:0.1.0
```

##### Run the app
```
docker pull physioarkathon/physio-backend:0.1.0
docker-compose up -d
```

Then open a browser and access
`http://localhost:8080/index.html`