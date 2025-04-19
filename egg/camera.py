#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This scrtipt script..

import cv2
import numpy as np
from datetime import datetime

class VideoCamera(object):
    def __init__(self, flip=False, file=False, file_type  = ".jpg", photo_string= "stream_photo"):
        self.stream = cv2.VideoCapture(0)
        
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        self.flip = flip
        self.file = file
        self.file_type = file_type
        self.photo_string = photo_string
        
        if not self.stream.isOpened():
                raise RintimeError("couldnt open video source")

    def __del__(self):
        if hasattr(self, 'stream'):
                self.stream.release()

    def get_frame(self):
        ret, frame = self.stream.read()
        
        if self.flip:
                frame = np.flip(frame, 0)
                
        ret, jpeg = cv2.imencode(self.file_type, frame)
        return jpeg.tobytes()
        
