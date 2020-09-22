def rozdil(a):
    mini = min(a)
    if(a.count(mini)>1):
        return "Still Rozdil"
    else:
        return a.index(mini)+1

n = int(input())
a = list(map(int, input().split()))
print(rozdil(a))