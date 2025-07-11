from PySide6.QtCore import QTranslator, QLocale

def load_translation(app):
    translator = QTranslator()
    locale = QLocale.system().name()
    translator.load(f"i18n_{locale}.qm")
    app.installTranslator(translator)