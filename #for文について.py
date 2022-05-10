#for文について
#for文の構文
#for 変数 in 繰り返しオブジェクト:➡処理
#ここでいう繰り返しオブジェクトは、リスト、辞書、range等である
"""
x_list=[100,190,2980]
for x in x_list:
    x_yen=str(x)+'円'
#数値型x_yenはstr()をつけると文字列になる
#文字列型に変換してから+を使って結合すると良い
    print(x_yen)
#なぜ100円,190円,2980円のような結果になったのか
#x_listの数値が一つずつxに代入されるから、
#x_yen=str(x)+円で、100+円,290+円のようになる
"""
#辞書の場合
#辞書の場合は、inの後に辞書.items()をつけなければいけない
#辞書は、keyと値(value)2つの変数があるものだった
"""
x_dict={'apple':100,'banana':350}
for key,value in x_dict.items():
    text=key+'は'+str(value)+'円です'
    print(text)
➡
appleは100円です
bananaは350円ですという結果が表示されました.
"""
#rangeは連番の整数を作れるもの,
#回数が決まっているfor文を使いたいときはrange
"""
for x in range(10): #for文の後にもコロン:を忘れない
    print(x)
➡
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
"""
#文章の場合
"""
for x in range(10):
    print('プリント文')
➡
    プリント文
    プリント文
    プリント文
    プリント文
    プリント文
    プリント文
    プリント文
    プリント文
    プリント文
    プリント文
"""
#リストの要素に対して繰り返し処理を行う場合の書き方 
"""
x_list=[10,22,70,-2]
for x in x_list:
    x_twice=x*2
    print(x_twice)
➡
    20
    44
    140
    -4
""" 
#あんまり良くわからない。。。
"""
x_dict={'りんご':150,'バナナ':300,'オレンジ':100}
for k, v in x_dict.items():
    print(k,v)
➡
    りんご 150
    バナナ 300
    オレンジ 100
"""
#あんまりよくわからない
"""
for i in range(3):
    print(i)
    print('for文の1行目の行')
    print('for文の2行目の行')
    break
    print('for文の3行目の行')
➡
    0
    for文の1行目の行
    for文の2行目の行
"""
#何が起きた？？
"""
for i in range(3):
    print(i)
    print('for文の1行目の行')
    print('for文の2行目の行')
    continue
    print('for文の3行目の行')
➡
0
for文の1行目の行
for文の2行目の行
1
for文の1行目の行
for文の2行目の行
2
for文の1行目の行
"""



