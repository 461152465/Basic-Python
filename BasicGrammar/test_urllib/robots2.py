from urllib.robotparser import RobotFileParser

rp = RobotFileParser('http://maoyan.com/')
rp.read()
print(rp.can_fetch('*','http://maoyan.com/'))