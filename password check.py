#这是一个密码检查器，它应该实现长度，数字个数，字母个数的三个方面的判断
#你可以继续添加判断条件和提示

print("===密码安全检查器===")

password=input("请输入你的密码：")
print("检查中……")
print()
print("检查结果：")

#初始化检查因子
check_passed=0
results=[]

#1.长度检查
length_checked=len(password)>=8
if length_checked:
    check_passed+=1
    results.append("长度检查：通过")
else:
    results.append("长度检查：不通过")

#2.数字检查
number_checked=False
for i in password:
     if i.isdigit():
        number_checked=True
        break
if number_checked:
    check_passed+=1
    results.append("数字检查：通过")
else:
    results.append("数字检查：不通过")

#3.字母检查
letter_checked=False
for i in password:
     if i.isalpha():
        letter_checked=True
        break
if letter_checked:
        check_passed += 1
        results.append("字母检查: 通过")
else:
        results.append("字母检查: 不通过")

#4.输出结果
for i in results:
     print(i)

if check_passed==0:
     strength="很不安全的密码"
     suggestions="请立刻修改密码，保证密码有至少8位，包含数字和字母的组合"
if check_passed==1:
     strength="弱密码"
     suggestions="请立刻修改密码，保证密码有至少8位，包含数字和字母的组合"
if check_passed==2:
     strength="中等密码"
     suggestions="建议使用更复杂的密码"
if check_passed==3:
     strength="强密码"
     suggestions="恭喜，密码检查通过~"

print(f"密码安全等级：{strength},{suggestions}")


#检查删改区
#删除any()，重新使用遍历
#定义False初始化，避免报错
