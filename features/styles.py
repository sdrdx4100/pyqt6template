from PySide6.QtWidgets import QApplication

def apply_style(app: QApplication, sheet_path: str):
    with open(sheet_path, "r") as f:
        app.setStyleSheet(f.read())