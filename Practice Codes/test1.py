def solve(test):
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    dict_total = {}
    dict_a = {}
    dict_b = {}
    for a in arr_a:
        if a in dict_total:
            dict_total[a] += 1
        else:
            dict_total[a] = 1
        if a in dict_a:
            dict_a[a] += 1
        else:
            dict_a[a] = 1
    for b in arr_b:
        if b in dict_total:
            dict_total[b] += 1
        else:
            dict_total[b] = 1
        if b in dict_b:
            dict_b[b] += 1
        else:
            dict_b[b] = 1
    # print('all:', d_total)
    # print('a:', d_a)
    # print('b:', d_b)
    isAnsExist = True
    for key in dict_total:
        if (dict_total[key]) % 2 == 1:
            isAnsExist = False
            break
    if not isAnsExist:
        print('-1')
    else:
        # ans exist
        #print(dict_total)
        change = {}
        for num in dict_total:
            a_count = 0
            b_count = 0
            if num in dict_a:
                a_count = dict_a[num]
            if num in dict_b:
                b_count = dict_b[num]
            if(a_count != b_count):
                change[num] = int(abs(a_count - b_count)/2)
        if len(change) == 0:
            print(0)
        else:
            #print(change)
            # calculate ans here
            arr = []
            for tem in change:
                for i in range(change[tem]):
                    arr.append(tem)
            arr.sort()
            ans = 0
            #print('arr', arr)
            min_ele = min(dict_total)
            #print(arr)
            #print(min_ele)
            for i in range(int(len(arr)/2)):
                if arr[i] > 2 * min_ele:
                    ans += 2*min_ele
                else:
                    ans += arr[i]
            print(ans)

test_case = int(input())
for test in range(test_case):
    solve(test + 1)
