import urllib.request

response = urllib.request.urlopen('http://www.python.org')
print(response.read().decode('utf-8'))
print(type(request))

# print(type(1))
# print(type('me'))