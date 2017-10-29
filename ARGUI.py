
import sys
from PyQt5 import QtWidgets, QtGui


class person:
    def __init__(self, name = None, relation = None, met = None):
        self.name = name
        self.relation = relation
        self.met = met

class recordFace( QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(recordFace, self).__init__(parent)
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Record New Face')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.recordNewFace()

    def recordNewFace(self):
        font = QtGui.QFont("Avenir",12)

class trackFaces(  QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(trackFaces, self).__init__(parent)
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Tracking Faces')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.liveFaceRec()

    def liveFaceRec(self):
        font = QtGui.QFont("Avenir",12)


class logInfo(  QtWidgets.QMainWindow):
  def __init__(self, parent = None):
    super(logInfo, self).__init__(parent)

    self.setGeometry(300, 300, 700, 500)
    self.setWindowTitle('Log Info')
    self.setWindowIcon(QtGui.QIcon('web.png'))

    self.infoPage()

  def infoPage(self):
    font = QtGui.QFont("Avenir", 12)
    titleFont = QtGui.QFont("Avenir", 20)

    self.title = QtGui.QLabel("Enter person's information below", self)
    self.title.move(200, 15)
    self.title.setFont(titleFont)
    self.title.resize(400, 50)

    self.logFaceBtn = QtGui.QPushButton("Log Face", self)
    self.logFaceBtn.move(300, 450)
    self.logFaceBtn.setFont(font)

    self.nameEntry = QtGui.QLineEdit(self)
    self.nameEntry.move(200, 100)
    self.nameEntry.resize(300, 25)

    self.relationEntry = QtGui.QLineEdit(self)
    self.relationEntry.move(200, 175)
    self.relationEntry.resize(300, 25)

    self.meetingEntry = QtGui.QLineEdit(self)
    self.meetingEntry.move(200, 250)
    self.meetingEntry.resize(300, 25)

    self.name = QtGui.QLabel("Name: ", self)
    self.name.move(100, 100)
    self.name.setFont(font)

    self.relation = QtGui.QLabel("Relationship: ", self)
    self.relation.move(100, 175)
    self.relation.setFont(font)

    self.meeting = QtGui.QLabel("Where you met: ", self)
    self.meeting.move(100, 250)
    self.meeting.setFont(font)

    self.logFaceBtn.clicked.connect(self.on_btn3_clicked)
    self.recordNewFace = recordFace(self)

  def on_btn3_clicked(self):
    #new instance of person
    name = self.nameEntry.text()
    relation = self.relationEntry.text()
    met = self.meetingEntry.text()
    newPerson = person(name, relation, met)

    f = open("peopleData.txt", "a+")

    f.write("%s \n" % newPerson.name)
    f.write("%s \n" % newPerson.relation)
    f.write("%s \n" % newPerson.met)

    f.close()

    #open up webcam & record snapshots of the person, send to aditya to train





class First(  QtWidgets.QMainWindow):

    def __init__(self):
        super(First, self).__init__()

        # self.storeFace()

        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Face Recognition')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.first_page()

    def first_page(self):
       	#Store new face button
        font = QtGui.QFont("Avenir", 12)
        titleFont = QtGui.QFont("Avenir", 40)
        subFont = QtGui.QFont("Avenir", 20)
        self.title = QtGui.QLabel("Welcome!", self)
        self.title.resize(400, 65)
        self.title.move(250, 35)
        self.title.setFont(titleFont)

        self.subTitle = QtGui.QLabel("Choose a function below", self)
        self.subTitle.resize(200, 30)
        self.subTitle.move(275, 85)
        self.subTitle.setFont(font)

        self.setWindowTitle('Welcome')
       	self.logBtn = QtGui.QPushButton("Log New Face", self)
       	self.logBtn.move(115, 250)
        self.logBtn.setFont(font)
        self.logBtn.resize(200, 25)

       #Track faces button
       	self.trackBtn = QtGui.QPushButton('Track Face', self)
       	self.trackBtn.move(365, 250)
        self.trackBtn.setFont(font)
        self.trackBtn.resize(200, 25)
       	
        #logBtn clicked 
        self.logBtn.clicked.connect(self.on_btn1_clicked)
        self.logInfo = logInfo(self)

        #tracBtn clicked
        self.trackBtn.clicked.connect(self.on_btn2_clicked)
        self.trackFaces = trackFaces(self)

    def on_btn1_clicked(self):
      self.logInfo.show()

    def on_btn2_clicked(self):

        #Facial tracking part opens, folders, checks which face it is within folders, data gets sent back to me
        number = 5;

        file = open("peopleData.txt", 'r')

        nameNum = 3*(number-1)+1
        for x in range(0, nameNum):
           name = file.readline()
        
        relation = file.readline()
        met = file.readline()
        personOut = person(name, relation, met)
        file.close()

        #Code to output who it is on the screen over the face

       
def main():
    
    app =   QtWidgets.QApplication(sys.argv)
    ex = First()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
