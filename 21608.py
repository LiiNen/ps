import copy

n = int(input())
s_array = [None for i in range(0, n*n+1)]
id_list = []

# u d l r
nn_array = [[[0, 0, 0, 0, 0] for i in range(0, n)] for i in range(0, n)]

for i in range(0, n*n):
  line = input().split(' ')
  id = int(line[0])
  like_id_list = [int(line[j]) for j in range(1, 5)]
  s_array[id] = like_id_list
  id_list.append(id)

for i in range(0, n):
  for j in range(0, n):
    ecount = -4
    if(i == 0):
      nn_array[i][j][1] = -1
      ecount += 1
    if(j == 0):
      nn_array[i][j][3] = -1
      ecount += 1
    if(i == n-1):
      nn_array[i][j][2] = -1
      ecount += 1
    if(j == n-1):
      nn_array[i][j][4] = -1
      ecount += 1
    nn_array[i][j][0] = ecount

# print('init')
# for j in range(0, n):
#   print([nn_array[j][k][0] for k in range(0, n)])

for i in range(0, n*n):
  id = id_list[i]
  rem_j = 0
  rem_k = 0
  rem_e = 1
  rem_c = -1
  s = s_array[id]
  for j in range(0, n):
    for k in range(0, n):
      tc = 0
      te = 0
      if(nn_array[j][k][0] > 0):
        continue
      for x in range(1, 5):
        if(nn_array[j][k][x] in s):
          tc += 1
      te = nn_array[j][k][0]
      if(tc >= rem_c):
        if(tc == rem_c):
          if(te < rem_e):
            rem_j = j
            rem_k = k
            rem_e = te
            rem_c = tc
        else:
          rem_j = j
          rem_k = k
          rem_e = te
          rem_c = tc
      if(rem_c == 4):
        break
    if(rem_c == 4):
      break
  nn_array[rem_j][rem_k][0] = id
  if(rem_j-1 >= 0):
    nn_array[rem_j-1][rem_k][2] = id
    if(nn_array[rem_j-1][rem_k][0] < 0):
      nn_array[rem_j-1][rem_k][0] += 1
  if(rem_j+1 < n):
    nn_array[rem_j+1][rem_k][1] = id
    if(nn_array[rem_j+1][rem_k][0] < 0):
      nn_array[rem_j+1][rem_k][0] += 1
  if(rem_k-1 >= 0):
    nn_array[rem_j][rem_k-1][4] = id
    if(nn_array[rem_j][rem_k-1][0] < 0):
      nn_array[rem_j][rem_k-1][0] += 1
  if(rem_k+1 < n):
    nn_array[rem_j][rem_k+1][3] = id
    if(nn_array[rem_j][rem_k+1][0] < 0):
      nn_array[rem_j][rem_k+1][0] += 1
  
  # print('after ', id)
  # for j in range(0, n):
  #   print([nn_array[j][k][0] for k in range(0, n)])

point = 0

for i in range(0, n):
  for j in range(0, n):
    s = s_array[nn_array[i][j][0]]
    count = 0
    for k in range(1, 5):
      if nn_array[i][j][k] in s:
        if(count == 0):
          count = 1
        else:
          count *= 10
    point += count

print(point)