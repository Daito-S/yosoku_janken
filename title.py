import sys
import pygame as pg

import config as cf
from button import Button

def title():
  # <-----初期設定----->

  # -----文字列-----
  text_title = font.L.render("予測じゃんけん", True, (0, 0, 0))
  # -----ボタン-----
  button_group = pg.sprite.Group()
  # スタートボタン
  button_start = Button(cf.start_path, 300, 400, None)
  button_group.add(button_start)
  # AIレベル選択ボタン
  button_level1 = Button(cf.level1_path, 150, 300, None)
  button_level2 = Button(cf.level2_path, 350, 300, None)
  button_level3 = Button(cf.level3_path, 550, 300, None)
  button_group.add(button_level1)
  button_group.add(button_level2)
  button_group.add(button_level3)
