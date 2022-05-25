a = [12,1,10,5,9,8,7,22]

# while a:
  # print(a)

min = a[0]
for i in a:
  if( min > i):
    print("if cond",min,i)
    min = i
  else:
    print(min,i)
    
  
    