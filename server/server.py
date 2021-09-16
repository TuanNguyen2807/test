# cd /d D:\Project 3\core\server
from flask_socketio import SocketIO
from flask import Flask, render_template, redirect, url_for, Request, Response
import cv2
import numpy as np
import base64
import os , io , sys
from PIL import Image
import imutils

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
# def messageReceived():
#     ret = True
#     cap = cv2.VideoCapture('./test.mp4')

#     while ret:
#         ret, frame1 = cap.read()
#         frame = cv2.imencode('.jpg', frame1)[1]
#         frame = frame.tobytes()

#         print('message received!!!')
#         sio.emit('my response', frame)
#         sio.sleep(0)

# @sio.on('my event')
# def handle_my_custom_event(json):
#     print('received my event: ' + str(json))
#     messageReceived()

# @sio.on('my event')
# def handle_my_custom_event(data, methods=['GET', 'POST']):
#     print('received my event: ' + data)
#     sio.emit('my response', data, callback=messageReceived)

# @sio.on('send data')
# def handle_data(data):
#     data = ""
#     payload_size = struct.calcsize("H") 
#     while True:
#         while len(data) < payload_size:
#             data += conn.recv(4096)
#         packed_msg_size = data[:payload_size]
#         data = data[payload_size:]
#         msg_size = struct.unpack("H", packed_msg_size)[0]
#         while len(data) < msg_size:
#             data += conn.recv(4096)
#         frame_data = data[:msg_size]
#         data = data[msg_size:]
#         ###

#         frame = pickle.loads(frame_data)

frame = b'\xff'

def generate_frames():
    while True:
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@sio.on('send data')
def image(stringData):
    global frame
    frame = stringData
    # nparr = np.fromstring(str_encode, np.uint8)
    # imgdecode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # cv2.imshow("img_decode", img_decode)
    # cv2.waitKey()
    

    # sbuf = io.StringIO()
    # sbuf.write(image)

    # # decode and convert into image
    # b = io.BytesIO(base64.b64decode(image))
    # pimg = Image.open(b)

    # ## converting RGB to BGR, as opencv standards
    # img = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    # yield img
    
    # # Process the image frame
    # # frame = imutils.resize(frame, width=700)
    # frame = cv2.flip(frame, 1)
    # imgencode = cv2.imencode('.jpg', frame)[1]

    # # base64 encode
    # stringData = base64.b64encode(imgencode).decode('utf-8')
    # b64_src = 'data:image/jpg;base64,'
    # stringData = b64_src + stringData

    # # emit the frame back
    # emit('response_back', stringData)
                   
if __name__ == "__main__":
    app.debug = True
    print('[INFO] Starting server at http://localhost:3456')
    sio.run(app=app, host='localhost', port=3456)