whether_dict = {}

with open('whether_info.txt') as f:
    for line in f:
        (key, val) = line.split(",")
        whether_dict[key] = val

print("您将进行一个天气查询程序，如需帮助，请输入h或help。")
#建立用户输入查询信息的字典
user_whether_dict = {}

while True:
    order = input("请输入指令或您要查询的城市名：")
    if order in ["help","h"]:
        print("\t-输入城市名，返回该城市的天气数据；")
        print("\t-输入help或h，打印帮助文档；")
        print("\t-输入history，获取历史查询信息。")
        print("\t-输入quit或exit，退出程序的交互；")
    elif order == "history":
        for order in user_whether_dict:
            print(order, user_whether_dict[order])
    elif order in ["quit","exit"]:
        break
    else:
        city = whether_dict.get(order)#判断用户输入命令是否超出设定范围。
        if not city:
            print("*您输入的指令或城市名不存在！") 
        else:
            print("%s的天气状况为：%s" %(order, whether_dict[order]))
            user_whether_dict[order] = whether_dict[order]
