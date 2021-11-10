import cv2

from detection import utils


class CascadeClassifier:
    def __init__(self):
        path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        self.detector = cv2.CascadeClassifier(path)
        self.options = {'scaleFactor': 1.10, 'minNeighbors': 5,
                        'minSize': (30, 30), 'flags': cv2.CASCADE_SCALE_IMAGE}

    def detect(self, image):
        image_gray = utils.bgr2gray(image)

        positions = self.detector.detectMultiScale(image_gray, **self.options)

        return positions
