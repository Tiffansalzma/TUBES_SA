import itertools 
import time
start_time = time.time()

n = 5
k = ["m", "k", "h", "u", "b"]
list_k = []
for i in range(n):
  for j in k:
    list_k.append(j)

list_k.sort()

permutations = list(itertools.permutations(list_k, r = n))
solution = []
for i in range(len(permutations)):
    count = 0
    for j in range(len(permutations[i])):
        temp = permutations[i][j]
        try:
            if (temp == permutations[i][j+1] and temp == permutations[i][j+2]):
                count += 1
        except:
            break
    if count == 0 :
        if permutations[i] not in solution :
            solution.append(permutations[i])
            print(permutations[i])
print("Terdapat", len(solution), "kombinasi")
print("Waktu untuk menyelesaikan program ini adalah", time.time() - start_time, "detik")
