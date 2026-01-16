import os
import sys

# <-----スクリーン----->
WIDTH, HEIGHT = 800, 600
LEFT_WIDTH = WIDTH * 0.65
RIGHT_WIDTH = WIDTH * 0.35

# <-----色----->
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# <-----手のボタン----->
button_W, button_H = 32, 51

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
# ---フォント---
font_path = "assets/fonts/ipaexm.ttf"

# ---ボタン---
start_path = ["assets/images/starts/start_0.png",
              "assets/images/starts/start_1.png"]
# じゃんけんの手
rock_path = ["assets/images/rock/rock_0.png",
             "assets/images/rock/rock_1.png"]

scissors_path = ["assets/images/scissors/scissors_0.png",
             "assets/images/scissors/scissors_1.png"]

paper_path = ["assets/images/paper/paper_0.png",
             "assets/images/paper/paper_1.png"]

# AIのレベル
level1_path = ["assets/images/ai_level/level1/level1_0.png",
               "assets/images/ai_level/level1/level1_1.png"]

level2_path = ["assets/images/ai_level/level2/level2_0.png",
               "assets/images/ai_level/level2/level2_1.png"]

level3_path = ["assets/images/ai_level/level3/level3_0.png",
               "assets/images/ai_level/level3/level3_1.png"]
