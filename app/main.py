import sys
import design
from PyQt5 import QtWidgets
import dispatchers.vk_api as vk
import dispatchers.fb_api as fb
from settings import settings


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.send_btn.clicked.connect(self.send)
        self.clear_btn.clicked.connect(self.clear)
        self.files = set()
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        files = event.mimeData().urls()
        for f in files:
            self.files.add(f.path())

        if len(self.files) > 5:
            self.clear()
            msg = QtWidgets.QMessageBox()
            msg.setText('Too much images!')
            msg.exec()
        else:
            self.file_box.setText('\n'.join(self.files))

    def send(self):
        message = self.message_box.toPlainText()
        if self.files:
            vk_res = 'vk - ' + vk.postPhoto(settings['vk_token'], settings['vk_gid'], message, self.files)
            fb_res = 'fb - ' + fb.postPhoto(settings['fb_token'], settings['fb_gid'], message, self.files)
        else:
            vk_res = 'vk - ' + vk.post(settings['vk_token'], settings['vk_gid'], message)
            fb_res = 'fb - ' + fb.post(settings['fb_token'], settings['fb_gid'], message)
        response = vk_res + '\n' + fb_res
        msg = QtWidgets.QMessageBox()
        msg.setText(response)
        msg.exec()
        self.clear()

    def clear(self):
        self.message_box.clear()
        self.files = set()
        self.file_box.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
