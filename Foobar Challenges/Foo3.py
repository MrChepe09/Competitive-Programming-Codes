def getlist(lis):
  dicti = dict.fromkeys(lis, 0)
  for el in lis:
    dicti[el] = list(map(int, el.split(".")))
  dicti = sorted(dicti.items(), key=lambda x: x[1])
  return [i[0] for i in dicti]

a = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
print(getlist(a))
