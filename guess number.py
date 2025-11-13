import random

print("=== 欢迎来到猜数字游戏！===")
print("我已经想好了一个1到10之间的数字，你能猜出来吗？")

#设置初始数字,初始轮数
answer=random.randint(1,10)
attempt=0

#提示输入
while True:
    guess=int(input("请输入你的猜测: "))
    attempt+=1
    if guess==answer:
        print("猜对了！")
        print(f"你总共猜了{attempt}次!")
        break
    if guess>answer:
        print("猜大了，再试试！")
        print()
    else:
        print("猜小了，再试试！")
        print()