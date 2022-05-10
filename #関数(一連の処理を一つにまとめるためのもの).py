#関数(一連の処理を一つにまとめるためのもの)
#関数の定義
# def 関数名(引数1,引数2,...):
#   処理...
#   処理........
#   return 戻り値
#   引数:関数に渡された値
#   戻り値:関数が返す値

#関数の呼び出し
#関数名(引数1,引数2,...)
"""
def print_banana():#こういった関数を定義した
    #ここからが関数の処理部分
    print('banana')
    
print_banana()#print_bananaという関数をここで呼び出している
➡
bananaという文字が表示された
"""
#引数を定義した関数
"""
def print_text(text):#text,これが引数
    print(text)
print_text('orange')
➡orangeという文字が表示された
"""
#引数と戻り値を設定した関数
#textを引数、?を戻り値として設定する
"""
def question_text(text):
    text_q=text+'?'
    return text_q
result_text=question_text('apple')
print(result_text)
➡
apple?という文字が表示された
"""
#複数の引数と複数の戻り値を設定した関数について

"""
def average_calc(x,y):
    avg=(x+y)/2
    return avg
result=average_calc(10,12)
print(result)
➡11.0が表示
    """
#引数と戻り値は必要に応じて複数設定することが出来る
#question_exclamation_textは関数
#text1,text2は引数
#return_text1,return_text2は引数を格納した変数
#return_text1,return_text2をreturnすることで、戻り値としている
#appleがtext1に、bananaがtext2に引き渡される
#r1にreturn_text1が、r2にreturn_text2が、それぞれ代入される

"""
def question_exclamation_text(text1,text2):
    return_text1=text1+'?'
    return_text2=text2+'!'
    return return_text1,return_text2
r1,r2=question_exclamation_text('apple','banana')
print(r1)
print(r2)
➡
    apple?
    banana!という結果が表示された。
"""
"""
def average_calc(x,y):
    avg=(x+y)/2
    diff=x-y
    return avg,diff
result1,result2=average_calc(10,12)
print(result1)
print(result2)
➡
    11.0
    -2
"""
