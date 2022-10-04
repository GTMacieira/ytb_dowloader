# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen_ytb_dowloader.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ytb_dowloader(object):
    def setupUi(self, ytb_dowloader):
        if not ytb_dowloader.objectName():
            ytb_dowloader.setObjectName(u"ytb_dowloader")
        ytb_dowloader.resize(650, 450)
        ytb_dowloader.setMinimumSize(QSize(650, 450))
        ytb_dowloader.setMaximumSize(QSize(600, 450))
        icon = QIcon()
        icon.addFile(u"youtube-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        ytb_dowloader.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(ytb_dowloader)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pesquisa = QFrame(ytb_dowloader)
        self.pesquisa.setObjectName(u"pesquisa")
        self.pesquisa.setMaximumSize(QSize(550, 50))
        self.pesquisa.setLayoutDirection(Qt.LeftToRight)
        self.pesquisa.setStyleSheet(u"alternate-background-color: rgba(255, 255, 255, 2);")
        self.pesquisa.setFrameShape(QFrame.NoFrame)
        self.pesquisa.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.pesquisa)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo = QLabel(self.pesquisa)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(40, 16777215))
        self.logo.setPixmap(QPixmap(u"youtube-logo.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.label_link = QLabel(self.pesquisa)
        self.label_link.setObjectName(u"label_link")
        self.label_link.setMinimumSize(QSize(50, 0))
        self.label_link.setLayoutDirection(Qt.LeftToRight)
        self.label_link.setAutoFillBackground(False)
        self.label_link.setIndent(21)

        self.horizontalLayout.addWidget(self.label_link)

        self.pesq_link = QLineEdit(self.pesquisa)
        self.pesq_link.setObjectName(u"pesq_link")
        self.pesq_link.setMaximumSize(QSize(450, 16777215))

        self.horizontalLayout.addWidget(self.pesq_link)


        self.verticalLayout.addWidget(self.pesquisa)

        self.info_frame = QFrame(ytb_dowloader)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setAutoFillBackground(False)
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.info_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tam_video = QLabel(self.info_frame)
        self.tam_video.setObjectName(u"tam_video")
        self.tam_video.setMaximumSize(QSize(110, 50))

        self.gridLayout.addWidget(self.tam_video, 2, 0, 1, 1)

        self.img_video = QLabel(self.info_frame)
        self.img_video.setObjectName(u"img_video")
        self.img_video.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.img_video, 3, 0, 1, 1)

        self.titulo = QLabel(self.info_frame)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setMaximumSize(QSize(110, 50))

        self.gridLayout.addWidget(self.titulo, 0, 0, 1, 1)

        self.reprud_time = QLabel(self.info_frame)
        self.reprud_time.setObjectName(u"reprud_time")
        self.reprud_time.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.reprud_time, 1, 0, 1, 1)

        self.dt_img = QLabel(self.info_frame)
        self.dt_img.setObjectName(u"dt_img")
        self.dt_img.setMaximumSize(QSize(300, 170))
        self.dt_img.setPixmap(QPixmap(u"youtube-logo.png"))
        self.dt_img.setScaledContents(True)

        self.gridLayout.addWidget(self.dt_img, 3, 1, 1, 1)

        self.dt_title = QLineEdit(self.info_frame)
        self.dt_title.setObjectName(u"dt_title")
        self.dt_title.setMaximumSize(QSize(300, 16777215))
        self.dt_title.setReadOnly(True)

        self.gridLayout.addWidget(self.dt_title, 0, 1, 1, 1)

        self.dt_temp = QLineEdit(self.info_frame)
        self.dt_temp.setObjectName(u"dt_temp")
        self.dt_temp.setMaximumSize(QSize(300, 16777215))
        self.dt_temp.setReadOnly(True)

        self.gridLayout.addWidget(self.dt_temp, 1, 1, 1, 1)

        self.dt_tam = QLineEdit(self.info_frame)
        self.dt_tam.setObjectName(u"dt_tam")
        self.dt_tam.setMaximumSize(QSize(300, 16777215))
        self.dt_tam.setReadOnly(True)

        self.gridLayout.addWidget(self.dt_tam, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.info_frame)

        self.load_frame = QFrame(ytb_dowloader)
        self.load_frame.setObjectName(u"load_frame")
        self.load_frame.setMaximumSize(QSize(600, 50))
        self.load_frame.setFrameShape(QFrame.StyledPanel)
        self.load_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.load_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressBar = QProgressBar(self.load_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(600, 16777215))
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.load_frame)

        self.baixar = QPushButton(ytb_dowloader)
        self.baixar.setObjectName(u"baixar")
        self.baixar.setMaximumSize(QSize(580, 16777215))

        self.verticalLayout.addWidget(self.baixar)


        self.retranslateUi(ytb_dowloader)

        QMetaObject.connectSlotsByName(ytb_dowloader)
    # setupUi

    def retranslateUi(self, ytb_dowloader):
        ytb_dowloader.setWindowTitle(QCoreApplication.translate("ytb_dowloader", u"DOWLOAD YOUTUBE", None))
        self.logo.setText("")
        self.label_link.setText(QCoreApplication.translate("ytb_dowloader", u"LINK:", None))
        self.tam_video.setText(QCoreApplication.translate("ytb_dowloader", u"Tamanho do v\u00eddeo:", None))
        self.img_video.setText(QCoreApplication.translate("ytb_dowloader", u"Imagem:", None))
        self.titulo.setText(QCoreApplication.translate("ytb_dowloader", u"T\u00edtulo:", None))
        self.reprud_time.setText(QCoreApplication.translate("ytb_dowloader", u"Tempo de reprodu\u00e7\u00e3o:", None))
        self.dt_img.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("ytb_dowloader", u"%p%", None))
        self.baixar.setText(QCoreApplication.translate("ytb_dowloader", u"Baixar", None))
    # retranslateUi

