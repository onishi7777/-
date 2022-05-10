#tqdm, zip, enumerateなどfor文で使うと便利な関数
#tqdmとは？
#for文などの繰り返し処理で進捗を表すポログレスバーを表示する関数
"""from tqdm import tqdm
for x in tqdm([10,11,12]):
    print(x)
    """
#zip関数とは？
#複数の繰り返しオブジェクトから一つずつ順番に要素を取り出して
#一つにまとめる満数
"""
sales_2020=[400238,560213,542490]
sales_2019=[489028,400123,442489]
for current,previous in zip(sales_2020,sales_2019):
    result=(current/previous-1)*100
    print(f'{result:.2f}%')
"""
#  :.2fについて、
# これはresultの値を小数点第二位まで表示させるということ
"""
➡
    -18.16%
    40.01%
    22.60%このように表示されました。
"""
#enumerateとは
#繰り返しオブジェクトの要素と、
# そのカウントのタプルを要素に持つオブジェクトを作る関数
#下のコードで、
#enumerate(names)とだけすると、i=0から始まっていく
#そのため、start=1というように代入する
"""
names=['鈴木','斎藤','大川']
for i,n in enumerate(names,start=1):
    print(f'{i}位{n}')
➡
    1位鈴木
    2位斎藤
    3位大川 のように書ける
"""