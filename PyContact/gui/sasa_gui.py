# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sasa.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SasaWidget(object):
    def setupUi(self, SasaWidget):
        SasaWidget.setObjectName("SasaWidget")
        SasaWidget.resize(712, 514)
        self.gridLayoutWidget = QtWidgets.QWidget(SasaWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 701, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.sasaSelection1TextField = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sasaSelection1TextField.setObjectName("sasaSelection1TextField")
        self.gridLayout.addWidget(self.sasaSelection1TextField, 3, 1, 1, 1)
        self.calculateContactAreaCheckbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.calculateContactAreaCheckbox.setObjectName("calculateContactAreaCheckbox")
        self.gridLayout.addWidget(self.calculateContactAreaCheckbox, 5, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.calcSasaButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.calcSasaButton.setObjectName("calcSasaButton")
        self.gridLayout.addWidget(self.calcSasaButton, 7, 3, 1, 1)
        self.sasaGraphWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.sasaGraphWidget.setObjectName("sasaGraphWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.sasaGraphWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 521, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.graphGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.graphGridLayout.setContentsMargins(0, 0, 0, 0)
        self.graphGridLayout.setObjectName("graphGridLayout")
        self.gridLayout.addWidget(self.sasaGraphWidget, 6, 1, 1, 1)
        self.sasaRestrictionTextField = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sasaRestrictionTextField.setObjectName("sasaRestrictionTextField")
        self.gridLayout.addWidget(self.sasaRestrictionTextField, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.sasaSelection2TextField = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sasaSelection2TextField.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sasaSelection2TextField.sizePolicy().hasHeightForWidth())
        self.sasaSelection2TextField.setSizePolicy(sizePolicy)
        self.sasaSelection2TextField.setMinimumSize(QtCore.QSize(0, 0))
        self.sasaSelection2TextField.setObjectName("sasaSelection2TextField")
        self.gridLayout.addWidget(self.sasaSelection2TextField, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.loadDataButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loadDataButton.setObjectName("loadDataButton")
        self.gridLayout.addWidget(self.loadDataButton, 2, 0, 1, 1)
        self.sasaProgressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.sasaProgressBar.setProperty("value", 0)
        self.sasaProgressBar.setTextVisible(True)
        self.sasaProgressBar.setInvertedAppearance(False)
        self.sasaProgressBar.setObjectName("sasaProgressBar")
        self.gridLayout.addWidget(self.sasaProgressBar, 7, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.coreBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.coreBox.setMinimum(1)
        self.coreBox.setMaximum(32)
        self.coreBox.setProperty("value", 4)
        self.coreBox.setObjectName("coreBox")
        self.verticalLayout.addWidget(self.coreBox)
        self.gridLayout.addLayout(self.verticalLayout, 6, 3, 1, 1)

        self.retranslateUi(SasaWidget)
        QtCore.QMetaObject.connectSlotsByName(SasaWidget)

    def retranslateUi(self, SasaWidget):
        _translate = QtCore.QCoreApplication.translate
        SasaWidget.setWindowTitle(_translate("SasaWidget", "Surface Areas"))
        self.calculateContactAreaCheckbox.setText(_translate("SasaWidget", "contact"))
        self.label.setText(_translate("SasaWidget", "selection:"))
        self.calcSasaButton.setText(_translate("SasaWidget", "Calculate"))
        self.label_2.setText(_translate("SasaWidget", "restriction:"))
        self.label_3.setText(_translate("SasaWidget", "selection 2:"))
        self.loadDataButton.setText(_translate("SasaWidget", "Load Data"))
        self.label_4.setText(_translate("SasaWidget", "Cores:"))

