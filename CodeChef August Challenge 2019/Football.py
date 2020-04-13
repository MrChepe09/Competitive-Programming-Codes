test_cases = int(input())
for i in range(test_cases):
  score = []
  total_players = int(input())
  goals = [int(i) for i in input().split()]
  fouls = [int(i) for i in input().split()]
  for j in range(len(goals)):
    s = (goals[j] * 20) - (fouls[j] * 10)
    score.append(s)
  print(max(0, max(score)))
  
