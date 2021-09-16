# cd /d D:\Project 3\core\raspberry
import socketio, cv2, pickle, struct
import pyshine as ps # pip install pyshine
import imutils # pip install imutils
import requests
import numpy as np
import base64
import os , io , sys
from PIL import Image

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[2]

if int(minor_ver) < 3:
    tracker = cv2.Tracker_create(tracker_type)
else:
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    if tracker_type == 'GOTURN':
        tracker = cv2.TrackerGOTURN_create()
    if tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    if tracker_type == "CSRT":
        tracker = cv2.TrackerCSRT_create()

socketIO = socketio.Client()

video = cv2.VideoCapture(0)

ok, frame = video.read()

# Define an initial bounding box
bbox = cv2.selectROI(frame, False)

ok = tracker.init(frame, bbox)

socketIO.connect('http://localhost:3456')

# @socketIO.event
# def connect_error(data):
#     print("The connection failed!")

# @socketIO.event
# def disconnect():
#     print(" disconnected!")

@socketIO.event
def connect():
    print('connection established')
    while (video.isOpened()):
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break

        # Update tracker
        ok, bbox = tracker.update(frame)

        # # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
        #     # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        
        ## converting RGB to BGR, as opencv standards
        # frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

        # Process the image frame
        # frame = imutils.resize(frame, width=300, height=300)
        frame = cv2.flip(frame, 1)
        imgencode = cv2.imencode('.jpg', frame)[1]

        stringData = imgencode.tobytes()
        # data_encode = np.array(imgencode)
        # stringData = data_encode.tostring()

        # stringData = base64.b64encode(imgencode).decode('utf-8')
        # b64_src = 'data:image/jpg;base64,'
        # stringData = b64_src + stringData

        # emit the frame back
        socketIO.emit('send data', stringData)
        
# while (video.isOpened()):
#     # Read a new frame
#     ok, frame = video.read()
#     if not ok:
#         break

#     # Update tracker
#     ok, bbox = tracker.update(frame)

#     # Draw bounding box
#     if ok:
#         # Tracking success
#         p1 = (int(bbox[0]), int(bbox[1]))
#         p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
#         cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
#     else :
#         # Tracking failure
#         cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

#     # Display tracker type on frame
#     a = pickle.dumps(frame)
#     message = struct.pack("Q",len(a))+a
#     # socketIO.send(message)
#     # Display result
#     cv2.imshow("Tracking", frame)

#     # Exit if ESC pressed
#     k = cv2.waitKey(1) & 0xff
#     if k == 27 : break