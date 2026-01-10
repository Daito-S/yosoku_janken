import sys
import pygame as pg

import config as cf
from enums import Hand
from button import Button, Ai_hand_img
from ai.simple_ai import Simple_ai
from ai.markov_ai import Markov_ai

def main():
  # <-----初期設定----->
  pg.init()
  screen = pg.display.set_mode((cf.WIDTH, cf.HEIGHT))
  pg.display.set_caption('予測じゃんけん')

  clock = pg.time.Clock()
  running = True

  # ---フォント---
  font = pg.font.Font(cf.font_path, 40)

  # ---文字列---
  text_you = font.render("YOU", True, (0, 0, 0))
  text_ai = font.render("AI", True, (0, 0, 0))
  text_ai_hand = font.render("", True, (0, 0, 0))

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

  # ---AIの手の画像---
  ai_hand_group = pg.sprite.Group()
  # グー
  ai_rock_img = Ai_hand_img(cf.rock_path, 45, 50, Hand.ROCK)
  ai_hand_group.add(ai_rock_img)
  # チョキ
  ai_scissors_img = Ai_hand_img(cf.scissors_path, 215, 50, Hand.SCISSORS)
  ai_hand_group.add(ai_scissors_img)
  # パー
  ai_paper_img = Ai_hand_img(cf.paper_path, 385, 50, Hand.PAPER)
  ai_hand_group.add(ai_paper_img)

  # <-----AIの決定(仮)----->
  AI = Simple_ai()
  # プレイヤーの手
  player_hand = None

  # <-----メインループ----->
  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False

      # クリック
      if event.type == pg.MOUSEBUTTONDOWN:
        click_pos = event.pos
        clicked = True
      else:
        clicked = False

    # クリックしていなくてもマウス位置を取得
    mouse_pos = pg.mouse.get_pos()

    # ---更新---
    # プレイヤーの手を調べる
    if clicked and player_hand is None:
      if button_rock.check_clicked(click_pos):
        player_hand = button_rock.hand
      elif button_scissors.check_clicked(click_pos):
        player_hand = button_scissors.hand
      elif button_paper.check_clicked(click_pos):
        player_hand = button_paper.hand
      else:
        player_hand = None

    # AIの手を決める
    if player_hand is not None:
      ai_hand = AI.prediction()
      AI.learn(player_hand)

    button_hand_group.update(mouse_pos)
    ai_hand_group.update()

    # ---画面描画---
    screen.fill(cf.WHITE)
    pg.draw.line(screen, cf.GRAY, (cf.LEFT_WIDTH, 0),
                 (cf.LEFT_WIDTH, cf.HEIGHT), 3)

    button_hand_group.draw(screen, player_hand)
    ai_hand_group.draw(screen)

    # 文字列
    screen.blit(text_you, (220, 550))
    screen.blit(text_ai, (240, 7))

    screen.blit(text_ai_hand, (220, 250))

    pg.display.update()
    clock.tick(60)

  pg.quit()
  sys.exit()

if __name__ == '__main__':
  main()
