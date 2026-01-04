import pygame as pg

import config as cf
from enums import Hand, Button_status

# 手を選択するのに使うボタンのクラス
class Button(pg.sprite.Sprite):
  def __init__(self, images_path, x, y, hand):
    super().__init__()
    # 画像
    self.images = []
    for i in images_path:
      img = pg.transform.scale(pg.image.load(i).convert_alpha(),(cf.button_W * 3, cf.button_H * 3))
      self.images.append(img)

    self.image = self.images[0]
    self.width, self.height = self.image.get_size() # (width,height)
    # width, height = self.width * 5, self.height * 5

    # 矩形
    self.rect = pg.Rect(x, y, self.width, self.height) # x,yは左,上
    # 手
    self.hand = hand
    # ステータス
    self.status = Button_status.NORMAL

  def check_clicked(self, pos):
    # クリックした位置が自分の範囲内にあるか調べる
    clicked = self.rect.collidepoint(pos)
    if clicked:
      self.status = Button_status.CLICKED
      return self.hand
