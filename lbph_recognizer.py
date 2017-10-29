import cv2
import os
import numpy as np
from detector import Detector
from classifier import Classifier
from predictor import Predictor

class prep_data:
    def prep_train_data(self, fldr_pth, detector):
        dirs = os.listdir(fldr_pth)
        faces = []
        labels = []
        print(dirs)
        for dir_name in dirs:
            if not dir_name.startswith('s'):
                # print('check')
                continue
            label = int(dir_name[1])
            # print(dir_name[1])
            subject_dir_path = fldr_pth + "/" + dir_name
            subject_image_names = os.listdir(subject_dir_path)
            for image_name in subject_image_names:
                image_path = subject_dir_path + "/" + image_name
                image = cv2.imread(image_path)
                cv2.imshow("Training on image...", image)
                cv2.waitKey(10)
                face, rect = detector.detect_face(image)
                if face is not None:
                    faces.append(face)
                    labels.append(label)

                    cv2.destroyAllWindows()
                    cv2.waitKey(1)
                    cv2.destroyAllWindows()

        return faces, labels


prep = prep_data()
detect_algo = Detector()
train_data = os.path.join(os.path.dirname(__file__), 'training-data')
faces, labels = prep.prep_train_data(train_data, detect_algo)
print("Data prepared")

# print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

classify_trainer = Classifier()
fr = classify_trainer.classify()

prediction = Predictor()
prediction

