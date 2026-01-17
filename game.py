import pygame as pg

import config as cf
from enums import Hand, Judge_result
from judge import judge
from button import Button, Title_button, Ai_hand_img
from ai.simple_ai import Simple_ai
from ai.markov_ai import Markov_ai


def game(running, title_running, AI_LEVEL, fonts, screen, clock):
  # <-----初期設定----->

  # ---文字列---
  font_L, font_M, font_S = fonts

  text_you = font_L.render("YOU", True, (0, 0, 0))
  text_ai = font_L.render("AI", True, (0, 0, 0))
  text_result = font_L.render("RESULT", True, (0, 0, 0))
  text_judge = [font_L.render("WIN", True, (0, 0, 0)),
                font_L.render("LOSE", True, (0, 0, 0)),
                font_L.render("DRAW", True, (0, 0, 0))]
  text_judgement_count = None

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

  # タイトル画面に戻るためのボタン
  button_back_title = Title_button(cf.reset_path, 580, 450, None)

  # ---AIの決定(仮)---
  if AI_LEVEL == 1:
    AI = Simple_ai()
  elif AI_LEVEL == 2:
    AI = Markov_ai()
  elif AI_LEVEL == 3:
    AI = Simple_ai()      # --------要修正---------

  # ---変数---
  AI_hand = None
  # プレイヤーの手
  player_hand = None
  # 勝敗
  judgement = None
  # 勝敗のカウント
  judgement_count = {Judge_result.WIN: 0,
                     Judge_result.LOSE: 0,
                     Judge_result.DRAW: 0}

  # 一回の手でAIが連続して学習、予測しないようにするための変数
  READY = False
  # クリック
  clicked = False

  # <-------メインループ------->
  while not title_running:
    for event in pg.event.get():
      # 終了イベント
      if event.type == pg.QUIT:
        running = False
        title_running = True

      # クリック
      if event.type == pg.MOUSEBUTTONDOWN:
        # リセットボタン(タイトルに戻る)
        if button_back_title.check_clicked(event.pos):
          title_running = True
        # プレイヤーの手を調べる
        if not READY:
          if button_rock.check_clicked(event.pos):
            player_hand = button_rock.hand
            READY = True
          elif button_scissors.check_clicked(event.pos):
            player_hand = button_scissors.hand
            READY = True
          elif button_paper.check_clicked(event.pos):
            player_hand = button_paper.hand
            READY = True

    # クリックしていなくてもマウス位置を取得
    mouse_pos = pg.mouse.get_pos()

    # -------更新-------

    # AIの手を決める・勝敗判定
    if READY:
      AI_hand = AI.prediction()

      judgement = judge(player_hand, AI_hand)
      judgement_count[judgement] += 1

      AI.learn(player_hand)
      READY = False

    button_hand_group.update(mouse_pos)
    ai_hand_group.update()

    # ------画面描画------

    screen.fill(cf.WHITE)
    pg.draw.line(screen, cf.GRAY, (cf.LEFT_WIDTH, 0),
                 (cf.LEFT_WIDTH, cf.HEIGHT), 3)

    button_hand_group.draw(screen)
    for sprite in ai_hand_group:
      sprite.draw(screen, AI_hand)

    button_back_title.draw(screen)

    # ---文字列---
    screen.blit(text_you, (220, 550))
    screen.blit(text_ai, (240, 7))
    screen.blit(text_result, (580, 10))

    if judgement != None:
      screen.blit(text_judge[judgement.value], (220, 220))

    # 勝敗のカウント
    count_str = [
      font_M.render(f"WIN: {judgement_count[Judge_result.WIN]}", True, (0, 0, 0)),
      font_M.render(f"LOSE: {judgement_count[Judge_result.LOSE]}", True, (0, 0, 0)),
      font_M.render(f"DRAW: {judgement_count[Judge_result.DRAW]}", True, (0, 0, 0))]
    for i, text in enumerate(count_str):
      screen.blit(text, (540, 90 + i * 50))

    pg.display.update()
    clock.tick(60)

  return running, title_running
