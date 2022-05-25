a = [["1", "2", ""],["3","4"]]
# output: [[1, 2, 0],[3,4]]
temp= []

# for i in a:
#     temp1=[]
#     for j in i:
#         if (j != ""):
#             temp1.append(int(j))
#         else:
#             temp1.append(0)
#     temp.append(temp1)
# print(temp)


result = [[int(j) if bool(j) == True else 0 for j in i] for i in a]
print(result)