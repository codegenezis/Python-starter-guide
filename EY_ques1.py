          
def anagram(str1,str2):
    temp = []
    for i in str1:
        if i not in temp:
            temp.append(i)    
    count = 0
    for j in temp:
        # print(j)
        if str1.count(j) == str2.count(j):
            count = count + 1;
    # print(count)
    
    if count == len(temp):
        return "true"
    else:
        return "false"

print(anagram("abaad", "baaac"))
    
        
        
    
    
    
