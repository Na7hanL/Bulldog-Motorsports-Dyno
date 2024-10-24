from data import *

# 10/23
#Create model to hold values
#Get numbers updating via random method for now, but with correct data format

class homeWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.rpmLabel = QtWidgets.QLabel("0")
        self.pwrLabel = QtWidgets.QLabel("0")
        self.trqLabel = QtWidgets.QLabel("0")

        self.layout = QtWidgets.QHBoxLayout(self)

        self.rpmlayout = QtWidgets.QHBoxLayout(self)
        self.rpmlayout.addWidget(QtWidgets.QLabel("RPM:"))
        self.rpmlayout.addWidget(self.rpmLabel)

        self.pwrlayout = QtWidgets.QHBoxLayout(self)
        self.pwrlayout.addWidget(QtWidgets.QLabel("PWR:"))
        self.pwrlayout.addWidget(self.pwrLabel)

        self.trqlayout = QtWidgets.QHBoxLayout(self)
        self.trqlayout.addWidget(QtWidgets.QLabel("TRQ:"))
        self.trqlayout.addWidget(self.trqLabel)

        self.layout.addLayout(self.rpmlayout)
        self.layout.addLayout(self.pwrlayout)
        self.layout.addLayout(self.trqlayout)

class TabWidgetApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bulldog Motorsports Dyno')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.model = DynoModel()

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.tab_widget = QtWidgets.QTabWidget()
        self.tab1 = homeWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tab4 = QtWidgets.QWidget()

        self.tab_widget.addTab(self.tab1, "Main View")
        self.tab_widget.addTab(self.tab2, "Power Output View")
        self.tab_widget.addTab(self.tab3, "Graph View")
        self.tab_widget.addTab(self.tab4, "Compare Graphs")

        self.layout.addWidget(self.tab_widget)

        self.initTab2()
        self.initTab3()
        self.initTab4()

        self.bottomButtonLayout = QtWidgets.QHBoxLayout()

        self.driveRatioButton = QtWidgets.QPushButton("Set Drive Ratio")
        self.bottomButtonLayout.addWidget(self.driveRatioButton)

        self.rpmCutoffButton = QtWidgets.QPushButton("Set Cutoff RPM")
        self.bottomButtonLayout.addWidget(self.rpmCutoffButton)

        self.startButton = QtWidgets.QPushButton("Start Run")
        self.bottomButtonLayout.addWidget(self.startButton)

        self.endButton = QtWidgets.QPushButton("End Run")
        self.bottomButtonLayout.addWidget(self.endButton)

        self.layout.addLayout(self.bottomButtonLayout)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateFakeRandomData)
        timer.start(50)

    def initTab2(self):
        layout = QtWidgets.QVBoxLayout(self.tab2)
        label = QtWidgets.QLabel("Content of Tab 2")
        layout.addWidget(label)

    def initTab3(self):
        layout = QtWidgets.QVBoxLayout(self.tab3)
        label = QtWidgets.QLabel("Content of Tab 3")
        layout.addWidget(label)

    def initTab4(self):
        layout = QtWidgets.QVBoxLayout(self.tab3)
        label = QtWidgets.QLabel("Content of Tab 4")
        layout.addWidget(label)

    def updateFakeRandomData(self):
        self.model.dynoStats[0] = random.randint(0, 12000)
        self.model.dynoStats[1] = random.randint(0, 50)
        self.model.dynoStats[2] = random.randint(0, 100)

        #TODO Read current tab to only update active 
        self.tab1.rpmLabel.setText(self.model.getRPM())
        self.tab1.trqLabel.setText(self.model.getTRQ())
        self.tab1.pwrLabel.setText(self.model.getPWR())

        self.model.layoutChanged.emit()

    def getSerialData(self):
        # Set up the serial port
        ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your serial port and 9600 with your baud rate
        ser.parity = serial.PARITY_NONE
        ser.bytesize = serial.EIGHTBITS
        
