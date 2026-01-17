import sys
import pygame as pg

import config as cf
from button import Button

def title(running, title_running):
  # <-----初期設定----->
  # AIレベル
  AI_LEVEL = 1 # 選択されなかったら一番低いレベルのままになる
  # -----文字列-----
  text_title = font.L.render("予測じゃんけん", True, (0, 0, 0))
  text_now = font.S.render("Now", True, (0, 0, 0))
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

  # <-----タイトルのループ----->
  while title_running:
    for event in pg.event.get():
      # 終了イベント
      if event.type == pg.QUIT:
        running = False
        title_running = False

      # クリック
      if event.type == pg.MOUSEBUTTONDOWN:
        # AIのレベルのボタン
        if button_level1.check_clicked(event.pos):
          AI_LEVEL = 1
        elif button_level2.check_clicked(event.pos):
          AI_LEVEL = 2
        elif button_level3.check_clicked(event.pos):
          AI_LEVEL = 3
        # ゲームの開始のボタン
        elif button_start.check_clicked(event.pos):
          title_running = False

    # クリックしていなくてもマウス位置を取得
    mouse_pos = pg.mouse.get_pos()

    # -----更新-----
    button_group.update(mouse_pos)

    # nowの表示位置
    now_rect = (180 + 150*(AI_LEVEL - 1), 300)

    # -----描画-----
    screen.fill(cf.WHITE)

    button_group.draw(screen)
    # 文字列
    screen.blit(text_title, (300, 130))
    screen.blit(text_now, (now_rect))

    pg.display.update()
    clock.tick(60)

  return running, title_running, AI_LEVEL
