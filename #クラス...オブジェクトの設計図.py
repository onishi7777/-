#クラス...オブジェクトの設計図
#クラスの定義
#class クラス名:
#   def メソッド名(self,引数,...)
#   def メソッド名(self,引数,...)
#クラスが持っている関数→メソッドという
#メソッドを書くときは一つ目の引数を必ずselfにする
#selfは自分自身(インスタンス)
#クラスがそれぞれ持っている変数の事をインスタンス変数という
#インスタンスごとに違う値を持つときはインスタンス変数を使うが、
#クラスで共通した値を持つときはクラス変数を使う
#インスタンス変数とクラス変数をまとめて属性という
#インスタンス名=クラス名(引数1,...)
#引数1....はイニシャライザに渡す引数
"""
class BodyCondition:
    def bmi_calc(self):
        print('あいうえお')
        #ここまでは設計図
bc=BodyCondition()
bc.bmi_calc()
→あいうえおが表示された
"""
"""
class BodyCondition:
    def __init__(self):
        print('初期化')
    def bmi_calc(self):
        print('あいうえお')
bc=BodyCondition() 
→初期化、が表示された。
"""
#イニシャライザはインスタンス作成時に一回だけ呼ばれるので、
#一回目の処理print('初期化)しか行わなかった   
"""
class BodyCondition:
    def __init__(self,arg_weight,arg_height):
        self.weight=arg_weight
        self.height=arg_height
    def bmi_calc(self):
        print('あいうえお')
bc=BodyCondition(50,150)
#ここで、def __init__のarg_weightに50が、
# arg_heightに150が代入される
print(bc.weight)
print(bc.height)
→50
 100が表示される
 """
"""
class BodyCondition:
    def __init__(self,arg_weight,arg_height):
        self.weight=arg_weight
        self.height=arg_height
    def bmi_calc(self):
        m_height=self.height/100
        bmi=self.weight/m_height/m_height
        print(bmi)
bc=BodyCondition(50,150)#値の代入
bc.bmi_calc()#二個目のdefの処理を行った結果
→22.222222222222225
"""
"""
class Student:
    def __init__(self,arg_name):
        #__init__...イニシャライザー、コンストラクターと呼ばれる
        #インスタンスが作成されるときに一回だけ実行される
        #インスタンスを初期化するのが__init__の役割
        #このイニシャライザーにインスタンス変数の値を設定する処理は、
        #self.変数名=引数、、で表現される
        self.name=arg_name
    def print_name(self):
            print(self.name)
student=Student('斎藤')
student.print_name()
➡
斎藤が表示された
"""

"""
class Student:
    def __init__(self,arg_name):
        self.name=arg_name
    def print_name(self):
            print(self.name)
student_1=Student('斎藤')
student_1.print_name()
student_2=Student('田中')
student_2.print_name()
student_3=Student('水面')
student_3.print_name()
➡
    斎藤
    田中
    水面
"""