from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTextEdit, QErrorMessage
from PyQt5.QtCore import QTimer
import time
import sys
from fgGroupPoster import fgGroupPoster

class Ui_AnonForm(object):
   def setupUi(self, AnonForm):
      AnonForm.setObjectName("AnonForm")
      maxWith = 500
      maxHeight = 500
      AnonForm.setFixedSize(maxWith, maxHeight)
     
      font = QtGui.QFont()
      font.setBold(True)
      font.setWeight(75)
      #----------------------{ x, y, W, H}--
      fbAccountLable       = [20,10,maxWith,20]
      IdAccountLable       = [fbAccountLable[0], fbAccountLable[1] + fbAccountLable[3], 30, 20]
      fbAccount            = [fbAccountLable[0] + IdAccountLable[2], fbAccountLable[1] + fbAccountLable[3], 150, 20]
      pwAccountLable       = [fbAccount[0] + fbAccount[2], fbAccountLable[1] + fbAccountLable[3], 90, 20]
      passwordAccount      = [pwAccountLable[0] + pwAccountLable[2], fbAccountLable[1] + fbAccountLable[3], 150, 20]
      Link1Lable           = [fbAccountLable[0], IdAccountLable[1] + IdAccountLable[3], maxWith, 20]
      link1                = [fbAccountLable[0], Link1Lable[1] + Link1Lable[3], maxWith-40, 20]
      Link2Lable           = [fbAccountLable[0], link1[1] + link1[3], maxWith, 20]
      link2                = [fbAccountLable[0], Link2Lable[1] + Link2Lable[3], maxWith-40, 20]
      Link3Lable           = [fbAccountLable[0], link2[1] + link2[3], maxWith, 20]
      link3                = [fbAccountLable[0], Link3Lable[1] + Link3Lable[3], maxWith-40, 20]
      Link4Lable           = [fbAccountLable[0], link3[1] + link3[3], maxWith, 20]
      link4                = [fbAccountLable[0], Link4Lable[1] + Link4Lable[3], maxWith-40, 20]
      Link5Lable           = [fbAccountLable[0], link4[1] + link4[3], maxWith, 20]
      link5                = [fbAccountLable[0], Link5Lable[1] + Link5Lable[3], maxWith-40, 20]
      messAreaLable        = [fbAccountLable[0], link5[1] + link5[3], maxWith-40, 20]
      AnonGoBtn            = [fbAccountLable[0], maxHeight - 40, maxWith-40, 20]
      messArea             = [fbAccountLable[0], messAreaLable[1] + messAreaLable[3], maxWith-40, AnonGoBtn[1] - messAreaLable[1] - messAreaLable[3]]
      #-------------------------------
      self.fbAccountLable = QtWidgets.QLabel(AnonForm)
      self.fbAccountLable.setGeometry(QtCore.QRect(fbAccountLable[0], fbAccountLable[1], fbAccountLable[2], fbAccountLable[3]))
      self.fbAccountLable.setFont(font)
      self.fbAccountLable.setTextFormat(QtCore.Qt.RichText)
      self.fbAccountLable.setAlignment(QtCore.Qt.AlignLeft)
      self.fbAccountLable.setObjectName("fbAccountLable")

      self.IdAccountLable = QtWidgets.QLabel(AnonForm)
      self.IdAccountLable.setGeometry(QtCore.QRect(IdAccountLable[0], IdAccountLable[1], IdAccountLable[2], IdAccountLable[3]))
      self.IdAccountLable.setFont(font)
      self.IdAccountLable.setTextFormat(QtCore.Qt.RichText)
      self.IdAccountLable.setAlignment(QtCore.Qt.AlignLeft)
      self.IdAccountLable.setObjectName("IdAccountLable")

      self.fbAccount = QtWidgets.QLineEdit(AnonForm)
      self.fbAccount.setGeometry(QtCore.QRect(fbAccount[0], fbAccount[1], fbAccount[2], fbAccount[3]))
      self.fbAccount.setFont(font)
      self.fbAccount.setAlignment(QtCore.Qt.AlignLeft)
      self.fbAccount.setObjectName("fbAccount")

      self.pwAccountLable = QtWidgets.QLabel(AnonForm)
      self.pwAccountLable.setGeometry(QtCore.QRect(pwAccountLable[0], pwAccountLable[1], pwAccountLable[2], pwAccountLable[3]))
      self.pwAccountLable.setFont(font)
      self.pwAccountLable.setTextFormat(QtCore.Qt.RichText)
      self.pwAccountLable.setAlignment(QtCore.Qt.AlignCenter)
      self.pwAccountLable.setObjectName("pwAccountLable")

      self.passwordAccount = QtWidgets.QLineEdit(AnonForm)
      self.passwordAccount.setGeometry(QtCore.QRect(passwordAccount[0], passwordAccount[1], passwordAccount[2], passwordAccount[3]))
      self.passwordAccount.setFont(font)
      self.passwordAccount.setEchoMode(QtWidgets.QLineEdit.Password)
      self.passwordAccount.setAlignment(QtCore.Qt.AlignLeft)
      self.passwordAccount.setObjectName("passwordAccount")
	  
      self.Link1Lable = QtWidgets.QLabel(AnonForm)
      self.Link1Lable.setGeometry(QtCore.QRect(Link1Lable[0], Link1Lable[1], Link1Lable[2], Link1Lable[3]))
      self.Link1Lable.setFont(font)
      self.Link1Lable.setTextFormat(QtCore.Qt.RichText)
      self.Link1Lable.setAlignment(QtCore.Qt.AlignLeft)
      self.Link1Lable.setObjectName("Link1Lable")

      self.link1 = QtWidgets.QLineEdit(AnonForm)
      self.link1.setGeometry(QtCore.QRect(link1[0], link1[1], link1[2], link1[3]))
      self.link1.setFont(font)
      self.link1.setAlignment(QtCore.Qt.AlignLeft)
      self.link1.setObjectName("link1")
	  
      self.Link2Lable = QtWidgets.QLabel(AnonForm)
      self.Link2Lable.setGeometry(QtCore.QRect(Link2Lable[0], Link2Lable[1], Link2Lable[2], Link2Lable[3]))
      self.Link2Lable.setFont(font)
      self.Link2Lable.setTextFormat(QtCore.Qt.RichText)
      self.Link2Lable.setAlignment(QtCore.Qt.AlignLeft)
      self.Link2Lable.setObjectName("Link2Lable")

      self.link2 = QtWidgets.QLineEdit(AnonForm)
      self.link2.setGeometry(QtCore.QRect(link2[0], link2[1], link2[2], link2[3]))
      self.link2.setFont(font)
      self.link2.setAlignment(QtCore.Qt.AlignLeft)
      self.link2.setObjectName("link2")
	  
      self.Link3Lable = QtWidgets.QLabel(AnonForm)
      self.Link3Lable.setGeometry(QtCore.QRect(Link3Lable[0], Link3Lable[1], Link3Lable[2], Link3Lable[3]))
      self.Link3Lable.setFont(font)
      self.Link3Lable.setTextFormat(QtCore.Qt.RichText)
      self.Link3Lable.setAlignment(QtCore.Qt.AlignLeft)
      self.Link3Lable.setObjectName("Link3Lable")

      self.link3 = QtWidgets.QLineEdit(AnonForm)
      self.link3.setGeometry(QtCore.QRect(link3[0], link3[1], link3[2], link3[3]))
      self.link3.setFont(font)
      self.link3.setAlignment(QtCore.Qt.AlignLeft)
      self.link3.setObjectName("link3")
	  
      self.Link4Lable = QtWidgets.QLabel(AnonForm)
      self.Link4Lable.setGeometry(QtCore.QRect(Link4Lable[0], Link4Lable[1], Link4Lable[2], Link4Lable[3]))
      self.Link4Lable.setFont(font)
      self.Link4Lable.setTextFormat(QtCore.Qt.RichText)
      self.Link4Lable.setAlignment(QtCore.Qt.AlignLeft)
      self.Link4Lable.setObjectName("Link4Lable")

      self.link4 = QtWidgets.QLineEdit(AnonForm)
      self.link4.setGeometry(QtCore.QRect(link4[0], link4[1], link4[2], link4[3]))
      self.link4.setFont(font)
      self.link4.setAlignment(QtCore.Qt.AlignLeft)
      self.link4.setObjectName("link4")
	  
      self.Link5Lable = QtWidgets.QLabel(AnonForm)
      self.Link5Lable.setGeometry(QtCore.QRect(Link5Lable[0], Link5Lable[1], Link5Lable[2], Link5Lable[3]))
      self.Link5Lable.setFont(font)
      self.Link5Lable.setTextFormat(QtCore.Qt.RichText)
      self.Link5Lable.setAlignment(QtCore.Qt.AlignLeft)
      self.Link5Lable.setObjectName("Link5Lable")

      self.link5 = QtWidgets.QLineEdit(AnonForm)
      self.link5.setGeometry(QtCore.QRect(link5[0], link5[1], link5[2], link5[3]))
      self.link5.setFont(font)
      self.link5.setAlignment(QtCore.Qt.AlignLeft)
      self.link5.setObjectName("link5")

      self.messAreaLable = QtWidgets.QLabel(AnonForm)
      self.messAreaLable.setGeometry(QtCore.QRect(messAreaLable[0], messAreaLable[1], messAreaLable[2], messAreaLable[3]))
      self.messAreaLable.setFont(font)
      self.messAreaLable.setTextFormat(QtCore.Qt.RichText)
      self.messAreaLable.setAlignment(QtCore.Qt.AlignCenter)
      self.messAreaLable.setObjectName("messAreaLable")
      self.messAreaLable.setStyleSheet("QLabel#messAreaLable {color: red}")

      self.messArea = QtWidgets.QTextEdit(AnonForm)
      self.messArea.setGeometry(QtCore.QRect(messArea[0], messArea[1], messArea[2], messArea[3]))
      self.messArea.setFont(font)
      self.messArea.setReadOnly(True)
      self.messArea.setAlignment(QtCore.Qt.AlignLeft)
      self.messArea.setObjectName("messArea")

      self.AnonGo = QtWidgets.QPushButton(AnonForm)
      self.AnonGo.setEnabled(False)
      self.AnonGo.setGeometry(QtCore.QRect(AnonGoBtn[0], AnonGoBtn[1], AnonGoBtn[2], AnonGoBtn[3]))
      self.AnonGo.setFont(font)
      self.AnonGo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
      self.AnonGo.setObjectName("AnonGo")

      self.retranslateUi(AnonForm)
      QtCore.QMetaObject.connectSlotsByName(AnonForm)

      self.link1.textChanged.connect(self.AnonOnpercentInputChg)
      self.link2.textChanged.connect(self.AnonOnpercentInputChg)
      self.link3.textChanged.connect(self.AnonOnpercentInputChg)
      self.link4.textChanged.connect(self.AnonOnpercentInputChg)
      self.link5.textChanged.connect(self.AnonOnpercentInputChg)
      self.AnonGo.clicked.connect(lambda: self.AnonGoSim(self.fbAccount.text(),self.passwordAccount.text(), self.link1.text(), self.link2.text(), self.link3.text(), self.link4.text(), self.link5.text()))
	  
   
   def AnonGoSim(self, fbAccount, passwordAccount, link1, link2, link3, link4, link5):
      self.messArea.clear()
      links = [link1, link2, link3, link4, link5]
      links = list(filter(None, links))

      self.__jumpToWeb(fbAccount, passwordAccount, links)
      self.messArea.append(link)
      self.messArea.show()

   def AnonOnpercentInputChg(self, text):
      if text:
         self.AnonGo.setEnabled(True)
      else:
         self.AnonGo.setEnabled(False)

   def retranslateUi(self, AnonForm):
      AnonForm.setWindowTitle("Share to FB")
      self.fbAccountLable.setText("FaceBook account: ")
      self.IdAccountLable.setText("Id: ")
      self.pwAccountLable.setText("Password: ")
      self.Link1Lable.setText("Link1: ")
      self.Link2Lable.setText("Link2: ")
      self.Link3Lable.setText("Link3: ")
      self.Link4Lable.setText("Link4: ")
      self.Link5Lable.setText("Link5: ")
      self.messAreaLable.setText("MESSAGE BOX")
      self.AnonGo.setText("Go!")


  
   def __jumpToWeb(self, fbAccount, passwordAccount, links):
      Web = fgGroupPoster(fbAccount, passwordAccount, links)
      self.messArea.append(Web.mess)
     

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   AnonForm = QtWidgets.QWidget()
   ui = Ui_AnonForm()
   ui.setupUi(AnonForm)
   AnonForm.show()
   sys.exit(app.exec_())