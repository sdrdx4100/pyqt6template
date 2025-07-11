try:
    from PySide6.QtWidgets import QApplication, QMainWindow
except ImportError as e:
    print("ImportError:", e)
    print("Please install system OpenGL library. On Debian/Ubuntu:")
    print("  sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx")
    import sys; sys.exit(1)

import sys
import config
import argparse
from features import (
    basic_widgets,
    layouts,
    signals_slots,
    file_dialogs,
)

FEATURE_MAP = {
    "basic_widgets": basic_widgets.create_demo,
    "layouts": layouts.create_demo,
    "signals_slots": signals_slots.create_demo,
    "file_dialogs": file_dialogs.create_demo,
}

def main(argv=None):
    parser = argparse.ArgumentParser(description="PySide6 feature demos")
    parser.add_argument(
        "--demo",
        choices=FEATURE_MAP.keys(),
        default="basic_widgets",
        help="Select which demo widget to display",
    )

    args = parser.parse_args(argv)

    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle(config.APP_NAME)
    window.resize(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

    demo_widget = FEATURE_MAP[args.demo]()
    window.setCentralWidget(demo_widget)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()