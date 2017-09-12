from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)

user_whether_list = []

def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': 'ive1e1zd9xufhvo7',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=3)
    output = result.json()
    state = output['results'][0]['now']['text']
    temperature = output['results'][0]['now']['temperature']
    time = output['results'][0]['last_update'][:-6].replace("T"," ")
    weather_str = '【地点】%s\n【天气】%s\n【温度】%s℃\n【查询时间】%s' %(location, state, temperature, time)
    return weather_str
    
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')
    
@app.route('/user_request', methods=['GET','post']) 
def order_request():
    try:
        if request.args.get('help')=="帮助":
            return render_template('help.html')
        elif request.args.get('find')=="查询":
            city = request.args.get('city')
            if city == '':
                return render_template('empty.html')
            else:
                weather = fetchWeather(city)
                user_whether_list.append(weather)
                return render_template('city.html',weather=weather)
        elif request.args.get('history')=="历史":
            return render_template('history.html',history=user_whether_list)
    except KeyError:
        return render_template('error.html')
        
if __name__ == '__main__':
    app.run(debug=True)
