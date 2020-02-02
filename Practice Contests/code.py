a = ['a', 'A', 'b', 'd', 'D', 'g', 'e', 'o', 'O', 'p', 'P', 'q', 'Q', 'R', '4', '6', '9', '0']
b = ['B', '8']
t = int(input())
for i in range(t):
  total = 0
  n = int(input())
  words = input().split()
  for i in range(len(words)):
    word = words[i]
    for j in range(len(word)):
      if word[j] in a:
        total = total + 1
      elif word[j] in b:
        total = total + 2
  print(total)
