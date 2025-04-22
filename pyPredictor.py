from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit
#from PyQt5 import uic
from pyPredictorUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('pyPredictorUI.ui',self)
        self.setupUi(self)
        self.btnLoadTrain.clicked.connect(self.btnLoadTrainClick)
        self.btnClearUser.clicked.connect(self.btnClearUserClick)
        self.listWidget.itemClicked.connect(self.itemClick)
        self.editUser.textChanged.connect(self.editUserChanged)
        self.freqTable = list()

    def btnClearUserClick(self):
        self.editUser.clear()

    def editUserChanged(self):
        words = self.editUser.toPlainText().split()
        if (len(words) > 0) and (len(self.freqTable) > 0):
            lastWord = words[-1].lower()
            self.listWidget.clear()
            for pair in self.freqTable:
                if pair[0].find(lastWord) == 0:
                    self.listWidget.addItem(pair[0] + ' ' + pair[1])

    def btnLoadTrainClick(self):
        filename = QFileDialog.getOpenFileName(self, 'Выбрать текст', '')[0]
        if filename != '':
            file = open(filename, "r")
            content = file.read()
            file.close()
            self.editTrain.setText(content)
            syms = ".,?!~`\'\":\\;{}[]|@#%^&*()-+=_<>/0123456789"
            content = content.lower()
            for ch in syms:
                content = content.replace(ch, " ")
            words = content.split()
            pairs = list()
            for k in range(len(words) - 1):
                pairs.append([words[k], words[k + 1], 0])
            pairs = sorted(pairs, key=lambda x: (x[0], x[1]))
            if len(pairs) > 0:
                self.freqTable.clear()
                self.freqTable.append(pairs[0])
                i = 0
                for pair in pairs:
                    if self.freqTable[i][1] == pair[1]:
                        self.freqTable[i][2] = self.freqTable[i][2] + 1
                    else:
                        self.freqTable.append(pair)
                        i = i + 1
                        self.freqTable[i][2] = 1
                self.freqTable = sorted(self.freqTable, key=lambda x: (x[0], -x[2]))

    def itemClick(self):
        predictWord = self.listWidget.currentItem().text()
        words = self.editUser.toPlainText().split()
        if len(words) > 0:
            words = words[:-1]
        words.append(predictWord)
        self.editUser.setText(' '.join(words))


app = QApplication([])
mainWindow = MainWindow()
mainWindow.show()
app.exec()
