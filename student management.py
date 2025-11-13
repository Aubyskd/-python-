#这是一个可以进行简单互动的学生信息管理系统
#你可以继续添加别的功能，比如展示所有的已经输入的学生的名单
#你可以通过这个很好的复习面向对象编程


print("===  学生信息管理系统 ===")
print("1.添加学生")
print("2.查询学生")

class STUDENT:
    # 学生信息初始化，保留addition 命名
    def __init__(self,name,number,age,major,py_score,math_score,eng_score):
        self.addition(name,number,age,major,py_score,math_score,eng_score)
    #学生信息添加
    def addition(self,name,number,age,major,py_score,math_score,eng_score):
        self.name=name
        self.number=number
        self.age=age
        self.major=major
        self.py_score=py_score
        self.math_score=math_score
        self.eng_score=eng_score
        self.total=self.total_score()
        self.average=self.average_score()
    def total_score(self):
        return self.py_score+self.math_score+self.eng_score
    def average_score(self):
        return round(self.total/3,2)
    #学生信息显示
    def display(self):
        
        print(f"姓名: {self.name}")
        print(f"学号: {self.number}")
        print(f"年龄: {self.age}")
        print(f"专业: {self.major}")
        print(f"Python: {self.py_score}, 数学: {self.math_score}, 英语: {self.eng_score}")
        print(f"总分: {self.total}, 平均分: {self.average}")
    
class MANAGEMENT:
    # 字典存储，键设置为学号，保留原来的 addition 命名
    def __init__(self):
        self.addition()
    def addition(self):
        self.student={}
    def addi(self):
        print("\n=== 添加学生 ===")
        name=input("请输入姓名：")
        number=int(input("请输入学号："))
        age=int(input("请输入年龄："))
        major = input("请输入专业: ")
        py_score = float(input("请输入Python成绩: "))
        math_score = float(input("请输入数学成绩: "))
        eng_score = float(input("请输入英语成绩: "))

        set_new=STUDENT(name,number,age,major,py_score,math_score,eng_score)

        # 检查学号是否重复
        if number in self.student:
            print("[错误]该学号已存在，未添加！")
            return

        # 保存并显示
        self.student[number]=set_new
        self.student[number].display()

        print("[提示]学生信息添加成功！")
    
    def search(self):
        print("\n=== 查询学生 ===")
        number=int(input("请输入学生学号："))
        if number in self.student:
            print("[提示]搜索到相关学生，具体信息如下:")
            self.student[number].display()
        else:
            print("[错误]未找到该学号对应的学生信息！")

    def show(self):
        while True:
            print("\n=== 学生信息管理系统 ===")
            print("1. 添加学生")
            print("2. 查询学生")

            order=int(input("请选择功能 (1-2)(按3退出):"))
            if order==1:
                self.addi()
            elif order==2:
                self.search()
            elif order==3:
                print("感谢使用，请及时反馈bug。")
                break
            else:
                print("system error,再试试吧~")

#主程序
def main():
    execute=MANAGEMENT()
    execute.show()

main()





