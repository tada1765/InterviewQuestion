""" Hi, here's your problem today. 
This problem was recently asked by Twitter:

Given 3 sorted lists, find the intersection 
of those 3 lists.
"""
def _findSameValInList(lista,listb):
    temp = []
    for i in range(0,len(lista)):
        val = lista[i]
        for j in range(0,len(listb)):
            val2 = listb[j]
            if (val == val2):
                temp.append(val)
    return temp

def intersection(list1, list2, list3):
    # result = [2, 4], minimising number of the data 
    result = _findSameValInList(list1, list2)
    result = _findSameValInList(result, list3)

    return result

print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]


# My other attempt:
def _intersection(*args):
    
    # for i in args:
    #     print(i)
    #     Output:
    #     # [1, 2, 3, 4]
    #     # [2, 4, 6, 8]
    #     # [3, 4, 5]

    result = args[0] # [1, 2, 3, 4]
    for i in range(1,len(args)):
        result = _findSameValInList(result, args[i])

    return result

list1 = [1, 2, 3, 4]
list2 = [2, 4, 6, 8]
list3 = [2, 4, 5]
list4 = [2, 5, 6, 7, 8]
print(_intersection(list1,list2,list3,list4)) # [2]
