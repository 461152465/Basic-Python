from urllib import request,parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host' : 'httpbin.org'
}
dict = {
    'name' : 'mio',
    'passowrd' : '123456'
}
method='POST'

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method=method)
response = request.urlopen(req)
print(response.read().decode('utf-8'))