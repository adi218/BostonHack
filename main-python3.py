import numpy as numpy
import cv2


class person:
    def __init__(self, name = None, image = None, relation = None, info = None, met = None):
        self.name = name
        self.image = image
        self.relation = relation
        self.info = info
        self.met = met


def rectangle_width(person):
    str1 = "Name: " + person.name
    str2 = "Relationship: " + person.relation
    str3 = "Info: " + person.info
    str4 = "Met: " + person.met
    lengths = [len(str1),len(str2),len(str3),len(str4)]
    maxlen = max(lengths)
    return maxlen*250/18


def overlay(person,frame,x,y):
    if x <= 100:
        cv2.putText(frame, "Name: {}".format(person.name),
                    (x + 200, y + 90), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 0), 1)
        cv2.putText(frame, "Relationship: {}".format(person.relation),
                    (x + 200, y + 110), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 0), 1)
        cv2.putText(frame, "Info: {}".format(person.info),
                    (x + 200, y + 130), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 0), 1)
        cv2.putText(frame, "Met: {}".format(person.met),
                    (x + 200, y + 150), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 0), 1)
        rect_width = rectangle_width(person)
        cv2.rectangle(frame, (x + 200, y + 70), (x + 200 + rect_width, y + 165), 1)
    else:
        cv2.putText(frame, "Name: {}".format(person.name),
                    (x - 300, y + 90), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 0), 1)
        cv2.putText(frame, "Relationship: {}".format(person.relation),
                    (x - 300, y + 110), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 0), 1)
        cv2.putText(frame, "Info: {}".format(person.info),
                    (x - 300, y + 130), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 0), 1)
        cv2.putText(frame, "Met: {}".format(person.met),
                    (x - 300, y + 150), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 0), 1)
        rect_width = rectangle_width(person)
        cv2.rectangle(frame, (x - 300, y + 70), (x - 300 + rect_width, y + 165), 1)


person1 = person("Aislinn", cv2.imread("people.jpg"), "friend", "Likes cats", "At school")
person2 = person("Emma",cv2.imread("people.jpg"), "friend", "cool", "hackathon")
people = [person1, person2]


def main():
    # import pre-trained haar-cascade classifier
    # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    # possible use for eye detection for increased accuracy?

    # sets video source to default webcam
    video_capture = cv2.VideoCapture(0)

    x_list = [0, 0, 0, 0]
    y_list = [0, 0, 0, 0]

    while True:
        ret, frame = video_capture.read()  # Capture frame by frame
        if ret is True:
            # if true, then it was read correctly
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale
        else:
            continue

        # store and detect face coordinates
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.8,
                                          minNeighbors = 5, minSize = (30, 30),
                                          flags = cv2.CASCADE_SCALE_IMAGE)
        # larger scale factor = smaller photo sample and faster face tracking
        # faces returned as a list of rectangles

        face_list = []

        for (x, y, w, h) in faces:
            # draw rectangle around each detected face, can remove later
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            # create a crop of just the face
            cropped = frame[y:y+h, x:x+w]
            face_plus_coord = [cropped, [x, y, w, h]]
            face_list.append(face_plus_coord)
            try:
                overlay(people[len(face_list)-1], frame, x, y)
            except:
                pass
        try:
            # try to display the cropped photo
            cv2.imshow('cropped', frame)
            i = 0
            for face in face_list:
                name = "face" + str(i)
                cv2.imwrite(name, face)
        except:
            # if faulty frame, just pass onto next frame
            pass

        # search for face captured
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
	main()