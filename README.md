# Heart Disease Prediction API


This repository contains source code of our project for Provathon.  Heart Disease Prediction API is Machine Learning based solution to predict risks of heart disease using a integrable API.


# Description

Our solution is based on microservices architecture and the AI Model can be independently used in any other platform with ease. We've also included a demo dashboard of our smart watch simulator where we can receive patient's real time health data directly from his smart watch and use those value to get a realtime prediction  of immediate risks of heart attacks in a patient. This real time prediction is  also simulated in a continuous graph to warn the patients in case of any risks.<br>
In similar way, our api can be integrated with any smart watches, hospital management system, health apps to get a real time prediction of immediate risks of heart attacks.

<img src="https://media.discordapp.net/attachments/862925813989244930/863628224932347904/unknown.png">


## Technical Aspect

<img src="https://d1.awsstatic.com/logos/aws-logo-lockups/poweredbyaws/PB_AWS_logo_RGB.61d334f1a1a427ea597afa54be359ca5a5aaad5f.png" width=100>  <img src="https://www.devteam.space/wp-content/uploads/2017/03/dockericon-min.png" width=100> <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" width=100>
<img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" width=100>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width=100>
<img src="https://cms-assets.tutsplus.com/uploads/users/1251/posts/28278/preview_image/chartjs-tutsplus.jpg" width=100>



## Response

```json
{
  "status":"success",
  "value":"92",
  "risk":true,
}
```

**status** : If any error occured in backend it will say error else it will be set to success. <br>
**value** : Confidence measure of the AI Model. <br>
**risk** : boolean value which says if the risk of heart disease is high ( default threshold is 75% ) 


# Installation and Test on Local Machine

## Step 1: Installation of WebApp.

```bash
git clone https://github.com/Romansth/heart-disease-api.git
cd heart-disease-api/backend
pip install django requests numpy pickle django-cors-headers 
python manage.py
```


## Step 2: Installation of AI Model

```bash
cd heart-disease-api/api
pip install flask pickle numpy flask-cors
python Deployed_Flask_App.py
```
## Step 3:  Run Smartwatch Simulator

```bash
cd heart-disease-api
python smartwatch_simulator.py
```
## Step 4: Go to heart-disease-api/frontend and open index.html

After following all these steps, the demo app will successfully run on your local machine.

Feel free to contribute !
