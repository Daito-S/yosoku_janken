''' 
  N-gramを使ったAI(2-gram)
  マルコフ連鎖を強化したイメージで"グー,チョキと出した次はパーを出しがち"
  のように二つの手の次に何を出すか予測するのでマルコフ連鎖よりプレイヤーの癖を掴める
'''
from collections import defaultdict
from random import randint

from ai.base_ai import Base
from enums import Hand

class Ngram_ai(Base):
  def __init__(self):
    # patterns[(手1, 手2)][次の手] = 回数
    self.patterns = defaultdict(
        lambda: {Hand.ROCK: 0, Hand.SCISSORS: 0, Hand.PAPER: 0})
    self.record = []
    self.hand_list = [Hand.ROCK, Hand.SCISSORS, Hand.PAPER]

  def learn(self, player_hand):
    self.record.append(player_hand) # 記録

    # 3手以上あるときパターンを記録
    if len(self.record) >= 3:
        key = (self.record[-3], self.record[-2])  # 直前2手
        next_hand = self.record[-1]                # 今回の手
        self.patterns[key][next_hand] += 1

  def prediction(self):
    # 記録が少ないと予測できないのでランダムで手を出す
    if len(self.record) < 2:
      return self.hand_list[randint(0, 2)]

    key = (self.record[-2], self.record[-1])

    # 未知のパターンなのでランダム
    if key not in self.patterns:
      return self.hand_list[randint(0, 2)]

    # 次のプレイヤーの手を予測
    next_counts = self.patterns[key]
    predicted = max(next_counts, key=next_counts.get)

    # 勝てる手を返す
    return self.hand_list[predicted.value - 1]
