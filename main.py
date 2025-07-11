try:
    from PySide6.QtWidgets import QApplication, QMainWindow
except ImportError as e:
    print("ImportError:", e)
    print("Please install system OpenGL library. On Debian/Ubuntu:")
    print("  sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx")
    import sys; sys.exit(1)

import sys
import config
from features import basic_widgets, layouts, signals_slots

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle(config.APP_NAME)
    window.resize(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

    # 基本ウィジェットサンプルを中央に表示
    demo_widget = basic_widgets.create_demo()
    window.setCentralWidget(demo_widget)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()