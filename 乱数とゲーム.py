#6面体のサイコロを作る
"""
import random
r=random.randint(1,6)
print(r)
➡実行するたびに結果が異なり、サイコロと同じ働きをしていることが分かる
"""
#じゃんけんゲームを作る
#1 議事乱数でコンピュータが出す手を決める
#2 ユーザーからどの手を出すのか入力してもらう
#3 どっちが勝ったか勝敗を出す
#これの繰り返しをする
import random
com=random.randint(0,2)
#0...グー、1...チョキ、2...パー
print('あなたの出す手を入力してください:a=グー、b=チョキ、c=パー')
input()
if com==0:
    a=0
    b=-1
    c=1
elif com==1:
    a=2
    b=1
    c=0
    
else:#com==2
    a=1
    b=3
    c=2
if (a|b|c)==com:
    print(com)
    print('あいこ')
elif (a|b|c)>com:
    print(com)
    print('あなたの勝ち')
else:
    print(com)
    print('あなたの負け')




