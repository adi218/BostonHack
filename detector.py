import cv2

class Detector:
    # function to detect face using OpenCV
    def detect_face(self, img):

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        if (len(faces) == 0):
            return None, None

        (x, y, w, h) = faces[0]

        # return only the face part of the image
        return gray[y: y + w, x: x + h], faces[0]
