#IF文について
"""x=10
if x==10:  #ここにコロン:を忘れないこと
    print('これは10です')"""

#条件に付いて
"""
x=10
print(x==10)
print(x==9)
    ➡True
    　Falseが帰ってきました。"""
     
#大小の比較に、条件文はよく使われる。
"""
a=10
b=9
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
   
   ➡False
    True
    True
    True
"""
#orとandについて
"""
x=10
y=9
print(x>=10 or y>=10) #orはまたは
print(x>=10 and y>=10)#andはかつ
➡
True
Falseという結果"""

#notを使った式
"""
x=10
print(x>=10)
print(not x>=10) #つまり、x<10ということ
➡
True
False
"""
#ifとelse文を使ってみる
"""
x=9
if x==10: #セミコロン:をifの後に絶対忘れないこと
    print('これは10です')
else: #セミコロン:を忘れないこと
    print('これは10ではありません')
➡
これは10ではありません"""

#elif文を使ってみる
"""
x=9
if x==10:
    print('これは10です')
elif x==9:
    print('これは9です')
else:
    print('これは10でも9でもありません')
➡
これは9です
"""
