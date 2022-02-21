
#append to a dicitionary
words = ['data', 'science', 'machine','learing']
values = [5,3,1,8]
a={}
for i in range(len(words)):
  a[words[i]] = values[i]

print("result", a)
