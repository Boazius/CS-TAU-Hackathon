# CS-TAU-Hackathon
CS crisis tech tau project

our talking file:
https://mailtauacil-my.sharepoint.com/:w:/g/personal/avnerf_mail_tau_ac_il/EVlPN3bz7uhOqgNRa8AfNeoBJRi1TAT1hmwr-8SWLGDzVA?e=nb2OIl

## Installiation
install python 3.10 with pip

navigate to detector folder and run:
`` pip install -r requirements.txt``

then run ```pip install imageai --upgrade```

then run ``` python app.py``` to run the flask server


now, run the chrome extension that can call the flask server with post:
```javascript
POST http://127.0.0.1:5000/detect -F "object_name=horse" -F "image=@/path/to/your/image.jpg"
```
which returns
```json
{
    "detected": false,
    "detection_time": 0.34709596633911133
}
```
if it is not detected

