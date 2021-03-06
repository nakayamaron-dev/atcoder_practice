# トーナメントの再帰関数 (準優勝者を返す。abc188-c)
def round(players):
    
    # インナー関数
    def _round(players):
        winners = []

        # 決勝戦は敗者を返す。
        if len(players) == 2:
            return min(players)

        # 決勝戦以外は勝者をwinnersに追加。
        for i in range(1, len(players), 2):
            winner = max(players[i-1], players[i])
            winners.append(winner)

        return _round(winners)

    return _round(players)

# 10進数をn進数に変換する。 (str)
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)