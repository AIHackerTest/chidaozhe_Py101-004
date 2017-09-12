# 任务：运用API查询实时天气

## 一号坑：安装Requests
- 根据大妈教练和各位学员的群聊，明白或许是Window系统本身导致的环境配置繁琐。依照网上教程一直无法顺利安装Requests，结果是花费2小时才找到**python -m pip install requests**这条命令安装成功，但依然无法通过pip安装运行。

## 二号坑：API参数传递
-  开始参照卡包推荐的心知天气注册完，得到key和ID，不知如何运用。然后就去上网查询有关API的相关知识和用法，忽略了网站提供的[demo](https://github.com/seniverse/seniverse-api-demos/blob/master/python/demo-requests.py)和参数说明，导致任务一直处于停滞状态。

> from utils.const_value import API, KEY, UNIT, LANGUAGE

> from utils.helper import getLocation

- 不知道开始的这两条命令如何使用？参数API、key、languege&unit如何设定？后来参照Leon-Huang的[What is API](https://github.com/Leon-Huang/Py101-004/blob/master/Chap2/note/README.md)才学会API的具体运用。然后编写代码实现了实时查询天气的核心功能。

## 三号坑：JSON解析数据
- 得到了实时天气信心，可数据全是连续的，无法可视化显示。通过[介绍 JSON](http://www.json.org/json-zh.html),明白JSON的功能和一种用法**return result.json()**，关于**import json**的用法还未学会。最重要的是明白运用字典解析数据，以及字典嵌套提取信息点的用法。

## 四号坑：建立嵌套字典
- 开始想到用字典保存用户查询信息，尝试建立嵌套字典，实现历史记录和查询记录同样的实现效果，但一直提示关键字无法建立。尝试多次未果（1.5小时），最终使用单个字典实现保存记录，失去历史记录和查询记录显示的一致性，之后会继续尝试解决。

## 五号坑：排除异常命令
- 完成基本功能后，考虑用户异常命令输入的问题。开始使用if...else...来判断输入命令是否存在于Web API中，但发现逻辑错误：错误信息无法与Web API中的信息进行对比判断，进而不能判断输入命令的正确与否。后阅读学员的代码，有人使用try...except...进行异常判断。网上学习并运用于自己的代码中，实现了排除异常命令的功能。

## 六号坑：温度单位转化
- 使用if...else...判断用户输入在“c”和“f”之间的选择，发现两个问题，一是unit参数在函数内部，无法将用户选择带入，二是在用户不输入“c”或“f”时，unit未设定程序无法执行。尝试0.5小时未果，暂放此功能，之后继续尝试解决。

