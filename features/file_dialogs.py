from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog


def create_demo():
    widget = QWidget()
    layout = QVBoxLayout(widget)
    text_edit = QTextEdit()
    open_btn = QPushButton("Open File")
    save_btn = QPushButton("Save File")

    def open_file():
        path, _ = QFileDialog.getOpenFileName(widget, "Open Text File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text_edit.setPlainText(f.read())
            except Exception as e:
                text_edit.setPlainText(f"Failed to open file: {e}")

    def save_file():
        path, _ = QFileDialog.getSaveFileName(widget, "Save Text File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text_edit.toPlainText())
            except Exception as e:
                text_edit.setPlainText(f"Failed to save file: {e}")

    open_btn.clicked.connect(open_file)
    save_btn.clicked.connect(save_file)

    layout.addWidget(text_edit)
    layout.addWidget(open_btn)
    layout.addWidget(save_btn)

    return widget
