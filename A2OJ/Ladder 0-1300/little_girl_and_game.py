def game(s):
    dicti = {}
    for i in s:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
    odd = 0
    for i in dicti:
        if dicti[i]%2==1:
            odd+=1

    if odd == 0:
        return 'First'
    elif odd== 1:
        return "First"
    else:
        if odd%2==1:
            return 'First'
        else:
            return 'Second'
        

s = input()
print(game(s))