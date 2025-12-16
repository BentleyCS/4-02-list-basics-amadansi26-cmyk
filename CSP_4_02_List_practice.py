
def bookends(li: list):
    first = li.pop(0)
    last = li.pop(-1)
    return [first, last]

print(bookends([3, 4, 5 ,6]))

def inOrder(li : list):
    if len(li)< 2:
        return True
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            return False
    return True
print(inOrder([1, 1, 1, 3, 4]))




def find(li: list, target : int):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1
print(find([1, 2, 3, 4, 5], 3))


def removeLowest(li):
    lowest = li[0]
    index_of_lowest = 0
    for i in range(len(li)):
        if li[i]<lowest:
            index_of_lowest = i
            lowest = li[i]
    li.pop(index_of_lowest)
    return li
print(removeLowest([5, 6, 5, 8]))


def keepOrder(li: list, value):
    if value<li[0]:
        li.insert(0, value)
        return li
    for i in range(len(li)):
        if i < len(li)-1:
            if li[i] < value < li[i + 1]:
                li.insert(i+1, value)
                return li
        else:
            if li[i] < value:
                li.append( value)
                return li
    return li
print(keepOrder([1, 3, 4, 5, 6, 7], 2))


def merge(l1:list, l2:list):
    new_list = list()
    i = 0
    j = 0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            new_list.append(l1[i])
            i=i+1
        else:
            new_list.append(l2[j])
            j=j+1
    for k in range(i, len(l1)):
        new_list.append(l1[k])
    for l in range(j, len(l2)):
        new_list.append(l2[l])
    return new_list
print(merge([12, 13, 14, 15, 16], [10, 11, 12, 13, 14, 15]))
    
