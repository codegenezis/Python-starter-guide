import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.deepcopy(old_list)

old_list.append([4, 4, 4])
old_list[1][1] = 'AA'  

print("Old list:", old_list)
print("New list:", new_list)

print("Old list:", id(old_list))
print("New list:", id(new_list))

# Shallow copy result:
# Old list: [[1, 2, 3], [4, 'AA', 6], [7, 8, 9], [4, 4, 4]]
# New list: [[1, 2, 3], [4, 'AA', 6], [7, 8, 9]]
# Old list: 140296995409088
# New list: 140296995445824

# Deep copy:
# Old list: [[1, 2, 3], [4, 'AA', 6], [7, 8, 9], [4, 4, 4]]
# New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Old list: 139852010454208
# New list: 139852010490944