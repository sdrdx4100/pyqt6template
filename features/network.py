from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl

def fetch_url(url: str):
    manager = QNetworkAccessManager()
    request = QNetworkRequest(QUrl(url))
    reply = manager.get(request)
    return reply