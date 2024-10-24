from home import *

if __name__ == "__main__":
    # Prints the Qt version used to compile PySide6
    print(QtCore.__version__)

    app = QtWidgets.QApplication(sys.argv)
    tabWidgetApp = TabWidgetApp()

    tabWidgetApp.resize(1200, 700)

    tabWidgetApp.show()
    sys.exit(app.exec())

    #widget = homeWidget()
    
    #widget.show()

    