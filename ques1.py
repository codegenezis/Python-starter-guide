list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

#logic 1:
for i in range(len(list1)):
  print(list1[i], list2[len(list1)-1 -i])

#logic2:

newlist = (list(zip(list1, list2[::-1])))
print(newlist)
for i,j in newlist:
  print(i,j)

# the ecpecte output should be 
# 10 400
# 20 300
# 30 200
# 40 100
