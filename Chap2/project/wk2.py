import requests

def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': 'ive1e1zd9xufhvo7',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=1)
    return result.json()

def showWeather():  
    output = fetchWeather(order)
    city = output['results'][0]['location']['name']
    state = output['results'][0]['now']['text']
    temperature = output['results'][0]['now']['temperature']
    time = output['results'][0]['last_update'][:-6].replace("T"," ")
    
    historyWeather[order] =  "%s 的天气是 %s ,温度为 %s 摄氏度" %(city, state, temperature)
    
    print("您查询的城市；\t",city)
    print("天气状况；\t",state)
    print("温度；\t\t",temperature,"摄氏度")
    print("查询时间；\t",time)

print("您将进行一个实时天气查询程序，如需帮助，请输入h或help。")
print("*所有天气数据来自心知天气*")
user_whether_dict = {}
historyWeather = {}

while True:
    order = input("请输入指令或您要查询的城市名：")
    try:
        showWeather()
        user_whether_dict[order] = historyWeather[order]
    except KeyError:
        if order in ["help","h"]:
            print("\t-输入城市名，返回该城市的天气数据；")
            print("\t-输入help或h，打印帮助文档；")
            print("\t-输入history，获取历史查询信息。")
            print("\t-输入quit或exit，退出程序的交互；")
        elif order == "history":
            for order in user_whether_dict:
                print(user_whether_dict[order])
        elif order in ["quit","exit"]:
            break
        else:
            print("*您输入的指令或城市名不存在！") 
