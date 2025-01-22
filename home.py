from data import *

medFont = QtGui.QFont("Cambria Math", pointSize=40)
largeFont = QtGui.QFont("Cambria Math", pointSize=80)

#TODO
# - New Session Button
# - Max TRQ/PWR @ RPM Stats
# - Add Units
#   - Only allow files of same unit in graph view? 
#   - Graph always displays same unit, converts only those in wrong unit
# - Multiply by drive ratio
# - Select files from different sessions

class cutoffModal(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Cutoff RPM")

        self.layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Cutoff RPM: ")
        self.lineEdit = QtWidgets.QLineEdit()

class homeWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.rpmLabel = QtWidgets.QLabel("0")
        self.rpmLabel.setFixedWidth(150)
        self.rpmLabel.setAlignment(QtCore.Qt.AlignRight)
        #self.rpmLabel.setAlignment(QtCore.Qt.AlignVCenter)
        self.rpmLabel.setFont(medFont)

        self.pwrLabel = QtWidgets.QLabel("0")
        self.pwrLabel.setAlignment(QtCore.Qt.AlignRight)
        self.pwrLabel.setFont(medFont)
        
        self.trqLabel = QtWidgets.QLabel("0")
        self.trqLabel.setAlignment(QtCore.Qt.AlignRight)
        self.trqLabel.setFont(medFont)

        self.layout = QtWidgets.QHBoxLayout(self)

        self.graphicsLayout = pg.GraphicsLayoutWidget(show=True, title="Dyno Stats")

        self.rpmGraph = self.graphicsLayout.addPlot(title="Engine RPM", row=0, column=0)
        self.rpmCurve = self.rpmGraph.plot(pen='g')

        self.pwrGraph = self.graphicsLayout.addPlot(title="Power", row=1, column=0)
        self.pwrCurve = self.pwrGraph.plot(pen='b')

        self.trqGraph = self.graphicsLayout.addPlot(title="Torque", row=2, column=0)
        self.trqCurve = self.trqGraph.plot(pen='r')

        self.statsLayout = QtWidgets.QVBoxLayout(self)  

        self.rpmlayout = QtWidgets.QHBoxLayout(self)
        rpmTitle = QtWidgets.QLabel("RPM:")
        rpmTitle.setFont(medFont)
        rpmTitle.setAlignment(QtCore.Qt.AlignRight)
        self.rpmlayout.addWidget(rpmTitle)
        self.rpmlayout.addWidget(self.rpmLabel)

        self.pwrlayout = QtWidgets.QHBoxLayout(self)
        pwrTitle = QtWidgets.QLabel("PWR:")
        pwrTitle.setFont(medFont)
        pwrTitle.setAlignment(QtCore.Qt.AlignRight)
        self.pwrlayout.addWidget(pwrTitle)
        self.pwrlayout.addWidget(self.pwrLabel)

        self.trqlayout = QtWidgets.QHBoxLayout(self)
        trqTitle = QtWidgets.QLabel("TRQ:")
        trqTitle.setFont(medFont)
        trqTitle.setAlignment(QtCore.Qt.AlignRight)
        self.trqlayout.addWidget(trqTitle)
        self.trqlayout.addWidget(self.trqLabel)

        self.statsLayout.addLayout(self.rpmlayout)
        self.statsLayout.addLayout(self.pwrlayout)
        self.statsLayout.addLayout(self.trqlayout)

        self.layout.setSpacing(20)
        #self.layout.setStretch(0, 200)

        self.layout.addLayout(self.statsLayout)
        self.layout.addWidget(self.graphicsLayout)

class powerWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.rpmLabel = QtWidgets.QLabel("0")
        self.rpmLabel.setFont(largeFont)
        self.rpmLabel.setAlignment(QtCore.Qt.AlignRight)
        self.pwrLabel = QtWidgets.QLabel("0")
        self.pwrLabel.setFont(largeFont)
        self.pwrLabel.setAlignment(QtCore.Qt.AlignRight)
        self.trqLabel = QtWidgets.QLabel("0")
        self.trqLabel.setFont(largeFont)
        self.trqLabel.setAlignment(QtCore.Qt.AlignRight)

        self.layout = QtWidgets.QHBoxLayout(self)

        rpmTitle = QtWidgets.QLabel("RPM:")
        rpmTitle.setFont(largeFont)
        rpmTitle.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.rpmlayout = QtWidgets.QVBoxLayout(self)
        self.rpmlayout.addWidget(rpmTitle)
        self.rpmlayout.addWidget(self.rpmLabel)

        pwrTitle = QtWidgets.QLabel("PWR:")
        pwrTitle.setFont(largeFont)
        pwrTitle.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

        self.pwrlayout = QtWidgets.QVBoxLayout(self)
        self.pwrlayout.addWidget(pwrTitle)
        self.pwrlayout.addWidget(self.pwrLabel)

        trqTitle = QtWidgets.QLabel("TRQ:")
        trqTitle.setFont(largeFont)
        trqTitle.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

        self.trqlayout = QtWidgets.QVBoxLayout(self)
        self.trqlayout.addWidget(trqTitle)
        self.trqlayout.addWidget(self.trqLabel)

        self.layout.addLayout(self.rpmlayout)
        self.layout.addLayout(self.pwrlayout)
        self.layout.addLayout(self.trqlayout)

class graphWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        self.graphics = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")

        self.layout.addWidget(self.graphics)

        self.rpmGraph = self.graphics.addPlot(title="Engine RPM")
        self.rpmCurve = self.rpmGraph.plot(pen='g')

        self.pwrGraph = self.graphics.addPlot(title="Power")
        self.pwrCurve = self.pwrGraph.plot(pen='b')

        self.trqGraph = self.graphics.addPlot(title="Torque")
        self.trqCurve = self.trqGraph.plot(pen='r')

class compareWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Create the layout for the widget
        self.layout = QtWidgets.QVBoxLayout(self)

        # Create a Matplotlib figure and axis
        self.fig, self.ax1 = plt.subplots()
        self.ax2 = self.ax1.twinx()

        # Bounds
        self.metPWRBound = 70
        self.metTRQBound = 70



        # Plot the first y-axis (Torque)
        
        self.ax1.set_xlim(0,15000)
        self.ax1.set_ylim(0,self.metTRQBound)
        self.ax1.set_xlabel('Engine RPM')
        self.ax1.set_ylabel('Power (Hp)')

        # Create a second y-axis (RPM)
        self.ax2.set_ylim(0,self.metPWRBound)
        self.ax2.set_ylabel('Torque (Nm)', color='grey')
        #self.ax2.tick_params(axis='y')

        # Set the title
        self.fig.suptitle('Torque vs Power')

        # Embed the Matplotlib figure into the PySide6 widget
        self.canvas = FigureCanvas(self.fig)
        
        self.graphLayout = QtWidgets.QHBoxLayout()
        self.graphLayout.addWidget(self.canvas)
        
        self.colorWidget = ColorLabelWidget()
        self.graphLayout.addWidget(self.colorWidget)
        
        self.layout.addLayout(self.graphLayout)

        # Draw the canvas
        self.canvas.draw()

        fileLayout = QtWidgets.QVBoxLayout()
        fileLayout.setSpacing(0)
        fileLayout.setContentsMargins(0,20,0,0)
        fileLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.button = QtWidgets.QPushButton('Open File Explorer', self)
        self.button.setFixedHeight(50)
        font = QtGui.QFont()  # Create a QFont object
        font.setPointSize(15)  # Set font size to 20 points
        self.button.setFont(font)  # Apply the font to the button

        self.button.clicked.connect(self.open_file_dialog)  # Connect the button click to the file dialog
        fileLayout.addWidget(self.button)

        self.label = QtWidgets.QLabel('No files selected', self)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label.setContentsMargins(0,5,0,10)
        fileLayout.addWidget(self.label)

        self.layout.addLayout(fileLayout)

    def open_file_dialog(self):
        initial_directory = os.path.join(os.getcwd(), 'results')

        self.ax1.cla()
        self.ax2.cla()
        self.ax1.clear()
        self.ax2.clear()

        # Remove auto generated 0-1 ticks made by .cla()
        self.ax2.set_yticks([])
        self.ax1.set_yticks([])

        # Reset axis
        self.ax1.set_xlim(0,15000)
        self.ax1.set_ylim(0,self.metPWRBound)
        self.ax1.set_xlabel('Engine RPM')
        self.ax1.set_ylabel('Power (Hp)')
        self.ax1.tick_params(axis='y')
        
        
        self.ax2 = self.ax1.twinx()
        self.ax2.set_ylim(0,self.metTRQBound)
        self.ax2.set_ylabel('Torque (Nm)', color='grey')
        self.ax2.tick_params(axis='y')

        # Open the file dialog with the option to select multiple files
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Select Files", initial_directory, "All Files (*)")
        
        # Limit the selection to a maximum of 8 files
        if files:
            
            colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'magenta']
            
            files = files[:8]  # Take the first 8 files if more than 8 are selected
            # Update the label with the selected files
            self.label.setText(f'{len(files)} files selected.')
            print(f'Selected Files: {", ".join(files)}')
            for idx, file in enumerate(files):
                self.csvToGraph(file, colors[idx])

            self.ax1.set_yticks(np.linspace(0,self.metPWRBound,15))
            self.ax2.set_yticks(np.linspace(0,self.metTRQBound,15))



            self.canvas.draw()
            
            self.colorWidget.updateLabels(files)
        
        else:
            self.label.setText('No files selected')
    
    def csvToGraph(self, filepath, color):
        
        data = []
        pwr = []
        trq = []
        rpm = []
        try:
            with open(filepath, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)  # Create a CSV reader object

                # Iterate through the rows in the CSV
                for row in csv_reader:
                    data.append((round(float(row[0]),2), round(float(row[1]),2),round(float(row[2]),2)))

                data = sorted(data, key=lambda x: x[0])

                for tuple in data:
                    rpm.append(tuple[0])
                    trq.append(tuple[1])
                    pwr.append(tuple[2])

                self.ax1.plot(rpm, pwr, color=QtGui.QColor(color).name())
                self.ax2.plot(rpm, trq, color=self.lighten_qcolor(QtGui.QColor(color)).name())

        except:
            print(f'Invalid File Provided: {filepath}')

    def lighten_qcolor(self, color, factor=0.6):
        """
        Lighten a QColor by increasing the brightness.
        :param color: QColor object to lighten.
        :param factor: Factor to lighten the color. 0.0 means no change, 1.0 means completely white.
        :return: New QColor object for the lighter shade.
        """
        # Get RGB components of the QColor
        r = color.red()
        g = color.green()
        b = color.blue()

        # Lighten the color
        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))

        # Return a new QColor with the modified values
        return QtGui.QColor(r, g, b)

