from ai.simple_ai import Simple_ai
from ai.markov_ai import Markov_ai
from enums import Hand

def janken():
  for i in range(10):
    x = input("グー、チョキ、パー　を入力してください。")
    assert x in hand_dict, "グー・チョキ・パーと違うね？"

    ai_hand = [k for k, v in hand_dict.items() if v == AI.prediction()][0]
    print(f'AI：{ai_hand}')
    print()
    AI.learn(hand_dict[x])
  print(AI.record)

hand_dict = {'グー': Hand.ROCK, 'チョキ': Hand.SCISSORS, 'パー': Hand.PAPER}

'''メイン処理'''
# AIの種類を決定
ai_num = input('シンプル：1, マルコフ：2を入力')
if ai_num == "1":
  AI = Simple_ai()
elif ai_num == "2":
  AI = Markov_ai()

janken()

if input('続けるなら入力せずEnter') == "":
  janken()
