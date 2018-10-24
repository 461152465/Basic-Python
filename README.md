


# why choose to learn python

 - 爬虫
 - PyGame
	 - 俄罗斯方块
	 - FlappyBird
	 - 坦克大战
 - 机器学习

# prepare work

- [x] 安装Anaconda：C:\ProgramData\Anaconda3
- [x] 安装Python：Python 3.5.4
- [x] 安装pip 3.5
- [x] 安装MongoDB 3.4：C:\MongoDB\Server\3.4\
- [x] 安装 robo3t（MongoDB可视化工具）： C:\Program Files\Robo 3T 1.2.1
- [x] 安装Reids ： C:\Program Files\Redis\
- [x] 安装Redis Desktop Manager （Redis可视化工具）： C:\Program Files (x86)\RedisDesktopManager


### MongoDB

>MongoDB是非关系型数据库

 - 配置

```cmd 
mongod --bind_ip 0.0.0.0 --logpath C:\MongoDB\Server\3.4\data\logs\mongo.log --logappend --dbpath C:\MongoDB\Server\3.4\data\db --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install
```

 ### Python库

  - [x] 更换pip源
  - [x] urilib re
  - [x] request
  - [x] selenium + ChromeDriver(已放在Anaconda目录下)
  - [x] phantomjs（相对于ChromeDiver没有视图界面）
  - [x] lxml
  - [x] beautifulsoup （网页解析库，依赖于lxml）
  - [x] pyquery（类似于jQuery的解析库）
  - [x] pymysql （连接MySQL）
  - [x] pymongo
  - [x] redis
  - [x] flask
  - [x] django
  - [x] jupyter （支持Markdown，可以在线运行Python代码）


 # Spider

 ## Steps

 - 通过Http库发送Request请求
 - 获取Response相应
 - 解析内容 
	 - json
	 - 正则表达式
	 - beautifulsoup
	 - pyquery
	 - xpath



### 抓取图片Demo

```python 
import requests
response = requests.get('url')
with open('路径','wb') as f:
	f.write(reponse.content)
	f.close()
```

### 解决JavaScript渲染

 - 分析Ajax请求（返回结果为JSON）
 - Selenium/WebDriver
 - Splash
 - PyV8、Ghost.py

### 数据存储

 - 纯文本、JSON、XML、
 - MySQL
 - 非关系型数据库
 - 二进制文件（图片视频）

## Urllib库

 - Urllib是Python内置库
	 - urllib.request 请求
	 - urllib.error 异常处理
	 - urllib.parse url解析
	 - urllib.robotparser





 

 
