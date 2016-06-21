#!/usr/bin/python
myFontSize = 40

from PyQt4 import QtGui
from PyQt4 import QtCore

import sys
import datetime

class Win(QtGui.QMainWindow):
    def __init__(self, parent = None):
        app = QtGui.QApplication(sys.argv)
        app.setAttribute(QtCore.Qt.WA_TranslucentBackground
                        | QtCore.Qt.WA_X11NetWmWindowTypeDesktop)
        QtGui.QMainWindow.__init__(self, parent, QtCore.Qt.WindowStaysOnBottomHint)
        palette = QtGui.QPalette()
        self.label = QtGui.QLabel()

        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)
        self.label.setPalette(palette)

        self.label.resize(1920, 1080)
        font = self.label.font()
        font.setPixelSize(myFontSize)
        self.label.setFont(font)

        self.label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground
                        | QtCore.Qt.WA_X11NetWmWindowTypeDesktop)

        self.update()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        sys.exit(app.exec_())

    def update(self):
        today = datetime.datetime.today()
        friday = datetime.timedelta(
                (4 - today.weekday()) % 7,
                0 - today.second,
                0, 0,
                30 - today.minute,
                16 - today.hour)
        self.label.setText("%i day(s) %i hour(s) %i minute(s) %i second(s) until comming weekend"
                % (friday.days, friday.seconds / 3600, (friday.seconds / 60) % 60,
                    friday.seconds % 60))
        self.label.show()

def main():
    QtCore.QThread(Win()).start()

if __name__ == '__main__':
    main()
