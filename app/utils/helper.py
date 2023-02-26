import os
import sys

def get_resource_path(relative_path):
    """相対パスからリソースの絶対パスを取得する"""
    try:
        # PyInstallerでパッケージ化されたアプリの場合
        base_path = sys._MEIPASS
    except Exception:
        # 通常のPythonスクリプトの場合
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
