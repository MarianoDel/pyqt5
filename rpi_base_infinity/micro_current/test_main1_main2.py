from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
import sys

class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window 1")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("This is Main Window 1")
        layout.addWidget(self.label)

        self.open_button = QPushButton("Open Main Window 2")
        self.open_button.clicked.connect(self.open_main_window2)
        layout.addWidget(self.open_button)

        self.setCentralWidget(central_widget)

    def open_main_window2(self):
        self.second_window = MainWindow2() # Create an instance of the second window
        self.second_window.show()
        # Optionally, hide the current window:
        # self.hide()

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window 2")
        self.setGeometry(200, 200, 400, 300)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("This is Main Window 2")
        layout.addWidget(self.label)

        self.close_button = QPushButton("Close Main Window 2")
        self.close_button.clicked.connect(self.close) # Close this window
        layout.addWidget(self.close_button)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window1 = MainWindow1()
    main_window1.show()
    sys.exit(app.exec_())        
