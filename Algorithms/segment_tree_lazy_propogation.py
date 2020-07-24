def segment_tree_build(si, ss, se):
    global seg, a
    if(ss==se):
        seg[si] = a[ss]
        return

    mid = (ss+se)//2
    segment_tree_build(2*si, ss, mid)
    segment_tree_build(2*si+1, mid+1, se)
    
    seg[si] = seg[2*si] + seg[2*si+1]
    
def segment_tree_query(si, ss, se, qs, qe):
    global seg, lazy
    if(lazy[si]!=0):
        dx = lazy[si]
        lazy[si]=0
        seg[si] += dx * (se-ss+1)

        if(ss != se):
            lazy[2*si]+=dx
            lazy[2*si+1] += dx
        
    if(ss>qe or se<qs):
        return 0
    if(ss>=qs and se<=qe):
        return seg[si]

    mid = (ss+se)//2
    
    return segment_tree_query(2*si, ss, mid, qs, qe) + segment_tree_query(2*si+1, mid+1, se, qs, qe)

def segment_tree_update(si, ss, se, qs, qe, val):
    global seg, lazy
    if(lazy[si]!=0):
        dx = laxy[si]
        lazy[si] = 0
        seg[si] += dx*(se-ss+1)

        if(ss!=se):
            lazy[2*si] += dx
            lazy[2*si+1] += dx
    
    if(ss>qe or se<qs):
        return

    if(ss >= qs and se <= qe):
        dx = (se-ss+1)*val
        seg[si] += dx
        if(ss!=se):
            lazy[2*si] += val
            lazy[2*si+1] += val
        return
            
    mid = (ss+se)//2
    #print(si, ss, se)
    segment_tree_update(2*si, ss, mid, qs, qe, val)
    segment_tree_update(2*si+1, mid+1, se, qs, qe, val)
    seg[si] = seg[2*si] + seg[2*si+1]

n, q = map(int, input().split())
a = [0]*(n+1)
seg  = [0]*400004
lazy = [0]*400004
segment_tree_build(1, 1, n)
#print(seg[:10])
for i in range(q):
    qlist = list(map(int, input().split()))
    if(len(qlist)==3):
        print(segment_tree_query(1, 1, n, qlist[1], qlist[2]))
    else:
        print(segment_tree_update(1, 1, n, qlist[1], qlist[2], qlist[3]))

