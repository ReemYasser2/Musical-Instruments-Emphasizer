# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Desktop\test\Musical-Instruments-Emphasizer-main\task3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupbox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupbox_4.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.groupbox_4.setTitle("")
        self.groupbox_4.setObjectName("groupbox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupbox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pause_button = QtWidgets.QPushButton(self.groupbox_4)
        self.pause_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\test\\Musical-Instruments-Emphasizer-main\\pause 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_button.setIcon(icon)
        self.pause_button.setObjectName("pause_button")
        self.horizontalLayout.addWidget(self.pause_button)
        self.play_button = QtWidgets.QPushButton(self.groupbox_4)
        self.play_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\test\\Musical-Instruments-Emphasizer-main\\play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        self.volume_slider = QtWidgets.QSlider(self.groupbox_4)
        self.volume_slider.setMinimumSize(QtCore.QSize(400, 0))
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.horizontalLayout.addWidget(self.volume_slider)
        self.volume_number = QtWidgets.QLabel(self.groupbox_4)
        self.volume_number.setMinimumSize(QtCore.QSize(150, 0))
        self.volume_number.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.volume_number.setObjectName("volume_number")
        self.horizontalLayout.addWidget(self.volume_number)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.groupbox_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupbox = QtWidgets.QGroupBox(self.tab)
        self.groupbox.setMaximumSize(QtCore.QSize(640, 16777215))
        self.groupbox.setStyleSheet("background-color: rgb(107, 107, 107);")
        self.groupbox.setTitle("")
        self.groupbox.setObjectName("groupbox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupbox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.instrument1_label = QtWidgets.QLabel(self.groupbox)
        self.instrument1_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Eras Demi ITC\";")
        self.instrument1_label.setObjectName("instrument1_label")
        self.verticalLayout.addWidget(self.instrument1_label)
        self.instrument1_slider = QtWidgets.QSlider(self.groupbox)
        self.instrument1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.instrument1_slider.setObjectName("instrument1_slider")
        self.verticalLayout.addWidget(self.instrument1_slider)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.instrument2_label = QtWidgets.QLabel(self.groupbox)
        self.instrument2_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Eras Demi ITC\";")
        self.instrument2_label.setObjectName("instrument2_label")
        self.verticalLayout_2.addWidget(self.instrument2_label)
        self.instrument2_slider = QtWidgets.QSlider(self.groupbox)
        self.instrument2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.instrument2_slider.setObjectName("instrument2_slider")
        self.verticalLayout_2.addWidget(self.instrument2_slider)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.instrument3_label = QtWidgets.QLabel(self.groupbox)
        self.instrument3_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Eras Demi ITC\";")
        self.instrument3_label.setObjectName("instrument3_label")
        self.verticalLayout_3.addWidget(self.instrument3_label)
        self.instrument3_slider = QtWidgets.QSlider(self.groupbox)
        self.instrument3_slider.setOrientation(QtCore.Qt.Horizontal)
        self.instrument3_slider.setObjectName("instrument3_slider")
        self.verticalLayout_3.addWidget(self.instrument3_slider)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.equalize_button = QtWidgets.QPushButton(self.groupbox)
        self.equalize_button.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.equalize_button.setObjectName("equalize_button")
        self.verticalLayout_5.addWidget(self.equalize_button)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupbox)
        self.splitter_3 = QtWidgets.QSplitter(self.tab)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.mainsignal_widget = PlotWidget(self.splitter_3)
        self.mainsignal_widget.setMinimumSize(QtCore.QSize(600, 0))
        self.mainsignal_widget.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.mainsignal_widget.setObjectName("mainsignal_widget")
        self.spectrogram_widget = PlotWidget(self.splitter_3)
        self.spectrogram_widget.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.spectrogram_widget.setObjectName("spectrogram_widget")
        self.horizontalLayout_2.addWidget(self.splitter_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout_7.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.drums_label = QtWidgets.QLabel(self.tab_2)
        self.drums_label.setMinimumSize(QtCore.QSize(0, 0))
        self.drums_label.setText("")
        self.drums_label.setPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\test\\Musical-Instruments-Emphasizer-main\\drumss.png"))
        self.drums_label.setScaledContents(True)
        self.drums_label.setWordWrap(False)
        self.drums_label.setObjectName("drums_label")
        self.gridLayout.addWidget(self.drums_label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.xylo_label = QtWidgets.QLabel(self.tab_3)
        self.xylo_label.setText("")
        self.xylo_label.setPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\test\\Musical-Instruments-Emphasizer-main\\xylophone-removebg-preview (1).png"))
        self.xylo_label.setScaledContents(True)
        self.xylo_label.setObjectName("xylo_label")
        self.gridLayout_3.addWidget(self.xylo_label, 0, 0, 2, 3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.piano_label = QtWidgets.QLabel(self.tab_4)
        self.piano_label.setStyleSheet("color: rgb(66, 66, 66);")
        self.piano_label.setText("")
        self.piano_label.setPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\test\\Musical-Instruments-Emphasizer-main\\piano-removebg-preview.png"))
        self.piano_label.setScaledContents(True)
        self.piano_label.setObjectName("piano_label")
        self.gridLayout_4.addWidget(self.piano_label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.splitter, 0, 1, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout_Us = QtWidgets.QMenu(self.menubar)
        self.menuAbout_Us.setObjectName("menuAbout_Us")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\test\\Musical-Instruments-Emphasizer-main\\../../../.designer/backup/DSP/open file.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon2)
        self.action_open.setObjectName("action_open")
        self.action_pause = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\test\\Musical-Instruments-Emphasizer-main\\../../../.designer/backup/DSP/pause 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pause.setIcon(icon3)
        self.action_pause.setObjectName("action_pause")
        self.action_play = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\test\\Musical-Instruments-Emphasizer-main\\../../../.designer/backup/DSP/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_play.setIcon(icon4)
        self.action_play.setObjectName("action_play")
        self.action_open_2 = QtWidgets.QAction(MainWindow)
        self.action_open_2.setObjectName("action_open_2")
        self.Reem_Yasser = QtWidgets.QAction(MainWindow)
        self.Reem_Yasser.setObjectName("Reem_Yasser")
        self.Maryam_Moataz = QtWidgets.QAction(MainWindow)
        self.Maryam_Moataz.setObjectName("Maryam_Moataz")
        self.Hassan_Samy = QtWidgets.QAction(MainWindow)
        self.Hassan_Samy.setObjectName("Hassan_Samy")
        self.Clara_Ashraf = QtWidgets.QAction(MainWindow)
        self.Clara_Ashraf.setObjectName("Clara_Ashraf")
        self.menuFile.addAction(self.action_open_2)
        self.menuAbout_Us.addAction(self.Reem_Yasser)
        self.menuAbout_Us.addAction(self.Maryam_Moataz)
        self.menuAbout_Us.addAction(self.Hassan_Samy)
        self.menuAbout_Us.addAction(self.Clara_Ashraf)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.volume_number.setText(_translate("MainWindow", "Volume"))
        self.instrument1_label.setText(_translate("MainWindow", "Instrument 1"))
        self.instrument2_label.setText(_translate("MainWindow", "Instrument 2"))
        self.instrument3_label.setText(_translate("MainWindow", "Instrument 3"))
        self.equalize_button.setText(_translate("MainWindow", "Equalize"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Isolator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Drums"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Xylophone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Piano"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout_Us.setTitle(_translate("MainWindow", "About Us"))
        self.action_open.setText(_translate("MainWindow", "open"))
        self.action_pause.setText(_translate("MainWindow", "pause"))
        self.action_play.setText(_translate("MainWindow", "play"))
        self.action_open_2.setText(_translate("MainWindow", "Open"))
        self.Reem_Yasser.setText(_translate("MainWindow", "Reem Yasser"))
        self.Maryam_Moataz.setText(_translate("MainWindow", "Maryam Moataz"))
        self.Hassan_Samy.setText(_translate("MainWindow", "Hassan Samy"))
        self.Clara_Ashraf.setText(_translate("MainWindow", "Clara Ashraf"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
