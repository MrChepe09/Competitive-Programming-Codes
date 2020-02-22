fin = open('a_example.txt', 'r')  #input file
fout = open('test.txt', 'w')  #output file
done = []
al_lib = []
book_done = []
mybook = []
al_lib_books = []
var_book = []
total_lib = 0
books, lib, days = (fin.readline().strip('\n').split())
books = int(books)
lib = int(lib)
days = int(days)
score_book = list(map(int, fin.readline().strip('\n').split()))
for i in range(0, books):
  mybook.append(i)
for i in range(lib):
  liba = list(map(int, fin.readline().strip('\n').split()))
  al_lib.append(liba)
  lib_books = list(map(int, fin.readline().strip('\n').split()))
  al_lib_books.append(lib_books)
trry = 0
best = 0
while(len(mybook)>0 or best != lib-1):
  print(trry)
  best = 100000000
  ans = []
  maxi = score_book.index(max(score_book))
  for j in range(len(al_lib)):
    if(maxi in al_lib_books[j]):
      if(al_lib[j][1]<best and al_lib[j][1]<days and (j not in done)):
        best = j
  done.append(best)
  print(al_lib)
  print(best)
  days -= al_lib[best][1]
  total_lib+=1
  bok_str = str(best) + " " +str(len(al_lib_books[best]))
  var_book.append(bok_str)
  var_book.append(al_lib_books[best])


  for k in range(0, al_lib[best][2]*days):
    if(k==al_lib[best][0]):
      break
    elif(al_lib_books[best][k] not in book_done):
      #print(al_lib_books[best][k])
      #print(score_book[al_lib_books[best][k]])
      mybook.remove(al_lib_books[best][k])
      book_done.append(k)
  trry+=1
    


fout.write(str(total_lib)+'\n')
for i in range(0, len(var_book)):
  var = " ".join([str(num) for num in var_book[i]])
  fout.write(str(var)+'\n')
fin.close()
fout.close()
  
#al_lib = " ".join([str(num) for num in al_lib])
