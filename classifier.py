import cv2


class Classifier:
    def classify(self, faces, labels):
        face_recognizer = cv2.face.createLBPHFaceRecognizer()
        face_recognizer.train(faces, np.array(labels))
        return face_recognizer

    def draw_rectangle(img, rect):
        (x, y, w, h) = rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    def draw_text(img, text, x, y):
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)