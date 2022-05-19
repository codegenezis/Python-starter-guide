a = [1,2,3,3,4,5,1,2,6,7]
print("Original list elements:", a )

res=[]
for i in a:
  if i not in res:
    res.append(i)
print("Vale after removing duplicates",res)