from PySide6.QtCore import QObject, QThread, Signal

class Worker(QObject):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        for i in range(100):
            self.progress.emit(i)
        self.finished.emit()

def create_demo():
    worker = Worker()
    thread = QThread()
    worker.moveToThread(thread)
    return thread, worker