# list1 = [2,4,5, 6,7,9,10, 12, 11,16]
list1 = [8,4,5,2, 6,7,9,10, 12, 11,16,3]
list1.sort()
print(list1)

temp = 0
temp1 = []

for i in range(len(list1)):
    if i==0:
        temp= list1[i]
        print(temp, list1[i]%temp )
        temp1.append(temp)
    else:
        # print(list1[i]/temp)
        if list1[i]%temp == 0 :
            print(list1[i])
        else:
            print("Number not divisible", list1[i])
            temp1.append(list1[i])

print(temp1)