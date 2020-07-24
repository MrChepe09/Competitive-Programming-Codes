def segment_tree_build(si, ss, se):
    global seg, a
    if(ss==se):
        seg[si] = a[ss]
        return

    mid = (ss+se)//2
    segment_tree_build(2*si, ss, mid)
    segment_tree_build(2*si+1, mid+1, se)
    
    seg[si] = min(seg[2*si], seg[2*si+1])
    
def segment_tree_query(si, ss, se, qs, qe):
    global seg, a
    if(ss>qe or se<qs):
        return float('inf')
    if(ss>=qs and se<=qe):
        return seg[si]

    mid = (ss+se)//2
    
    return min(segment_tree_query(2*si, ss, mid, qs, qe), segment_tree_query(2*si+1, mid+1, se, qs, qe))

def segment_tree_update(si, ss, se, qi):\
    global seg, a
    if(ss==se):
        seg[si] = a[ss]
        return

    mid = (ss+se)//2
    if(sq <= mid):
        segment_tree_update(2*si, ss, mid, qi)
    else:
        segment_tree_update(2*si+1, mid+1, se, qi)
    seg[si] = min(seg[2*si], seg[2*si+1])

n = int(input())
a = list(map(int, input().split()))
a = [0]+a
seg  = [0]*400004
segment_tree_build(1, 1, n)
#print(seg[:10])
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(segment_tree_query(1, 1, n, l+1, r+1))
