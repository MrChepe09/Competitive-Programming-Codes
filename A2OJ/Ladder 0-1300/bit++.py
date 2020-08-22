def bit(n, seq):
    if(seq[1]=='+'):
        n+=1
    elif(seq[1]=='-'):
        n-=1
    return n

s = int(input())
no = 0
for i in range(s):
    seq = input()
    no = bit(no, seq)
print(no)