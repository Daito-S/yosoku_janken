import sys
import pygame as pg

import config as cf

from game.game import game
from game.title import title


if __name__ == '__main__':
  # <-----初期設定----->
  pg.init()
  screen = pg.display.set_mode((cf.WIDTH, cf.HEIGHT))
  pg.display.set_caption('予測じゃんけん')

  clock = pg.time.Clock()
  running = True
  title_running = True

  # ---フォント---
  font_L = pg.font.Font(cf.font_path, 40)
  font_M = pg.font.Font(cf.font_path, 30)
  font_S = pg.font.Font(cf.font_path, 20)

  fonts = [font_L, font_M, font_S]

  # <-----メインループ----->
  while running:
    if title_running:
      running, title_running, AI_LEVEL = title(running, title_running, fonts, screen, clock)
    else:
      running, title_running = game(running, title_running, AI_LEVEL, fonts, screen, clock)

  pg.quit()
  sys.exit()
