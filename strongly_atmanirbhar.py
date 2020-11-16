def atmanirbhar(n, m):
    global item, quan, price, litem, lquan, lprice
    for i in range(m):
        if litem[i] in item:
            ind = item.index(litem[i])
            if lquan[i] > quan[ind]:
                lquan[i] = quan[ind]
                quan[ind] = 0
            else:
                quan[ind] -= lquan[i]
    costimp = 0
    costind = 0
    for i in range(m):
        if litem[i] in item:
            costind += (lquan[i]*lprice[i])
    for j in range(n):
        costimp += (quan[j]*price[j])
    
    return costimp + costind


n = int(input())
item = []
quan = []
price = []
for i in range(n):
    i, q, p = input().split()
    item.append(i)
    quan.append(int(q))
    price.append(int(p))
m = int(input())
litem = []
lquan = []
lprice = []
for i in range(m):
    i, q, p = input().split()
    litem.append(i)
    lquan.append(int(q))
    lprice.append(int(p))
print(atmanirbhar(n, m))