import pygame as pg
import config as cf

# <-----初期設定----->

pg.init()
screen = pg.display.set_mode((cf.WIDTH, cf.HEIGHT))
pg.display.set_caption('予測じゃんけん')