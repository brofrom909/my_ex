from PySide2 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Dialog

#Create apppilcation
app = QtWidgets.QApplication(sys.argv)


#Create from and init UI
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


#Hook ligoc
def bp():
    ui.lineEdit.setText("Hello world")


ui.pushButton_10.clicked.connect(bp)
#run main loop
sys.exit(app.exec_())

