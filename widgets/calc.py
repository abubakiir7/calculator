from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(width, height)
        self.calc_list = ""
        self.digits = ""

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.my_layout = QVBoxLayout()
        self.my_layout.setContentsMargins(0, 0, 0, 0)
        self.result_label = QLabel("0")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.result_label.setFixedHeight(60)
        self.result_label.setStyleSheet("""
            font-size: 50px;
            margin-top: 10px;
        """)
        self.my_layout.addWidget(self.result_label)
        self.setupButtons()
        self.central_widget.setLayout(self.my_layout)

    def keyPressEvent(self, event):
        d = event.key()
        if 41 < d < 58 or d == 16777220 or d == 16777219:
            self.onButtonClicked(event.key())

    def setupButtons(self):
        self.buttons_layout = QGridLayout()
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_layout.setGeometry(QRect(1, 50, 238, 254))
        self.buttons = [
            ["AC", "+/-", "%", "÷"],
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ",", "="]
        ]

        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                button = QPushButton(self.buttons[i][j])
                button.setStyleSheet("""    
                    height: 63.5%;
                    width: 59.5%;
                """)
                self.buttons_layout.addWidget(button, i, j)
                button.clicked.connect(self.onButtonClicked)

        self.my_layout.addLayout(self.buttons_layout)

    def clicking_keyboard(self, event):
        key = event.key()


    def onButtonClicked(self, num="None"):
        button = self.sender()
        if not(num):
            data = button.text() 
            # print('kirdi')
        else:
            if int(num) == 16777220:
                data = '='
            elif int(num) == 16777219:
                data = 'del'
            else:
                data = chr(int(num))

        if data != "AC" and data != '=' and data != 'del':
            if data == 'x':
                self.calc_list += "*"
            elif data == '÷':
                self.calc_list += "/"
            elif data == ',':
                self.calc_list += '.'
            else:
                self.calc_list += str(data)
            if data.isdigit() or data == ',':
                self.digits += str(data)
                self.result_label.setText(f"{self.digits}")
            else:
                self.digits = ""
                self.result_label.setText("0")
        elif data == "=":
            try:
                res = eval(self.calc_list)
                self.result_label.setText(f"{str(res)}")
                self.calc_list = str(res)
                self.digits = str(res)
            except:
                pass
        elif data == "AC":
            self.calc_list = ""
            self.digits = ""
            self.result_label.setText("0")
        elif data == 'del' and len(self.digits) > 0:
            if len(self.digits) == 1:
                self.digits = self.digits[:len(self.digits) - 1]
                self.calc_list = self.calc_list[:len(self.calc_list) - 1]
                self.result_label.setText("0")
            else:
                self.digits = self.digits[:len(self.digits) - 1]
                self.calc_list = self.calc_list[:len(self.calc_list) - 1]
                print(self.calc_list)
                self.result_label.setText(f"{self.digits}")



                