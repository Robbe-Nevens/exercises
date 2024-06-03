def findMaximum(list):
    if len(list) == 1:
        return list
    if list[0] > list[-1]:
        return findMaximum(list[:-1])
    else:
        return findMaximum(list[1:])
    
print(findMaximum([]))