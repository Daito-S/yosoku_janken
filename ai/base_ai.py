# どのAIでも共通されるメソッドを定義して後に継承する

class Base:
  def learn(self, player_hand):
    # ここでプレイヤーの手を学習する
    raise NotImplementedError # 継承先で実装しないとエラーになるようにする

  def prediction(self):
    # ここで次の手を予測して勝てる手を返す
    raise NotImplementedError  # 継承先で実装しないとエラー
