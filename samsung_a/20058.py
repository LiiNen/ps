nq = input().split(' ')
n = int(nq[0])
q = int(nq[1])

arr = []
n = 1 << n
for i in range(0, n):
  temp = input().split(' ')
  arr.append([int(t) for t in temp])

temp_magic = input().split(' ')
magic_list = [int(tm) for tm in temp_magic]

def rotate(x, y, L):
  global arr
  for i in range(0, int(L/2)):
    for j in range(0, L):
      temp = arr[x+i][y+j]
      arr[x+i][y+j] = arr[x+(L-1)-i][y+j]
      arr[x+(L-1)-i][y+j] = temp
  for i in range(0, L):
    for j in range(i, L):
      temp = arr[x+i][y+j]
      arr[x+i][y+j] = arr[x+j][y+i]
      arr[x+j][y+i] = temp

def fire_storm():
  global n, arr
  # print('\n\nfirestormbefore')
  # for i in range(0, n):
  #   print(arr[i])

  fire_arr = []
  for i in range(0, n):
    for j in range(0, n):
      if(arr[i][j] == 0):
        continue
      c = 0
      if(i > 0 and arr[i-1][j] != 0):
        c += 1
      if(i < n-1 and arr[i+1][j] != 0):
        c += 1
      if(j > 0 and arr[i][j-1] != 0):
        c += 1
      if(j < n-1 and arr[i][j+1] != 0):
        c += 1
      if(c < 3):
        fire_arr.append([i, j])
  for fire_target in fire_arr:
    arr[fire_target[0]][fire_target[1]] -= 1
  # print('firestormafter')
  # for i in range(0, n):
  #   print(arr[i])

def spell(magic_L):
  global n
  if(magic_L > 1):
    for i in range(0, n, magic_L):
      for j in range(0, n, magic_L):
        rotate(i, j, magic_L)
  fire_storm()

visit_arr = [[False for i in range(0, n)] for j in range(0, n)]
max_size = 0
count = 0
sum = 0
queue = []
def bfs(x, y):
  global arr, n, count, visit_arr, sum, queue
  count += 1
  visit_arr[x][y] = True
  sum += arr[x][y]
  # print(x, y, count)
  if(x-1 >= 0 and arr[x-1][y] != 0):
    queue.append([x-1, y])
  if(y-1 >= 0 and arr[x][y-1] != 0):
    queue.append([x, y-1])
  if(x+1 < n and arr[x+1][y] != 0):
    queue.append([x+1, y])
  if(y+1 < n and arr[x][y+1] != 0):
    queue.append([x, y+1])

for i in range(0, len(magic_list)):
  spell(1 << magic_list[i])

for i in range(0, n):
  for j in range(0, n):
    if(visit_arr[i][j] == False and arr[i][j] != 0):
      count = 0
      queue = [[i, j]]
      while(len(queue) != 0):
        if(visit_arr[queue[0][0]][queue[0][1]] == False):
          bfs(queue[0][0], queue[0][1])
        queue.pop(0)
      if(count > max_size):
        max_size = count

print(sum)
print(max_size)