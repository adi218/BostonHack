from detector import Detector
import cv2


class Predictor:
    def __init__(self):
        self.detect = Detector()

    def draw_rectangle(self, img, rect):
        (x, y, w, h) = rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    def draw_text(self, img, text, x, y):
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    def predict(self, test_img, fr):
        img = test_img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face, rect = self.detect.detect_face(img)
        label = fr.predict(gray)
        print(label)

        self.draw_rectangle(img, rect)

        self.draw_text(img, str(label), rect[0], rect[1] - 5)

        return img
