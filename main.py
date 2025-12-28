from ai.simple_ai import Simple_ai
from hand_enum import Hand

ai_simple = Simple_ai() 
hand_dict = {'グー':Hand.ROCK, 'チョキ':Hand.SCISSORS, 'パー':Hand.PAPER}

for i in range(10):
  x = input("グー、チョキ、パー　を入力してください。")

  ai_hand = [k for k, v in hand_dict.items() if v == ai_simple.prediction()][0]
  print(f'AI：{ai_hand}')
  print()
  ai_simple.learn(hand_dict[x])