class TabWidgetApp(QtWidgets.QMainWindow):
    def __init__(self, debug=True):
        super().__init__()
        
        # Window Configuration 
        self.setWindowTitle('Bulldog Motorsports Dyno')
        self.setGeometry(100, 100, 1350, 900)
        self.setMinimumHeight(600)
        self.setMinimumWidth(900)
        self.logoIcon = QtGui.QIcon('./images/logosmall.png')
        self.setWindowIcon(self.logoIcon)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)


        # Model Configuration
        self.model = DynoModel()

        # Persistent variables
        self.dynoData = {}
        
        with open("config.json", 'r') as config:
            self.dynoData = json.load(config)


        # Session variables
        self.sessionName = ""
        self.recording = False
        self.debug = debug
        self.csvValues = []

        if not self.debug:
            # Serial port
            self.ser = serial.Serial('COM12', 9600, timeout=5)  # Replace 'COM3' with your serial port and 9600 with your baud rate
            self.ser.parity = serial.PARITY_NONE
            self.ser.bytesize = serial.EIGHTBITS

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateData)
        # Slow for testing purposes
        # TODO increase timing
        timer.start(5)


        # Tab Widget configuration 
        self.tab_widget = QtWidgets.QTabWidget()
        self.tab1 = homeWidget()
        self.tab2 = powerWidget()
        self.tab3 = graphWidget()
        self.tab4 = compareWidget()

        self.tab_widget.addTab(self.tab1, "Main View")
        self.tab_widget.addTab(self.tab2, "Power Output View")
        self.tab_widget.addTab(self.tab3, "Graph View")
        self.tab_widget.addTab(self.tab4, "Compare Graphs")

        self.layout.addWidget(self.tab_widget)

        # Bottom Banner configuration
        self.bottomButtonLayout = QtWidgets.QHBoxLayout()

        self.driveRatioButton = QtWidgets.QPushButton("Set Drive Ratio")
        self.driveRatioButton.setFixedHeight(50)
        self.driveRatioButton.clicked.connect(self.openRatioDialog)
        self.bottomButtonLayout.addWidget(self.driveRatioButton)

        self.rpmCutoffButton = QtWidgets.QPushButton("Set Cutoff RPM")
        self.rpmCutoffButton.clicked.connect(self.openCutOffDialog)
        self.rpmCutoffButton.setFixedHeight(50)
        self.bottomButtonLayout.addWidget(self.rpmCutoffButton)

        self.startStopButton = QtWidgets.QPushButton("Start", self)
        self.startStopButton.clicked.connect(self.toggle_action)
        self.startStopButton.setFixedHeight(50)
        self.startStopButton.setStyleSheet("background-color: green; color: white;")
        self.bottomButtonLayout.addWidget(self.startStopButton)

        # Create a QPushButton with a plus icon and label
        self.new_session_button = QtWidgets.QPushButton()
        self.new_session_button.setIcon(QtGui.QIcon('./images/si--add-square-line.svg'))  # Using a theme-based icon for "New"
        self.new_session_button.setIconSize(QtCore.QSize(30, 30))
        self.new_session_button.setStyleSheet("QPushButton {background-color: rgb(252,202,5);}") 
        self.new_session_button.setFixedSize(48, 48)
        self.new_session_button.setToolTip("New Session")
        self.new_session_button.clicked.connect(self.openSessionDialog)
        self.bottomButtonLayout.addWidget(self.new_session_button)

        self.layout.addLayout(self.bottomButtonLayout)

    def updateData(self):
        
        # Read data
        if self.debug:    
            self.model.setRPM(random.randint(0, 15000)) 
            self.model.setTRQ(random.randint(0, 70)) 
            self.model.setPWR(random.randint(0, 70)) 

            self.model.rpmBuffer.append(self.model.getRPM())
            self.model.trqBuffer.append(self.model.getTRQ())
            self.model.pwrBuffer.append(self.model.getPWR())
        else:
            #TODO Read Serial
            serialData =  self.ser.readline().decode('utf-8').rstrip()

            # Multiply RPM by drive ratio

        # Store data if active
        if self.recording:
            self.csvValues.append((self.model.getRPM(), self.model.getTRQ(), self.model.getPWR()))
            
            # Stop recording if cutoff RPM is reached
            if(self.model.getRPM() > int(self.dynoData['cutOffRPM'])):
                print("Cutoff RPM Reached.")
                self.toggle_action()

            

        

        currentTab = self.tab_widget.currentIndex()

        if currentTab == 0:
        # Tab 1 - Main
            self.tab1.rpmLabel.setText(str(self.model.getRPM()))
            self.tab1.trqLabel.setText(str(self.model.getTRQ()))
            self.tab1.pwrLabel.setText(str(self.model.getPWR()))
            self.tab1.rpmCurve.setData(self.model.rpmBuffer.get())
            self.tab1.pwrCurve.setData(self.model.pwrBuffer.get())
            self.tab1.trqCurve.setData(self.model.trqBuffer.get())

        elif currentTab == 1:
        # Tab 2 - Power 
            self.tab2.rpmLabel.setText(str(self.model.getRPM()))
            self.tab2.trqLabel.setText(str(self.model.getTRQ()))
            self.tab2.pwrLabel.setText(str(self.model.getPWR()))

        elif currentTab == 2:
        # Tab 3 - Output
            self.tab3.rpmCurve.setData(self.model.rpmBuffer.get())
            self.tab3.pwrCurve.setData(self.model.pwrBuffer.get())
            self.tab3.trqCurve.setData(self.model.trqBuffer.get())

        #self.model.layoutChanged.emit()
    
    def openCutOffDialog(self):
        # Create and open the text field dialog
        dialog = cutOffRPMDialog(initial_cutoff=str(self.dynoData['cutOffRPM']), parent=self)
        dialog.exec()  # Run the dialog
        
    def setCutoffFromDialog(self, newVal):
        self.dynoData['cutOffRPM'] = newVal
        
        with open('config.json', 'w') as config:
            json.dump(self.dynoData, config, indent=4)

    def openRatioDialog(self):
        # Create and open the text field dialog
        dialog = driveRatioDialog(initial_ratio=str(self.dynoData['driveRatio']), parent=self)
        dialog.exec()  # Run the dialog
        
    def setRatioFromDialog(self, newVal):
        self.dynoData['driveRatio'] = newVal
        with open('config.json', 'w') as config:
            json.dump(self.dynoData, config, indent=4)
    
    def openSessionDialog(self):
        dialog = sessionDialog(parent=self)
        dialog.exec()  # Run the dialog

    def setSessionFromDialog(self, newVal):
        self.sessionName = newVal

    def toggle_action(self):
        """ Toggle between Start and Stop functionality and change color """
        if self.startStopButton.text() == "Start":
            self.startStopButton.setText("Stop")  # Change the button text to "Stop"
            self.startStopButton.setStyleSheet("background-color: red; color: white;")  # Change button color to red
            self.run_start_function()  # Call the start function
        else:
            self.startStopButton.setText("Start")  # Change the button text to "Start"
            self.startStopButton.setStyleSheet("background-color: green; color: white;")  # Change button color to green
            self.run_stop_function()  # Call the stop function

    def run_start_function(self):
        print("Starting Recording...")
        if self.sessionName == "":
            self.openSessionDialog()
        
        self.recording = True

    def run_stop_function(self):
        print("Stopping recording...")
        self.recording = False
        
        # Format the date and time as a string for filename
        now = datetime.datetime.now()
        fileName = now.strftime("dynoRead_%m-%d_%H-%M-%S.csv")

        if(self.sessionName != ""):
            directory_path = os.path.join('results', self.sessionName)
        else:
            directory_path = os.path.join('results', 'unlabeledSession')

        # Create the directory, including any intermediate directories
        os.makedirs(directory_path, exist_ok=True)

        filePath = os.path.join(directory_path, fileName)

        # Save values to output file
        with open(filePath, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write each tuple to the CSV file
            for row in self.csvValues:
                writer.writerow(row)


        if(self.sessionName != ""):
            show_message(f"Recording saved at %{self.sessionName}/${fileName}.")
        else:
            show_message(f"Recording saved at unlabeledSession/${fileName}.")
        
        # Clear CSV buffer
        self.csvValues = []

class cutOffRPMDialog(QtWidgets.QDialog):
        # Signal to send the text back to the main window
        def __init__(self, initial_cutoff='13500', parent=None):
            super().__init__(parent)

            self.setWindowTitle("Cutoff RPM")
            self.setGeometry(100, 100, 300, 150)
            self.center_dialog()

            # Layout for the dialog
            layout = QtWidgets.QVBoxLayout(self)

            # Create a QLabel to show instructions
            self.label = QtWidgets.QLabel("Cutoff RPM:", self)
            layout.addWidget(self.label)

            # Create a QLineEdit to allow the user to adjust text
            self.cutoff_edit = QtWidgets.QLineEdit(self)
            self.cutoff_edit.setText(initial_cutoff)  # Set the initial text

            int_validator = QtGui.QIntValidator(self)
            self.cutoff_edit.setValidator(int_validator)

            layout.addWidget(self.cutoff_edit)

            # Create a QPushButton to confirm the changes
            self.submit_button = QtWidgets.QPushButton("Submit", self)
            self.submit_button.clicked.connect(self.submit_changes)  # Connect button to the submit function
            layout.addWidget(self.submit_button)

        def submit_changes(self):
            # Retrieve the text entered in the QLineEdit
            new_text = self.cutoff_edit.text()
            
            if new_text:
                self.accept()  # Close the dialog
                self.parent().setCutoffFromDialog(new_text)  # Call a method in the parent (main window) to set the text
            else:
                # If the input is empty or invalid, you can show an error message (optional)
                print("Invalid input. Please enter a valid integer.")

        def center_dialog(self):
            """ Centers the dialog on the main window """
            main_window = self.parent()  # Get the parent (main window)
            if main_window:
                # Get the position and size of the main window
                main_window_rect = main_window.geometry()
                dialog_width = self.width()
                dialog_height = self.height()

                # Calculate the position to center the dialog on the main window
                x = main_window_rect.left() + (main_window_rect.width() - dialog_width) // 2
                y = main_window_rect.top() + (main_window_rect.height() - dialog_height) // 2

                # Move the dialog to the calculated position
                self.move(x, y)

class driveRatioDialog(QtWidgets.QDialog):
        # Signal to send the text back to the main window
        def __init__(self, initial_ratio='1', parent=None):
            super().__init__(parent)

            self.setWindowTitle("Drive Ratio")
            self.setGeometry(100, 100, 300, 150)
            self.center_dialog()

            # Layout for the dialog
            layout = QtWidgets.QVBoxLayout(self)

            # Create a QLabel to show instructions
            self.label = QtWidgets.QLabel("Drive Ratio:", self)
            layout.addWidget(self.label)

            # Create a QLineEdit to allow the user to adjust text
            self.ratio_edit = QtWidgets.QLineEdit(self)
            self.ratio_edit.setText(initial_ratio)  # Set the initial text

            int_validator = QtGui.QDoubleValidator(self)
            self.ratio_edit.setValidator(int_validator)

            layout.addWidget(self.ratio_edit)

            # Create a QPushButton to confirm the changes
            self.submit_button = QtWidgets.QPushButton("Submit", self)
            self.submit_button.clicked.connect(self.submit_changes)  # Connect button to the submit function
            layout.addWidget(self.submit_button)

        def submit_changes(self):
            # Retrieve the text entered in the QLineEdit
            new_text = self.ratio_edit.text()
            
            if new_text:
                self.accept()  # Close the dialog
                self.parent().setRatioFromDialog(new_text)  # Call a method in the parent (main window) to set the text
            else:
                # If the input is empty or invalid, you can show an error message (optional)
                print("Invalid input. Please enter a valid float.")

        def center_dialog(self):
            """ Centers the dialog on the main window """
            main_window = self.parent()  # Get the parent (main window)
            if main_window:
                # Get the position and size of the main window
                main_window_rect = main_window.geometry()
                dialog_width = self.width()
                dialog_height = self.height()

                # Calculate the position to center the dialog on the main window
                x = main_window_rect.left() + (main_window_rect.width() - dialog_width) // 2
                y = main_window_rect.top() + (main_window_rect.height() - dialog_height) // 2

                # Move the dialog to the calculated position
                self.move(x, y)

class sessionDialog(QtWidgets.QDialog):
        # Signal to send the text back to the main window
        def __init__(self, parent=None):
            super().__init__(parent)

            self.setWindowTitle("New Session")
            self.setGeometry(100, 100, 300, 150)
            self.center_dialog()

            # Layout for the dialog
            layout = QtWidgets.QVBoxLayout(self)

            # Create a QLabel to show instructions
            self.label = QtWidgets.QLabel("Enter a session name:", self)
            layout.addWidget(self.label)

            # Create a QLineEdit to allow the user to adjust text
            self.session_edit = QtWidgets.QLineEdit(self)

            dir_validator = DirectoryValidator(self)
            self.session_edit.setValidator(dir_validator)

            layout.addWidget(self.session_edit)

            # Create a QPushButton to confirm the changes
            self.submit_button = QtWidgets.QPushButton("Submit", self)
            self.submit_button.clicked.connect(self.submit_changes)  # Connect button to the submit function
            layout.addWidget(self.submit_button)

        def submit_changes(self):
            # Retrieve the text entered in the QLineEdit
            new_text = self.session_edit.text()
            
            if new_text:
                self.accept()  # Close the dialog
                self.parent().setSessionFromDialog(new_text)  # Call a method in the parent (main window) to set the text
            else:
                # If the input is empty or invalid, you can show an error message (optional)
                print("Invalid input. Please enter a valid float.")

        def center_dialog(self):
            """ Centers the dialog on the main window """
            main_window = self.parent()  # Get the parent (main window)
            if main_window:
                # Get the position and size of the main window
                main_window_rect = main_window.geometry()
                dialog_width = self.width()
                dialog_height = self.height()

                # Calculate the position to center the dialog on the main window
                x = main_window_rect.left() + (main_window_rect.width() - dialog_width) // 2
                y = main_window_rect.top() + (main_window_rect.height() - dialog_height) // 2

                # Move the dialog to the calculated position
                self.move(x, y)

class DirectoryValidator(QtGui.QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input_str, pos):
        """
        Check if the input string is a valid directory path.
        Returns QValidator.Acceptable, QValidator.Intermediate, or QValidator.Invalid.
        """
        # Check for invalid characters in the path
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        if any(char in input_str for char in invalid_chars):
            return QtGui.QValidator.Invalid, input_str, pos

        return QtGui.QValidator.Acceptable, input_str, pos
        
class ColorLabelWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 300)
        self.setMaximumWidth(750)

        # Define a list of color names
        self.colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'magenta']

        # Create a layout for the widget
        self.main_layout = QtWidgets.QHBoxLayout(self)

         # Create two vertical layouts (one for each column)
        left_column_layout = QtWidgets.QVBoxLayout()
        right_column_layout = QtWidgets.QVBoxLayout()

        labelStyle = """
            background-color: grey; 
            border: 2px solid black;
            padding: 10px;
            font-size: 14px;
            border-radius: 5px;
            """

        self.label1 = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()
        self.label3 = QtWidgets.QLabel()
        self.label4 = QtWidgets.QLabel()
        self.label5 = QtWidgets.QLabel()
        self.label6 = QtWidgets.QLabel()
        self.label7 = QtWidgets.QLabel()
        self.label8 = QtWidgets.QLabel()

        self.labels = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6, self.label7, self.label8]

        # Create labels and colored square icons
        for idx, (color, label) in enumerate(zip(self.colors, self.labels)):
            # Create the color square as a QLabel with a colored background
            color_icon = self.create_color_icon(color)

            # Create the label with text
            self.labels[idx].setStyleSheet(labelStyle)

            row_layout = QtWidgets.QHBoxLayout()
            row_layout.addWidget(color_icon)
            row_layout.addWidget(self.labels[idx])

            if idx < 4:
                left_column_layout.addLayout(row_layout)
            else:
                right_column_layout.addLayout(row_layout)

            # Horizontal layout for each label and colored square

            # Add the row layout to the main layout
        
        self.main_layout.addLayout(left_column_layout)
        self.main_layout.addLayout(right_column_layout)

        self.setLayout(self.main_layout)

    def updateLabels(self, labels):
        
        while(len(labels) < 8):
            labels.append("")

        for idx, label in enumerate(labels):
            if(label != ""):
                fileName = label.rsplit(sep="/")[-2] + '/' + label.rsplit(sep="/")[-1]
                
                # Calculating max torque and power for each file and adding that to the label
                try:
                    
                    data = []
                    displayData = ''
                    
                    with open(label, mode='r', newline='', encoding='utf-8') as file:
                        csv_reader = csv.reader(file)  # Create a CSV reader object

                        # Iterate through the rows in the CSV
                        for row in csv_reader:
                            data.append((round(float(row[0]),2), round(float(row[1]),2),round(float(row[2]),2)))

                        pwrSortedData = sorted(data, key=lambda x: x[0])
                        trqSortedData = sorted(data, key=lambda x: x[0])
                    
                        displayData = fileName + "\nTRQ: 123 @ 5500" + "\nPWR: 123 @ 5500"
                
                    self.labels[idx].setText(displayData)

                except:
                    pass

            else:
                self.labels[idx].setText("")

    def create_color_icon(self, color_name):
        
        """Create a square icon with the specified color."""
        pixmap = QtGui.QPixmap(40, 40)  # 40x40 square icon
        pixmap.fill(QtGui.QColor(color_name))  # Fill the pixmap with the color
        color_icon = QtWidgets.QLabel(self)  # Create a QLabel to hold the pixmap
        color_icon.setPixmap(pixmap)  # Set the pixmap (colored square) to the label
        color_icon.setFixedSize(QtCore.QSize(40, 40))  # Set a fixed size for the icon
        return color_icon

class BoxWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Box Widget")
        self.setGeometry(200, 200, 300, 200)

        # Set a grey background and small border around the entire widget
        style = """
                background-color: grey;
                border: 2px solid black;
                border-radius: 5px;
        """

        # Create labels for File, Max Power, and Max Torque
        self.max_power_label = QtWidgets.QLabel("Max Power:")
        self.max_power_label.setStyleSheet(style)

        self.max_torque_label = QtWidgets.QLabel("Max Torque:")
        self.max_torque_label.setStyleSheet(style)

        # Create a QGroupBox to enclose the entire layout in a box
        group_box = QtWidgets.QGroupBox()
        group_box.setTitle("File: ")  # Optional title for the box
        group_box.setStyleSheet("""
            QGroupBox {
                border: 2px solid black;
                border-radius: 5px;
                padding: 10px;
                background-color: grey;
            }
        """)

        # Layout for the labels and values
        layout = QtWidgets.QVBoxLayout()
        max_power_layout = QtWidgets.QHBoxLayout()
        max_power_layout.addWidget(self.max_power_label)

        max_torque_layout = QtWidgets.QHBoxLayout()
        max_torque_layout.addWidget(self.max_torque_label)

        layout.addLayout(max_power_layout)
        layout.addLayout(max_torque_layout)

        # Set the layout for the QGroupBox
        group_box.setLayout(layout)

        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(group_box)

        # Set the main layout for the widget
        self.setLayout(main_layout)

def show_message(message):
    # Create the QMessageBox with a simple message
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)  # Information icon
    msg.setText(message)
    msg.setWindowTitle("Notification")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

    # Show the message box
    msg.exec()

    # Set a timer to close the message box after 3 seconds (3000 milliseconds)
    QtCore.QTimer.singleShot(500, msg.close)  # Close the message box after 3 seconds
