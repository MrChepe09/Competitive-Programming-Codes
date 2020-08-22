def boygirl(s):
    if(len(set(s))%2==1):
        return "IGNORE HIM!"
    return 'CHAT WITH HER!'

s = input()
print(boygirl(s))