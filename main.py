import sys
import pygame as pg

import config as cf


# <-----初期設定----->
pg.init()
screen = pg.display.set_mode((cf.WIDTH, cf.HEIGHT))
pg.display.set_caption('予測じゃんけん')

clock = pg.time.Clock()
running = True

# ---フォント---
font = pg.font.Font(cf.font_path,30)

# <-----メインループ----->
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
    
    # クリック
    if event.type == pg.MOUSEBUTTONDOWN:
      mouseX, mouseY = event.pos


  # ---画面描画---
  screen.fill(cf.WHITE)

  hello_world = font.render("Hello World!", True, (0, 0, 0))
  screen.blit(hello_world, (40,40))

  pg.display.update()
  clock.tick(60)

pg.quit()
sys.exit()
