from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

def create_demo():
    player = QMediaPlayer()
    audio = QAudioOutput()
    player.setAudioOutput(audio)
    video_widget = QVideoWidget()
    player.setVideoOutput(video_widget)
    return video_widget, player