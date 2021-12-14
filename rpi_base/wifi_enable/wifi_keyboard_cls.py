from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer


#get the UI from here
from wifi_keyboard_ui import Ui_KeyboardDialog


########################
# KeyboardDialog Class #
########################
class KeyboardDialog(QDialog):

    def __init__(self, config_str, first_str):
        super(KeyboardDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_KeyboardDialog()
        self.ui.setupUi(self)

        # get the close event and specials buttons connect
        self.ui.cancelButton.clicked.connect(self.CancelButton)
        self.ui.enterButton.clicked.connect(self.AcceptButton)
        self.ui.backButton.clicked.connect(self.BackSpaceButton)
        self.ui.spaceButton.clicked.connect(self.SpaceButton)
        self.ui.shiftshortButton.clicked.connect(self.ShiftButton)
        self.ui.shiftlongButton.clicked.connect(self.ShiftButton)
        self.ui.symbolsButton.clicked.connect(self.SymbolsButton)
        
        # connect common buttons
        self.ui.Button_1.clicked.connect(self.CommonButtons)
        self.ui.Button_2.clicked.connect(self.CommonButtons)
        self.ui.Button_3.clicked.connect(self.CommonButtons)
        self.ui.Button_4.clicked.connect(self.CommonButtons)
        self.ui.Button_5.clicked.connect(self.CommonButtons)
        self.ui.Button_6.clicked.connect(self.CommonButtons)
        self.ui.Button_7.clicked.connect(self.CommonButtons)
        self.ui.Button_8.clicked.connect(self.CommonButtons)
        self.ui.Button_9.clicked.connect(self.CommonButtons)
        self.ui.Button_10.clicked.connect(self.CommonButtons)
        self.ui.Button_11.clicked.connect(self.CommonButtons)
        self.ui.Button_12.clicked.connect(self.CommonButtons)
        self.ui.Button_13.clicked.connect(self.CommonButtons)
        self.ui.Button_14.clicked.connect(self.CommonButtons)
        self.ui.Button_15.clicked.connect(self.CommonButtons)
        self.ui.Button_16.clicked.connect(self.CommonButtons)
        self.ui.Button_17.clicked.connect(self.CommonButtons)
        self.ui.Button_18.clicked.connect(self.CommonButtons)
        self.ui.Button_19.clicked.connect(self.CommonButtons)
        self.ui.Button_20.clicked.connect(self.CommonButtons)
        self.ui.Button_21.clicked.connect(self.CommonButtons)
        self.ui.Button_22.clicked.connect(self.CommonButtons)
        self.ui.Button_23.clicked.connect(self.CommonButtons)
        self.ui.Button_24.clicked.connect(self.CommonButtons)
        self.ui.Button_25.clicked.connect(self.CommonButtons)
        self.ui.Button_26.clicked.connect(self.CommonButtons)
        self.ui.Button_27.clicked.connect(self.CommonButtons)

        self.ui.configLabel.setText(config_str)
        self.ui.configEdit.setText(first_str)
        self.first_str = first_str
        self.answer = first_str

        self.capsonce = False
        self.symbols = False
        self.othersymbols = False        


    def CancelButton (self):
        self.answer = self.first_str
        self.accept()

        
    def AcceptButton (self):
        self.answer = self.ui.configEdit.text()
        self.accept()


    def BackSpaceButton (self):
        actual_str = self.ui.configEdit.text()
        if len(actual_str) > 0:
            self.ui.configEdit.setText(actual_str[:-1])


    def SpaceButton (self):
        last_str = self.ui.configEdit.text()
        self.ui.configEdit.setText(last_str + ' ')

            
    def CommonButtons (self):
        sender = self.sender()
        last_str = self.ui.configEdit.text()
        ## ampersand correction
        sender_str = sender.text()
        if sender_str == '&&':
            self.ui.configEdit.setText(last_str + '&')
        else:
            self.ui.configEdit.setText(last_str + sender_str)

        if self.capsonce:
            self.ToLower()
            self.capsonce = False


    def ShiftButton (self):
        sender = self.sender()

        if self.symbols:
            if self.othersymbols:
                self.othersymbols = False
                self.ToSymbols()
            else:
                self.othersymbols = True
                self.ToOtherSymbols()
                
        else:
            if sender.objectName() == 'shiftlongButton':
                self.ToUpper()
            else:
                if self.capsonce:
                    self.ToLower()
                    self.capsonce = False
                else:
                    self.capsonce = True
                    self.ToUpper()


    def SymbolsButton (self):
        if self.symbols:
            self.symbols = False
            self.othersymbols = False
            self.ToChars()
        else:
            self.symbols = True
            self.ToSymbols()
            
        
    def ToUpper (self):
        self.ui.Button_1.setText(self.ui.Button_1.text().upper())
        self.ui.Button_2.setText(self.ui.Button_2.text().upper())
        self.ui.Button_3.setText(self.ui.Button_3.text().upper())
        self.ui.Button_4.setText(self.ui.Button_4.text().upper())
        self.ui.Button_5.setText(self.ui.Button_5.text().upper())
        self.ui.Button_6.setText(self.ui.Button_6.text().upper())
        self.ui.Button_7.setText(self.ui.Button_7.text().upper())
        self.ui.Button_8.setText(self.ui.Button_8.text().upper())
        self.ui.Button_9.setText(self.ui.Button_9.text().upper())
        self.ui.Button_10.setText(self.ui.Button_10.text().upper())
        self.ui.Button_11.setText(self.ui.Button_11.text().upper())
        self.ui.Button_12.setText(self.ui.Button_12.text().upper())
        self.ui.Button_13.setText(self.ui.Button_13.text().upper())
        self.ui.Button_14.setText(self.ui.Button_14.text().upper())
        self.ui.Button_15.setText(self.ui.Button_15.text().upper())
        self.ui.Button_16.setText(self.ui.Button_16.text().upper())
        self.ui.Button_17.setText(self.ui.Button_17.text().upper())
        self.ui.Button_18.setText(self.ui.Button_18.text().upper())
        self.ui.Button_19.setText(self.ui.Button_19.text().upper())
        self.ui.Button_20.setText(self.ui.Button_20.text().upper())
        self.ui.Button_21.setText(self.ui.Button_21.text().upper())
        self.ui.Button_22.setText(self.ui.Button_22.text().upper())
        self.ui.Button_23.setText(self.ui.Button_23.text().upper())
        self.ui.Button_24.setText(self.ui.Button_24.text().upper())
        self.ui.Button_25.setText(self.ui.Button_25.text().upper())
        self.ui.Button_26.setText(self.ui.Button_26.text().upper())
        self.ui.Button_27.setText(self.ui.Button_27.text().upper())
        
        
    def ToLower (self):
        self.ui.Button_1.setText(self.ui.Button_1.text().lower())
        self.ui.Button_2.setText(self.ui.Button_2.text().lower())
        self.ui.Button_3.setText(self.ui.Button_3.text().lower())
        self.ui.Button_4.setText(self.ui.Button_4.text().lower())
        self.ui.Button_5.setText(self.ui.Button_5.text().lower())
        self.ui.Button_6.setText(self.ui.Button_6.text().lower())
        self.ui.Button_7.setText(self.ui.Button_7.text().lower())
        self.ui.Button_8.setText(self.ui.Button_8.text().lower())
        self.ui.Button_9.setText(self.ui.Button_9.text().lower())
        self.ui.Button_10.setText(self.ui.Button_10.text().lower())
        self.ui.Button_11.setText(self.ui.Button_11.text().lower())
        self.ui.Button_12.setText(self.ui.Button_12.text().lower())
        self.ui.Button_13.setText(self.ui.Button_13.text().lower())
        self.ui.Button_14.setText(self.ui.Button_14.text().lower())
        self.ui.Button_15.setText(self.ui.Button_15.text().lower())
        self.ui.Button_16.setText(self.ui.Button_16.text().lower())
        self.ui.Button_17.setText(self.ui.Button_17.text().lower())
        self.ui.Button_18.setText(self.ui.Button_18.text().lower())
        self.ui.Button_19.setText(self.ui.Button_19.text().lower())
        self.ui.Button_20.setText(self.ui.Button_20.text().lower())
        self.ui.Button_21.setText(self.ui.Button_21.text().lower())
        self.ui.Button_22.setText(self.ui.Button_22.text().lower())
        self.ui.Button_23.setText(self.ui.Button_23.text().lower())
        self.ui.Button_24.setText(self.ui.Button_24.text().lower())
        self.ui.Button_25.setText(self.ui.Button_25.text().lower())
        self.ui.Button_26.setText(self.ui.Button_26.text().lower())
        self.ui.Button_27.setText(self.ui.Button_27.text().lower())


    def ToSymbols (self):
        self.ui.Button_1.setText('1')
        self.ui.Button_2.setText('2')
        self.ui.Button_3.setText('3')
        self.ui.Button_4.setText('4')
        self.ui.Button_5.setText('5')
        self.ui.Button_6.setText('6')
        self.ui.Button_7.setText('7')
        self.ui.Button_8.setText('8')
        self.ui.Button_9.setText('9')
        self.ui.Button_10.setText('0')
        self.ui.Button_11.setText('@')
        self.ui.Button_12.setText('#')
        self.ui.Button_13.setText('$')
        self.ui.Button_14.setText('_')
        self.ui.Button_15.setText('&&')
        self.ui.Button_16.setText('-')
        self.ui.Button_17.setText('+')
        self.ui.Button_18.setText('(')
        self.ui.Button_19.setText(')')
        self.ui.Button_20.setText('/')
        self.ui.Button_21.setText('*')
        self.ui.Button_22.setText('"')
        self.ui.Button_23.setText("'")
        self.ui.Button_24.setText(':')
        self.ui.Button_25.setText(';')
        self.ui.Button_26.setText('!')
        self.ui.Button_27.setText('?')


    def ToOtherSymbols (self):
        # self.ui.Button_1.setText('1')
        # self.ui.Button_2.setText('2')
        # self.ui.Button_3.setText('3')
        # self.ui.Button_4.setText('4')
        # self.ui.Button_5.setText('5')
        # self.ui.Button_6.setText('6')
        # self.ui.Button_7.setText('7')
        # self.ui.Button_8.setText('8')
        # self.ui.Button_9.setText('9')
        # self.ui.Button_10.setText('0')
        self.ui.Button_11.setText('~')
        self.ui.Button_12.setText('%')
        self.ui.Button_13.setText('^')
        self.ui.Button_14.setText('|')
        self.ui.Button_15.setText('[')
        self.ui.Button_16.setText(']')
        self.ui.Button_17.setText('<')
        self.ui.Button_18.setText('>')
        self.ui.Button_19.setText('{')
        self.ui.Button_20.setText('}')
        self.ui.Button_21.setText('\\')
        self.ui.Button_22.setText('')
        self.ui.Button_23.setText('')
        self.ui.Button_24.setText('')
        self.ui.Button_25.setText('')
        self.ui.Button_26.setText('')
        self.ui.Button_27.setText('')


    def ToChars (self):
        self.ui.Button_1.setText('q')
        self.ui.Button_2.setText('w')
        self.ui.Button_3.setText('e')
        self.ui.Button_4.setText('r')
        self.ui.Button_5.setText('t')
        self.ui.Button_6.setText('y')
        self.ui.Button_7.setText('u')
        self.ui.Button_8.setText('i')
        self.ui.Button_9.setText('o')
        self.ui.Button_10.setText('p')
        self.ui.Button_11.setText('a')
        self.ui.Button_12.setText('s')
        self.ui.Button_13.setText('d')
        self.ui.Button_14.setText('f')
        self.ui.Button_15.setText('g')
        self.ui.Button_16.setText('h')
        self.ui.Button_17.setText('j')
        self.ui.Button_18.setText('k')
        self.ui.Button_19.setText('l')
        self.ui.Button_20.setText('z')
        self.ui.Button_21.setText('x')
        self.ui.Button_22.setText('c')
        self.ui.Button_23.setText("v")
        self.ui.Button_24.setText('b')
        self.ui.Button_25.setText('n')
        self.ui.Button_26.setText('m')
        self.ui.Button_27.setText('.')

        
### end of file ###
