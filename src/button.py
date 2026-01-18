import pygame as pg

import src.config as cf
from src.enums import Hand, Button_status, Button_status_click

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
    self.y = y
    # 手
    self.hand = hand
    # ステータス
    self.status = Button_status.NORMAL
    self.status_click = Button_status_click.UNCLICKED

  def check_clicked(self, pos):
    # クリックした位置が自分の範囲内にあるか調べる
    if self.rect.collidepoint(pos):
      self.status_click = Button_status_click.CLICKED
      return True
    else:
      self.status_click = Button_status_click.UNCLICKED
      return False

  def mouse_on(self, pos):
    # マウスが自分の範囲内にあるか見る
    if self.rect.collidepoint(pos):
      self.status = Button_status.MOUSE_ON
    else:
      self.status = Button_status.NORMAL
      self.status_click = Button_status_click.UNCLICKED

  def update(self, pos):
    # 自身の手が選択されたら大きめに前に出す
    if self.status_click == Button_status_click.CLICKED:
      self.image = self.images[0]
      self.rect.y = self.y - 45
      self.status_click = Button_status_click.CLICKED_WAIT
    else:
      # 色を反転・少し前に出す
      self.mouse_on(pos)
      if self.status == Button_status.MOUSE_ON:
        self.image = self.images[1]
        if self.status_click == Button_status_click.CLICKED_WAIT:
          self.rect.y = self.y - 45
        else:
          self.rect.y = self.y - 15
      else:
        self.image = self.images[0]
        if self.status_click == Button_status_click.CLICKED_WAIT:
          self.rect.y = self.y - 45
        else:
          self.rect.y = self.y

  def draw(self, screen):
    screen.blit(self.image, self.rect)


# タイトルのボタンのクラス
class Title_button(pg.sprite.Sprite):
  def __init__(self, images_path, x, y, level):
    super().__init__()
    # 画像
    self.images = []
    for i in images_path:
      img = pg.transform.scale(pg.image.load(i).convert_alpha(),(cf.title_button_W * 6, cf.title_button_H * 6))
      self.images.append(img)

    self.image = self.images[0]
    self.width, self.height = self.image.get_size() # (width,height)

    # 矩形
    self.rect = pg.Rect(x, y, self.width, self.height) # x,yは左,上
    self.y = y
    # ステータス
    self.level = level

  def check_clicked(self, pos):
    # クリックした位置が自分の範囲内にあるか調べる
    if self.rect.collidepoint(pos):
      return True
    else:
      return False

  # 注意 -> 他のクラスと処理が違う
  def mouse_on(self, pos):
    # マウスが自分の範囲内にあるか見る
    if self.rect.collidepoint(pos):
      return True
    else:
      return False

  def update(self, level, mouse_pos):
    # self.levelがちゃんと数字の時
    if self.level != None:
      if level == self.level:
        self.image = self.images[1]
      else:
        self.image = self.images[0]
    # Noneならマウスの位置を見て色を反転
    else:
      if self.mouse_on(mouse_pos):
        self.image = self.images[1]
      else:
        self.image = self.images[0]

  def draw(self, screen):
    screen.blit(self.image, self.rect)


# AIの手(ボタンではない)
class Ai_hand_img(pg.sprite.Sprite):
  def __init__(self, images_path, x, y, hand):
    super().__init__()
    # 画像
    self.images = []
    for i in images_path:
      img = pg.transform.scale(pg.image.load(
          i).convert_alpha(), (cf.button_W * 3, cf.button_H * 3))
      # 回転
      img = pg.transform.rotate(img, 180)
      self.images.append(img)

    self.image = self.images[0]
    self.width, self.height = self.image.get_size()  # (width,height)

    # 矩形
    self.rect = pg.Rect(x, y, self.width, self.height)  # x,yは左,上
    # 手
    self.hand = hand
    # ステータス
    self.status = Button_status.NORMAL

  def draw(self, screen, ai_hand):
    if ai_hand == self.hand or ai_hand is None:
      screen.blit(self.image, self.rect)
