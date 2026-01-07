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
  font = pg.font.Font(cf.font_path, 40)

  # ---ボタン---
  button_hand_group = pg.sprite.Group()
  # グー
  button_rock = Button(cf.rock_path, 45, 400, Hand.ROCK)
  button_hand_group.add(button_rock)
  # チョキ
  button_scissors = Button(cf.scissors_path, 215, 400, Hand.SCISSORS)
  button_hand_group.add(button_scissors)
  # パー
  button_paper = Button(cf.paper_path, 385, 400, Hand.PAPER)
  button_hand_group.add(button_paper)

  # <-----メインループ----->
  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False

      # クリック
      if event.type == pg.MOUSEBUTTONDOWN:
        click_pos = event.pos

    # クリックしていなくてもマウス位置を取得
    mouse_pos = pg.mouse.get_pos()

    # ---更新---
    button_hand_group.update(mouse_pos)

    # ---画面描画---
    screen.fill(cf.WHITE)
    pg.draw.line(screen, cf.GRAY, (cf.LEFT_WIDTH, 0),
                 (cf.LEFT_WIDTH, cf.HEIGHT), 3)

    button_hand_group.draw(screen)

    text_you = font.render("YOU", True, (0, 0, 0))
    screen.blit(text_you, (220, 550))

    pg.display.update()
    clock.tick(60)

  pg.quit()
  sys.exit()

if __name__ == '__main__':
  main()
