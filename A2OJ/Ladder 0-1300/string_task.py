def stringtask(s):
    res = []
    vowels = ['A', 'a', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    for i in s:
        if(i not in vowels):
            res.append('.')
            res.append(i.lower())
    ans = ''.join(res)
    return ans

s = input()
print(stringtask(s))