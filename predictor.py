class Predictor:

    def predict(self, img):
        img = test_img.copy()
        face, rect = detect_face(img)