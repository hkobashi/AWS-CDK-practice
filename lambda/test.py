"""
問題URL:https://paiza.jp/challenges/533/show
"""

# 人数と左端の人の個数の値を受け取る
input_line_1 = list(map(int, input().split()))
N = input_line_1[0]

# 各人における「各人とその両隣の総和」を受け取る
sums_list = list(map(int, input().split()))
if sums_list != N:
  # 左から1,2番目の人の所持数を格納
  possession_list =[input_line_1[1]] # 入力1行目の2番目の値を配列possession_listに追加
  possession_list.append(sums_list[0] - possession_list[0]) 

  num = 0 # 順番を変数化
  for sum in range(len(sums_list)-2): # 求めたい値のうち2つはリストに格納済みのためループ回数を減らす
    num += 1 # 
    possession = sums_list[num] - possession_list[num] - possession_list[num-1] # 左端の人から合計の値を格納するための変数を定義
    possession_list.append(possession) # 算出した値をリストに格納

  # リストに格納した値を加工
  possession_list=[str(pos) for pos in possession_list]
  possession_list=" ".join(possession_list)
  print(possession_list)