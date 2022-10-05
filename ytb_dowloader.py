from http.client import ImproperConnectionState
from pytube import YouTube
from screen_ytb_dowloader import Ui_ytb_dowloader
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget)
import sys


# Pergunta pelo link do YouTube

def download(link):
    print(link)
    yt = YouTube(link)

    # Mostra detalhes do vídeo
    print("Título: ",yt.title)
    print("Tempo do vídeo: ",yt.length, " segundos")
    print("Tamando do vídeo: ",yt.streams.get_highest_resolution().filesize ,"em bytes")
    print(yt.thumbnail_url)
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Starting download
    print("Downloading...")
    ys.download()
    print("Download finalizado!!")

class download_video(Ui_ytb_dowloader, QWidget, YouTube):
    def __init__(self):
        super(download_video, self).__init__()
        self.setupUi(self)
        
        self.baixar.clicked.connect(lambda: self.baixar(self.pesq_link.text()))

    def baixar(self,lk):
        self.dt_title = YouTube.title
        self.dt_temp = YouTube.length
        self.dt_tam = YouTube.streams.get_highest_resolution().filesize
        self.dt_img = YouTube.thumbnail_url

        YouTube.download()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = download_video()
    window.show()
    app.exec()