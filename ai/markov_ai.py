''' 
  マルコフ連鎖を使ったAI
  プレイヤーが、何の手の次に、何の手を出したかを記録して
  (手を出した後、次はどの手に変えるかについての確率を調べて)
  今出した手から次の手を予測する
'''
from ai.base_ai import Base
from hand_enum import Hand

class Markov_ai(Base):
  def __init__(self):
    self.record = {
      Hand.ROCK:{Hand.ROCK:0, Hand.SCISSORS:0, Hand.PAPER:0},
      Hand.SCISSORS:{Hand.ROCK:0, Hand.SCISSORS:0, Hand.PAPER:0},
      Hand.PAPER:{Hand.ROCK:0, Hand.SCISSORS:0, Hand.PAPER:0}
    }
    self.last_player_hand = None