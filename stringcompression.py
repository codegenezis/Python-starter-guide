a = "aaaabbcca"

newstring = ""

for i in a:
  # print(i)
  if i not in newstring:
    print("i value", i)
    print("count value", a.count(i))
    newstring = newstring + i + str(a.count(i))
    print(newstring)