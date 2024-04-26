import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import vlc


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowIcon(QIcon('icon.png'))

        self.instance = vlc.Instance("--no-xlib")
        self.player = self.instance.media_player_new()

        self.video_widget = QWidget(self)
        self.video_layout = QVBoxLayout()
        self.video_widget.setLayout(self.video_layout)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_video)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_video)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_video)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        # Connect slider to media position
        self.slider.sliderMoved.connect(self.set_position)

        self.video_layout.addWidget(self.start_button)
        self.video_layout.addWidget(self.pause_button)
        self.video_layout.addWidget(self.stop_button)
        self.video_layout.addWidget(self.slider)

        self.setCentralWidget(self.video_widget)

        self.media = self.instance.media_new('video.mp4')
        self.player.set_media(self.media)

    def start_video(self):
        self.player.play()

    def pause_video(self):
        self.player.pause()

    def stop_video(self):
        self.player.stop()

    def set_position(self, position):
        self.player.set_position(position / 1000)  # Convert to seconds


if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_player = VideoPlayer()
    video_player.show()
    sys.exit(app.exec())
