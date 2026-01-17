import sys
import pygame as pg

import config as cf
from button import Title_button

def title(running, title_running, fonts, screen, clock):
  # <-----初期設定----->
  # AIレベル
  AI_LEVEL = 1 # 選択されなかったら一番低いレベルのままになる
  # -----文字列-----
  font_L, font_M, font_S = fonts
  text_title = font_L.render("-------YosokuJanken-------", True, (0, 0, 0))
  text_now = font_M.render("Now", True, (0, 0, 0))
  # -----ボタン-----
  button_group = pg.sprite.Group()
  # スタートボタン
  button_start = Title_button(cf.start_path, 320, 400, None)
  button_group.add(button_start)
  # AIレベル選択ボタン
  button_level1 = Title_button(cf.level1_path, 120, 240, 1)
  button_level2 = Title_button(cf.level2_path, 320, 240, 2)
  button_level3 = Title_button(cf.level3_path, 520, 240, 3)
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
    button_group.update(AI_LEVEL, mouse_pos)

    # nowの表示位置
    now_rect = (155 + 200*(AI_LEVEL - 1), 210)

    # -----描画-----
    screen.fill(cf.WHITE)

    button_group.draw(screen)
    # 文字列
    screen.blit(text_title, (180, 110))
    screen.blit(text_now, (now_rect))

    pg.display.update()
    clock.tick(60)

  return running, title_running, AI_LEVEL
