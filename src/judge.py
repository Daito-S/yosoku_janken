from src.enums import Hand, Judge_result
# じゃんけんの勝敗判定の関数

def judge(player_hand, ai_hand):
  if player_hand == ai_hand:
    return Judge_result.DRAW
  
  winning_patterns = {
      Hand.ROCK: Hand.SCISSORS,    # グーはチョキに
      Hand.SCISSORS: Hand.PAPER,   # チョキはパーに
      Hand.PAPER: Hand.ROCK        # パーはグーに勝つ
  }

  if winning_patterns[player_hand] == ai_hand:
    return Judge_result.WIN
  else:
    return Judge_result.LOSE
