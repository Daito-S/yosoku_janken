from enum import Enum

class Hand(Enum):
  ROCK = 0
  SCISSORS = 1
  PAPER = 2

class Button_status(Enum):
  NORMAL = 0
  MOUSE_ON = 1
  CLICKED = 2