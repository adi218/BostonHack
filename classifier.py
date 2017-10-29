import cv2
import numpy as np


class Classifier:
    def classify(self, faces, labels):
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.train(faces, np.array(labels))
        return face_recognizer

