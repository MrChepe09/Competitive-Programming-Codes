def getParent(lev, key):
    maxi = (2**lev)-1
    start = 0
    flag = True
    size = maxi
    ans = -1
    while flag:
        if size == 0:
            flag = False
        size = size//2
        left_child = start + size
        right_child = left_child + size
        my_node = right_child + 1
        if (left_child == key) or (right_child == key):
            ans = my_node
            flag = False
        if (key > left_child):
            start = left_child
    return ans
    
def solution(h, q):
    return [ getParent(h, x) for x in q ]
