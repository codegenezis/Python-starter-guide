# count is used to take the number of occurance in the strng

# a ="aabbbbcccc"
a = "aabbac"
# method 1
# print(a.count("a"))

# method2
newstring = ""
count = 1
for i in range(len(a)-1):
  if a[i] == a[i+1]:
    count = count + 1
  else:
    newstring = newstring + a[i] + str(count)
    count = 1
newstring = newstring + a[i+1] + str(count)
print(newstring)
#output = a2b4c4  