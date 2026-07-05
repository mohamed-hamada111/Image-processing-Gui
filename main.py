from PyQt5 import QtWidgets ,QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog ,QApplication ,QMainWindow 
from PyQt5.QtGui import QPixmap ,QImage
from PyQt5.QtCore import Qt

from Sobel import Ui_Form as Ui_Sobel
from perweit import Ui_Form as Ui_perweit
from canny import Ui_Cancel as Ui_canny
from laplace import Ui_Form as Ui_laplace
from gaussian import Ui_Form as Ui_gaussian
from rotate import Ui_Form as Ui_rotate
from flip import Ui_Form as Ui_flip
from histgram import Ui_Form as Ui_hist
from adaptive import Ui_Form as Ui_adaptive
from otsu import Ui_Form as Ui_otsu

from ui_mainWindow import Ui_MainWindow
import sys

import cv2
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.SobalDialog =QtWidgets.QDialog()
        self.sobelform = Ui_Sobel()
        self.sobelform.setupUi(self.SobalDialog)

        self.ui.upload.clicked.connect(self.upload_image)
        self.ui.cancel.clicked.connect(self.Clear_image)
        self.ui.sobal.clicked.connect(self.sobel)
        self.ui.Perweit.clicked.connect(self.perweit)

        self.sobelform.horizontalSlider.valueChanged.connect(self.sobel)
        self.sobelform.Cancel.clicked.connect(self.SobalDialog.close)

        self.perweitDialog = QtWidgets.QDialog()
        self.perweitform = Ui_perweit()
        self.perweitform.setupUi(self.perweitDialog)
        self.perweitform.Cancel.clicked.connect(self.perweitDialog.close)

        self.cannyDialog =QtWidgets.QDialog()
        self.cannyform = Ui_canny()
        self.cannyform.setupUi(self.cannyDialog)
        self.ui.canny.clicked.connect(self.Canny)
        self.cannyform.horizontalSlider.valueChanged.connect(self.Canny)
        self.cannyform.horizontalSlider_2.valueChanged.connect(self.Canny)
        self.cannyform.Cancel_2.clicked.connect(self.cannyDialog.close)

        # Laplace filter transformation 
        self.laplaceDialog =QtWidgets.QDialog()
        self.laplaceform =Ui_laplace()
        self.laplaceform.setupUi(self.laplaceDialog)
        self.ui.laplace.clicked.connect(self.Laplace)
        self.laplaceform.horizontalSlider.valueChanged.connect(self.Laplace)
        self.laplaceform.Cancel.clicked.connect(self.laplaceDialog.close)

        # Gaussian Blur
        self.gaussianDialog =QtWidgets.QDialog()
        self.gaussianform =Ui_gaussian()
        self.gaussianform.setupUi(self.gaussianDialog)
        self.ui.Guassian.clicked.connect(self.GuassianBlur)
        self.gaussianform.horizontalSlider.valueChanged.connect(self.GuassianBlur)
        self.gaussianform.verticalSlider_1.valueChanged.connect(self.GuassianBlur)
        self.gaussianform.verticalSlider_2.valueChanged.connect(self.GuassianBlur)
        self.gaussianform.Cancel.clicked.connect(self.gaussianDialog.close)

        # Rotation
        self.rotateDialog =QtWidgets.QDialog()
        self.rotateform = Ui_rotate()
        self.rotateform.setupUi(self.rotateDialog)
        self.ui.Rotation.clicked.connect(self.Rotate)
        self.rotateform.Rotate.clicked.connect(self.Rotate)
        self.rotateform.Cancel.clicked.connect(self.rotateDialog.close)

        # Flipping
        self.flipDialog =QtWidgets.QDialog()
        self.flipform = Ui_flip()
        self.flipform.setupUi(self.flipDialog)
        self.ui.Flipping.clicked.connect(self.flipping)
        self.flipform.Flipping.clicked.connect(self.flipping)
        self.flipform.Cancel.clicked.connect(self.flipDialog.close)

        # Histgram
        self.histDialog =QtWidgets.QDialog()
        self.histform =Ui_hist()
        self.histform.setupUi(self.histDialog)
        self.ui.Histgram.clicked.connect(self.Histogram)
        self.histform.horizontalSlider.valueChanged.connect(self.Histogram)
        self.histform.Cancel.clicked.connect(self.histDialog.close)

        # Adaptive Histgram
        self.adptiveDialog =QtWidgets.QDialog()
        self.adptiveform =Ui_adaptive()
        self.adptiveform.setupUi(self.adptiveDialog)
        self.ui.adaptive.clicked.connect(self.AdaptiveHistogram)
        self.adptiveform.horizontalSlider.valueChanged.connect(self.AdaptiveHistogram)
        self.adptiveform.horizontalSlider_2.valueChanged.connect(self.AdaptiveHistogram)
        self.adptiveform.Cancel.clicked.connect(self.adptiveDialog.close) 

        # otsu
        self.otsueDialog =QtWidgets.QDialog()
        self.otsuform =Ui_otsu()
        self.otsuform.setupUi(self.otsueDialog)
        self.ui.otsu.clicked.connect(self.Otsu)
        self.otsuform.Cancel.clicked.connect(self.otsueDialog.close)


    def DisplayImage(self, image, label):
        if image.ndim == 2:
            h, w = image.shape
            bytes_per_line = w
            qimage = QImage(image.data, w, h, bytes_per_line,QImage.Format_Grayscale8)
        else:
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytes_per_line = w * ch
            qimage = QImage(img.data, w, h, bytes_per_line,QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qimage)

        return pixmap.scaled(
            label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )


    def upload_image(self):
        file_name ,_ = QFileDialog.getOpenFileName(None ,"Open Image" ,"" ,"Images (*.jfif *.png  *.jpg *.jpeg *.gif)")
        self.image = cv2.imread(file_name)
        if not file_name:
            return
        pixmap =QPixmap(file_name)
        if pixmap.isNull():
            return 
        
        scaled = pixmap.scaled(self.ui.ImageLabel.size() ,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.ui.ImageLabel.setPixmap(scaled)
        self.img =self.image.copy()


    def Clear_image(self):
        self.ui.ImageLabel.clear()
        self.ui.ImageLabel.setText("Select Image")

    def sobel(self):
        gray = cv2.cvtColor(self.image , cv2.COLOR_BGR2GRAY)
        ksize = self.sobelform.horizontalSlider.value()
        if ksize%2 ==0:
            ksize +=1
        sobelx =cv2.Sobel(gray,cv2.CV_64F,1,0,ksize= ksize) 
        sobely =cv2.Sobel(gray,cv2.CV_64F,0,1,ksize= ksize) 

        sobelx =cv2.convertScaleAbs(sobelx)
        sobely =cv2.convertScaleAbs(sobely)


        scaled =self.DisplayImage(sobelx+sobely ,self.sobelform.Image)
        self.sobelform.Image.setPixmap(scaled)
        self.sobelform.sobelx.setPixmap(self.DisplayImage(sobelx,self.sobelform.sobelx))
        self.sobelform.sobely.setPixmap(self.DisplayImage(sobely,self.sobelform.sobely))

        self.SobalDialog.show()


    def perweit(self):
        gray = cv2.cvtColor(self.image ,cv2.COLOR_BGR2GRAY)
        kernelx =np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        kernely =np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

        perweitx = cv2.filter2D(gray ,-1,kernelx)
        perweity = cv2.filter2D(gray ,-1,kernelx)

        perweitx = cv2.convertScaleAbs(perweitx)
        perweity = cv2.convertScaleAbs(perweity)

        scaled =self.DisplayImage(perweitx+perweity ,self.perweitform.Image)
        self.perweitform.Image.setPixmap(scaled)
        self.perweitform.perweitx.setPixmap(self.DisplayImage(perweitx ,self.perweitform.perweitx))
        self.perweitform.perweity.setPixmap(self.DisplayImage(perweity ,self.perweitform.perweity))
        self.perweitDialog.show()

    def Canny(self):
        gray = cv2.cvtColor(self.image ,cv2.COLOR_BGR2GRAY)
        gaussian = cv2.GaussianBlur(gray ,(3,3) ,0)
        threshold1 =self.cannyform.horizontalSlider.value()
        threshold2 =self.cannyform.horizontalSlider_2.value()

        img =cv2.Canny(gaussian ,threshold1 ,threshold2)
        scaled =self.DisplayImage(img ,self.cannyform.Image)
        self.cannyform.Image.setPixmap(scaled)
        self.cannyDialog.show()


    def Laplace(self):
        gray = cv2.cvtColor(self.image ,cv2.COLOR_BGR2GRAY)
        guassian = cv2.GaussianBlur(gray ,(3,3), 0)
        kernel_size = self.laplaceform.horizontalSlider.value()
        if kernel_size%2 ==0:
            kernel_size +=1

        img = cv2.Laplacian(guassian ,cv2.CV_64F , ksize=kernel_size)
        img = cv2.convertScaleAbs(img)
        self.laplaceform.image.setPixmap(self.DisplayImage(img ,self.laplaceform.image))
        self.laplaceDialog.show()

    
    def GuassianBlur(self):
        ksize =self.gaussianform.horizontalSlider.value()
        sigmaX =self.gaussianform.verticalSlider_2.value()
        sigmaY =self.gaussianform.verticalSlider_1.value()
        if ksize %2 ==0:
            ksize +=1

        guassian = cv2.GaussianBlur(self.image ,ksize=(ksize,ksize) ,sigmaX=sigmaX ,sigmaY=sigmaY)
        self.gaussianform.image.setPixmap(self.DisplayImage(guassian,self.gaussianform.image))
        self.gaussianDialog.show()

    def Rotate(self):
        angle = self.rotateform.spinBox.value()
        (h, w) = self.image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1)
        rotated = cv2.warpAffine(self.image, M, (w, h))
        self.rotateform.image.setPixmap(self.DisplayImage(rotated, self.rotateform.image)) 
        self.rotateDialog.show()

    def flipping(self):
        self.img = cv2.flip(self.img ,1)
        self.flipform.image.setPixmap(self.DisplayImage(self.img,self.flipform.image))
        self.flipDialog.show()

    def Histogram(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        threshold = self.histform.horizontalSlider.value()
        _, segmented = cv2.threshold(gray,threshold,255,cv2.THRESH_BINARY)
        self.histform.image.setPixmap(self.DisplayImage(segmented, self.histform.image))
        self.histDialog.show()

    def AdaptiveHistogram(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blockSize = self.adptiveform.horizontalSlider.value()
        C = self.adptiveform.horizontalSlider_2.value()

        # blockSize must be odd and greater than 1
        if blockSize < 3:
            blockSize = 3
        if blockSize % 2 == 0:
            blockSize += 1

        adaptive = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blockSize,C)
        self.adptiveform.image.setPixmap(self.DisplayImage(adaptive, self.adptiveform.image))
        self.adptiveDialog.show()


    def Otsu(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        threshold, otsu = cv2.threshold(gray,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        print("Otsu Threshold =", threshold)
        self.otsuform.image.setPixmap(self.DisplayImage(otsu, self.otsuform.image))
        self.otsueDialog.show()



if __name__ =="__main__":
    app =QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())