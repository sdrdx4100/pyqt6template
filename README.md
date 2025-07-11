# pyqt6template

## プロジェクト構成
```
/workspaces/pyqt6template/
├─ config.py
├─ main.py
├─ features/
│  ├─ __init__.py
│  ├─ basic_widgets.py
│  ├─ layouts.py
│  ├─ signals_slots.py
│  ├─ threads.py
│  ├─ network.py
│  ├─ database.py
│  ├─ styles.py
│  ├─ internationalization.py
│  ├─ multimedia.py
│  ├─ custom_widgets.py
│  └─ file_dialogs.py
└─ resources/
   └─ resources.qrc
```

## 各モジュールの役割
- **config.py**  
  アプリケーション名やウィンドウサイズなど設定値を一元管理  
- **main.py**  
  QApplication の初期化、メインウィンドウの生成と機能サンプルの呼び出し  
- **features/basic_widgets.py**  
  ボタンやラベルなど基本ウィジェットのサンプル実装  
- **features/layouts.py**  
  QHBoxLayout、QVBoxLayout、QGridLayout などレイアウト例  
- **features/signals_slots.py**  
  シグナルとスロットの接続例  
- **features/threads.py**  
  QThread を使ったバックグラウンド処理サンプル  
- **features/network.py**  
  QNetworkAccessManager による HTTP 通信例  
- **features/database.py**  
  QtSql を使った SQLite 接続とクエリ実行例  
- **features/styles.py**  
  QSS を読み込んでスタイルを適用する例  
- **features/internationalization.py**  
  QTranslator を使った多言語対応例  
- **features/multimedia.py**  
  QMediaPlayer／QAudioOutput／QVideoWidget による音声・動画再生例  
- **features/custom_widgets.py**
  QPainter を使ったカスタムウィジェット作成例
- **features/file_dialogs.py**
  QFileDialog を使用したファイルの読み込み・保存の例
- **resources/**
  QSS、アイコン、リソースファイル（.qrc）などを配置

## トラブルシューティング
- ImportError: libGL.so.1: cannot open shared object file  
  システムの OpenGL ライブラリが不足しています。Debian/Ubuntu 系の場合は以下を実行してください。  
  ```bash
  sudo apt-get update
  sudo apt-get install -y libgl1-mesa-glx
  ```  
  他のディストリビューションでは相当するパッケージをインストールしてください。