import pickle
from server import sio

# data = ""
# payload_size = struct.calcsize("H") 
# while True:
#     while len(data) < payload_size:
#         data += conn.recv(4096)
#     packed_msg_size = data[:payload_size]
#     data = data[payload_size:]
#     msg_size = struct.unpack("H", packed_msg_size)[0]
#     while len(data) < msg_size:
#         data += conn.recv(4096)
#     frame_data = data[:msg_size]
#     data = data[msg_size:]
#     ###

#     frame = pickle.loads(frame_data)
#     cv2.imshow('frame',frame)


