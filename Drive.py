#
# Author: Arsh
# Created On: 13 May, 2019 at 11:25:37
# Username: arsh_16
#
import socketio
import eventlet
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
import random
# Web sockets are used to perform real time communication between the client and the server

sio = socketio.Server()
# Whenever python execuctes the script, it assigns the name which is "main". Here main is assigned to name
app = Flask(__name__) # __main__

# @app.route("/home") # this function will run if the user navigates to this path on browser
# def greeting():
#     return "Welcome!"

def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img

speed_limit = 10
@sio.on('telemetry')
def telemetry(sid, data): # simulator sends the data to telemetry after connection
    speed = float(data['speed'])
    image = Image.open(BytesIO(base64.b64decode(data['image']))) #decode the base64 encoded image
    # BytesIO is used to mimic the data as a normal file which can then be opened by Image module
    image = np.asarray(image)
    image = img_preprocess(image)
    image = np.array([image]) # to add an extra dimension as model takes 4d image
    steering_angle = float(model.predict(image))
    throttle = 1 -speed/speed_limit
    # print(steering_angle, throttle, speed)
    if -0.1<=steering_angle<=0.1:
        print("Moving Straight")
    elif -0.5<=steering_angle<=0.1:
        print("Taking Slight Left")
    elif steering_angle<-0.5:
        print("Taking Sharp Left")
    elif 0.5>=steering_angle>=0.1:
        print("Taking Slight Right")
    else:
        print("Taking Sharp Right")
    send_control(steering_angle, 1)


@sio.on('connect') # fires on when connected
def connect(sid, environ):
    print("Connected")
    send_control(0, 0) # make the car have 0 angle and throttle at beginning

def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle':steering_angle.__str__(),
        'throttle':throttle.__str__()
    })
if __name__=="__main__":
    model = load_model('model.h5')
    # app.run(port = 3000)
    app = socketio.Middleware(sio, app) #combines socketio server with our web app
    # lets make use of web server gateaway interface to make web server send any request made by the client to the web server
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app) # listen request on any available ip but on port 4567



