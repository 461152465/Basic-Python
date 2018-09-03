import  re
s = 'I have a dog, I have a cat'
print(re.findall(r'I have a dog|cat',s))