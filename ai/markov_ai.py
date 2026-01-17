''' 
  マルコフ連鎖を使ったAI
  プレイヤーが、何の手の次に、何の手を出したかを記録して
  (手を出した後、次はどの手に変えるかについての確率を調べて)
  今出した手から次の手を予測する
'''
from random import randint

from ai.base_ai import Base
from enums import Hand


class Markov_ai(Base):
  def __init__(self):
    self.record = {
        Hand.ROCK: {Hand.ROCK: 0, Hand.SCISSORS: 0, Hand.PAPER: 0},  # グーから次の手
        # チョキから次の手
        Hand.SCISSORS: {Hand.ROCK: 0, Hand.SCISSORS: 0, Hand.PAPER: 0},
        Hand.PAPER: {Hand.ROCK: 0, Hand.SCISSORS: 0,
                     Hand.PAPER: 0}  # パーから次の手の記録
    }
    self.hand_list = [Hand.ROCK, Hand.SCISSORS, Hand.PAPER]
    self.last_player_hand = None

  def learn(self, player_hand):
    if self.last_player_hand != None:  # 前の手があるとき記録
      self.record[self.last_player_hand][player_hand] += 1
    self.last_player_hand = player_hand  # 前の手を更新

  def prediction(self):
    # 一回目は記録できない、予測できないのでとりあえずランダムで手を出す
    if self.last_player_hand == None:
      return self.hand_list[randint(0, 2)]
    # 次のプレイヤーの手を予測
    predicted = max(self.record[self.last_player_hand],
                    key=self.record[self.last_player_hand].get)

    # 勝てる手を返す
    return self.hand_list[predicted.value - 1]
