import sip
from functools import partial

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QDialog, QGridLayout, QCheckBox)
from PyQt5.Qt import Qt
import numpy as np

from ..core.Biochemistry import ContactType
from .Plotters import ContactPlotter
from .DetailWidget import Detail


class LabelView(QWidget):
    """Proviedes more detailed statistics of the clicked contact in MainWindow."""

    def __init__(self, accumulatedTrajectory):
        super(QWidget, self).__init__()
        self.trajectory = accumulatedTrajectory
        # self.vismode = False
        self.buttons = []
        self.checkboxes = []
        self.buttonWidths = []
        self.detailView = None
        self.nsPerFrame = 0
        self.threshold = 0
        self.initUI()
        print(self.geometry())

    def clean(self):
        """Delete all labels."""
        allLabels = self.findChildren(QPushButton)
        for child in allLabels:
            sip.delete(child)
        allBoxes = self.findChildren(QCheckBox)
        for child in allBoxes:
            sip.delete(child)

    def initUI(self):
        """Create the labels to the corresponding contact"""
        start_text = 10
        textoffset = 5
        rowheight = 22
        row = 0
        checkboxOffset = 0
        # next version...
        # if self.vismode:
        #     checkboxOffset = 15

        if self.trajectory is None:
            return

        cindex = 0
        for title, ctype in zip(self.trajectory.titles, self.trajectory.contactTypes):
            self.buttons.append(QPushButton(title))
            stylesheet = "border: 0px solid #222222; background-color: " + ContactType.colors[ctype] + ";"
            self.buttons[-1].setStyleSheet(stylesheet)
            self.buttons[-1].clicked.connect(partial(self.handleButton, data=cindex))
            self.buttons[-1].setParent(self)
            self.buttons[-1].move(start_text + checkboxOffset, row + textoffset)
            self.buttons[-1].setFont(QFont('Arial', 9))
            self.buttons[-1].show()
            self.buttonWidths.append(self.buttons[-1].width())
            # next version
            # if self.vismode:
            #     self.checkboxes.append(QCheckBox())
            #     self.checkboxes[-1].setParent(self)
            #     self.checkboxes[-1].move(start_text, row + textoffset - 2.0)
            #     self.checkboxes[-1].show()
            row += rowheight
            cindex += 1
        if len(self.buttonWidths):
            self.setGeometry(0, 0, np.max(self.buttonWidths) + 10, row)

    def handleButton(self, data):
        """Show the detailed view when clicking on the contact label"""
        self.detailView = Detail(self.contacts[data], self.nsPerFrame, self.threshold)
        self.detailView.show()
