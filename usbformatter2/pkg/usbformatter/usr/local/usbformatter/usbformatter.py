import sys
import os
import PyQt4
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from usbformatter_ui import Ui_MainWindow
from threading import Thread
import subprocess

usbformatter = QApplication(sys.argv)

def get_file_path(filename):
    if hasattr(sys, 'frozen'):
        return sys.executable
    else:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

class UsbFormatter(QMainWindow):
    start = pyqtSignal()
    end = pyqtSignal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.movie = QMovie(get_file_path('images/loading.gif'))
        self.window.label_3.setMovie(self.movie)
        self.movie.start()
        self.window.label_3.setVisible(False)
        self.load_devices()
        #connects
        self.window.format_button.clicked.connect(self.format_button_clicked)
        self.window.devices_combo.currentIndexChanged.connect(self.devices_combo_clicked)
        self.window.refresh_button.clicked.connect(self.load_devices)
        self.window.action_exit.triggered.connect(self.exit_app)
        self.end.connect(self.set_loading_false)

    def exit_app(self):
        main.close()

    def load_devices(self):
        self.window.devices_combo.clear()
        with open('/proc/mounts') as f:
            data = f.readline()
            while data != "":
                data = f.readline()
                if data.split(' ')[0].startswith('/dev/'):
                    excludes = ['/', '/home', '/boot']
                    not_this = False
                    for ex in excludes:
                        if data.split()[1] == ex: 
                            not_this = True
                    if not_this == False:
                        device = data.split()[0]
                        device_name = data.split()[1].split('/')
                        device_name = data.split()[1].split('/')[len(device_name)-1]
                        self.window.devices_combo.addItem(device_name, userData=device)

    def devices_combo_clicked(self, index):
        pass

    def disable_stuff(self):
        self.window.name_edit.setEnabled(False)
        self.window.devices_combo.setEnabled(False)
        self.window.format_button.setEnabled(False)

    def enable_stuff(self):
        self.window.name_edit.setEnabled(True)
        self.window.devices_combo.setEnabled(True)
        self.window.format_button.setEnabled(True)

    @pyqtSlot()
    def set_loading_false(self):
        self.window.label_3.setVisible(False)

    @pyqtSlot()
    def set_loading_true(self):
        self.window.label_3.setVisible(True)

    def format_device(self, device, device_name):
        subprocess.call(['mkfs.vfat', device, '-n', device_name])
        self.end.emit()
        self.window.label_status.setText('Done!')

    def format_button_clicked(self):
        device = self.window.devices_combo.itemData(self.window.devices_combo.currentIndex())
        device_name = self.window.name_edit.text()
        self.window.label_3.setVisible(True)
        self.start.emit()
        self.window.label_status.setText('Formatting...')
        subprocess.call(['umount', device])
        print('umounted')
        t = Thread(target=self.format_device, args=(device, device_name))
        t.daemon = True
        t.start()
        print('started thread')

    def run(self):
        self.show()
        usbformatter.exec_()

if __name__ == "__main__":
    main = UsbFormatter()
    main.setWindowIcon(QIcon(get_file_path('images/usb-usbformatter.png')))
    main.run()
