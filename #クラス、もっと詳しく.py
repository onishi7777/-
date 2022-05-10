#クラス、もっと詳しく
"""
class SchoolReport(クラス名):
    ・インスタンス変数(オブジェクトごとに違うデータを代入)
    ・メソッド(クラスが持っている関数,計算等を処理する部分)
"""
"""
class SchoolReport(クラス名):
    def function(self):
        ↑メソッド名 ↑オブジェクト自身,第一引数
    x=10+20
    print('処理が終了')
    return x  ←普通の関数と同じ
"""
#引数とは、値の事
"""
class SchoolReport:
    def __init__(self):
    イニシャライザはクラスが持っている変数であるインスタンス変数に
    値を代入するのによく使う。
    まずデータを設定してオブジェクトを初期化する役割を持つ
        self.インスタンス変数名
"""
"""
class SchoolReport:
    def __init__(self,student_name):
        self.student_name = student_name
sr=SchoolReport('田中A')#ここで、srはオブジェクト名
print(sr.student_name) 
"""
#このインスタンス変数にオブジェクト側からアクセスするとき
#オブジェクト名.インスタンス変数名のように書く
"""
class SchoolReport:
    def __init__(self,student_name,
                 math_score,jp_score,en_score):
        self.student_name=student_name
        self.math_score=math_score
        self.jp_score=jp_score
        self.en_score=en_score
    def calc_avg_score(self):
        sum_score=(self.math_score
                   +self.jp_score+self.en_score)
        avg_score=sum_score/3
        return avg_score
sr_a=SchoolReport('田中A',100,30,50)
avg_a=sr_a.calc_avg_score()
print(f'Aさんの三教科平均点:{avg_a}')

sr_b=SchoolReport('田中B',101,31,53)
avg_b=sr_b.calc_avg_score()
print(f'Bさんの三教科平均点:{avg_b}')
"""
#インスタンス変数...オブジェクトごとに違う値
#            オブジェクト名.インスタンス変数名(オブジェクトからアクセス)
#            self.インスタンス変数名(メソッド内からアクセス)
#クラス変数...オブジェクト同士で共通の値
#             クラス名.クラス変数名(外からアクセス)
#              self.クラス変数名(メソッド内からアクセス)
#メソッド内の一時的な変数...sumやavg_score等はselfをつけないし、
# 外からアクセス出来ない
"""
class SchoolReport:
    school_name='サプー中学校'
    #↑のものは、クラス変数名=値、という感じで設定
    #クラス変数名←オブジェクトで共通
    #クラス変数は、クラス名のすぐ下に書くのが一般的
    #クラス変数は、インスタンス変数と違って、self.をつけない
    #SchoolReport.school_name←クラス変数にアクセスするとき"""
"""
class SchoolReport
    school_name='サプー中学校'
    def __init__(self,student_name):
        self.student_name=student_name
sr_a=SchoolReport('田中A')
print(sr_a.school_name)
SchoolReport.school_name='サプー高校'
print(sr_a.school_name)
"""
  