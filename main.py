import sys
import pygame as pg

import config as cf
from enums import Hand
from button import Button

def main():
  # <-----初期設定----->
  pg.init()
  screen = pg.display.set_mode((cf.WIDTH, cf.HEIGHT))
  pg.display.set_caption('予測じゃんけん')

  clock = pg.time.Clock()
  running = True

  # ---フォント---
  font = pg.font.Font(cf.font_path, 30)

  # ---ボタン---
  button_hand_group = pg.sprite.Group()
  button_rock = Button(cf.rock_path, 100, 400, Hand.ROCK)
  button_hand_group.add(button_rock)


  # <-----メインループ----->
  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False

      # クリック
      if event.type == pg.MOUSEBUTTONDOWN:
        mouse_pos = event.pos

    # ---画面描画---
    screen.fill(cf.WHITE)
    pg.draw.line(screen, cf.GRAY, (cf.LEFT_WIDTH, 0),
                 (cf.LEFT_WIDTH, cf.HEIGHT), 3)

    button_hand_group.draw(screen)

    hello_world = font.render("Hello World!", True, (0, 0, 0))
    screen.blit(hello_world, (40, 40))

    pg.display.update()
    clock.tick(60)

  pg.quit()
  sys.exit()

if __name__ == '__main__':
  main()
