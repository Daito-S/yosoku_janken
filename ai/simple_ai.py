# 一番シンプルなAI
from ai.base_ai import Base
from hand_enum import Hand

class Simple_ai(Base):
  def __init__(self):
    self.record = {Hand.ROCK: 0, Hand.SCISSORS: 0, Hand.PAPER: 0}
    self.hand_list = [Hand.ROCK, Hand.SCISSORS, Hand.PAPER]

  def learn(self, player_hand):
    self.record[player_hand] += 1

  def prediction(self):
    # もっとも出しやすい手を調べる
    predicted = max(self.record, key=self.record.get)

    # 勝てる手を返す
    return self.hand_list[predicted.value - 1]  # リストのインデックスを一つずらすと勝てる手になる
