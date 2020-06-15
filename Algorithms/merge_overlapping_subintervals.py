def merge_time(meetings):
  sorted_meet = sorted(meetings)
  merged_meet = [sorted_meet[0]]

  for start, end in sorted_meet[1:]:
    last_start, last_end = merged_meet[-1]
    if(start<=last_end):
      merged_meet[-1] = (last_start, max(last_end, end))
    else:
      merged_meet.append([start, end])
  return merged_meet


test = int(input())
for i in range(test):
  meetings = []
  n = int(input())
  for j in range(n):
    a = list(map(int, input().split()))
    meetings.append(a)
  print(merge_time(meetings))
