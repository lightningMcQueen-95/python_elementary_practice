import os
import pyqrcode
from PIL import Image

class   QR_Gen(object):
    def _init_(self, text):
        self.qr_image = self.qr_generator(text)

    @staticmethod
    def qr_generator(text):
        qr_code = pyqrcode.create(text)
        file_name = "QR Code Result"
        save_path = os.path.join(os.path.expand('~'),'Desktop')

        name = f"{save_path}{file_name}.png"
        qr_code.png(name, scaler=10)
        image = Image.open(name)
        image = image.resize((400,400),Image.ANTIALIAS)
        image.show()

if __name__== "__main__":
    QR_Gen(input("[QR] Enter text or link: "))
