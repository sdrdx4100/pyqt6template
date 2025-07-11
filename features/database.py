from PySide6.QtSql import QSqlDatabase, QSqlQuery

def connect_db(path: str):
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(path)
    db.open()
    return db