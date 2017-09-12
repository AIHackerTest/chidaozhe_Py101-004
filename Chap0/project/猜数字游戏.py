from sys import exit
import random
right = random.randint(0, 20)

a = 10

print("欢迎进行猜数字游戏。")
print("游戏规则：")
print("\t*程序会自动生成一个20以内的随机数。")
print("\t*你有10次机会猜测。")
print("\t*每次会根据你的猜测情况给出提示。")
print("\t*10次没有猜中，游戏结束。")

def end():
    print("恭喜你猜对了！")
    exit(0)
    
if a > 0:
    while a != 0:
        guess = int(input("请输入一个0到20之间的整数>"))
        if guess < right:
            print("*小了,请重新猜测。")
            a = a - 1
            print("你还有 %d 次猜的机会。" % a)
        elif guess > right:
            print("*大了,请重新猜测。")
            a = a - 1
            print("你还有 %d 次猜的机会。" % a)
        else:
            end()
else:
    print("你已使用完猜测次数！")
