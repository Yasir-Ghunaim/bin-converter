#!/usr/bin/python

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):      

        #self.btn = QtGui.QPushButton('Dialog', self)
        #self.btn.move(20, 20)
        #self.btn.clicked.connect(self.showDialog)
        
        self.inputTextEdit = QtGui.QTextEdit(self)
        self.inputTextEdit.move(10, 10)
        
        self.outputTextEdit = QtGui.QTextEdit(self)
        self.outputTextEdit.move(310, 10)
        
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Input dialog')
        self.show()
        
    #def showDialog(self):
        
     #   text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
      #      'Enter your name:')
        
       # if ok:
        #    self.le.setText(str(text))
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
