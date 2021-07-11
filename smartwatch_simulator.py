import requests
import time
import random

while True:
    heartBeat = random.randint(50,150)
    bp = random.randint(80,250)

    requests.get(f"http://localhost:8000/patient/bp/{bp}")
    requests.get(f"http://localhost:8000/patient/heart-rate/{heartBeat}")
    print(heartBeat, bp)
    time.sleep(1)