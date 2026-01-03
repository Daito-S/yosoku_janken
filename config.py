import os
import sys


WIDTH, HEIGHT = 800, 600

# <-----色----->
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)

# <-----パス----->
# ''' BASE_PATH を実行環境に応じて切り替える関数等
# '''
# if getattr(sys, 'frozen', False):
#   # PyInstallerでビルドされた実行ファイルからの実行時
#   BASE_PATH = sys._MEIPASS
# else:
#   # 通常のPythonスクリプトとして実行時
#   BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # ファイルのパス
# def resource_path(relative_path):
#   return os.path.join(BASE_PATH, relative_path)

''' パス
'''
# フォント
font_path = "assets/fonts/ipaexm.ttf"

