import sys
import design
from PyQt5 import QtWidgets
import dispatchers.vk_api as vk
import dispatchers.fb_api as fb
from settings import settings

# result = vk.post(settings['vk_token'], settings['vk_gid'], 'baca')
# result = fb.post(settings['fb_token'], settings['fb_gid'], 'baca')

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.send_btn.clicked.connect(self.send)
        self.clear_btn.clicked.connect(self.clear)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        files = event.mimeData().urls()
        for f in files:
            self.file_box.setText(f.path())

    def send(self):
        message = self.message_box.toPlainText()
        file = self.file_box.toPlainText()
        if file:
            print(file)
        else:
            vk_res = 'vk - ' + vk.post(settings['vk_token'], settings['vk_gid'], 'baca')
            fb_res = 'fb - ' + fb.post(settings['fb_token'], settings['fb_gid'], 'baca')
            response = vk_res + '\n' + fb_res
            msg = QtWidgets.QMessageBox()
            msg.setText(response)
            msg.exec()
        self.clear()

    def clear(self):
        self.message_box.clear()
        self.file_box.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
