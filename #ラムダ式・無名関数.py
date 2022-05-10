#ラムダ式・無名関数
#ラムダ式の書き方
#lambda 引数:処理
#引数を複数設定したい場合は
#lambda 引数1,引数2:処理
#例　lambda x: print(x+'!')
#この関数オブジェクトは変数に代入できる
#ラムダ式で作った関数オブジェクトをfuncという変数に代入できる
#func=lambda x: print(x+'!')
"""
func = lambda x,y: print(f'{x}さんは{y}です')
func('鈴木','学生')
"""
#ラムダ式無名関数は、ほかの関数と組み合わせて使う
#map関数とかfilter関数など

#map関数...
# 繰り返しオブジェクトのすべての要素にある処理を行う関数
#書き方
#map(関数,繰り返しオブジェクト) この関数をラムダ式で直接書く
"""
names=['鈴木','斎藤','田中']
result=list(map(lambda x:x+'さん',names))
print(result)
"""
"""
n1=['鈴木','斎藤','田中']
n2=['めい','ゆづき','ひなた']
result=list(map(lambda x,y:x+y+'さん',n1,n2))
print(result)
"""

#filter関数とは
#繰り返しオブジェクトの中である条件が,
#Trueになる要素だけを抽出する関数
#filter(関数,繰り返しオブジェクト)という風に書く
numbers=[5,8,10,12,30]
result=list(filter(lambda x: x>=10,numbers))
print(result)
