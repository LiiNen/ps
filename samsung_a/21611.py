import copy

nm = input()
n = int(nm.split(' ')[0])
m = int(nm.split(' ')[1])

nn_array = []
ds_array = []

for i in range(0, n):
  temp_array = []
  temp = input().split(' ')
  for j in range(0, n):
    temp_array.append(int(temp[j]))
  nn_array.append(temp_array)

for i in range(0, m):
  ds = input().split(' ')
  ds_array.append([int(ds[0]), int(ds[1])])

shark = int(n/2)

dxdy = [[0, -1], [1, 0], [0, 1], [-1, 0]]
d_index = 0
prev_x = shark
prev_y = shark
x = shark
y = shark
inc = 1

prev_list = []
next_list = []
for i in range(0, n):
  prev_list.append([None for j in range(0, n)])
  next_list.append([None for j in range(0, n)])

while(1):
  for z in range(0, 2):
    for i in range(0, inc):
      x = prev_x + dxdy[d_index][0]
      y = prev_y + dxdy[d_index][1]
      if(x == 0 and y == -1):
        break
      prev_list[x][y] = [prev_x, prev_y]
      next_list[prev_x][prev_y] = [x, y]
      prev_x = x
      prev_y = y
    if(x == 0 and y == -1):
      break
    d_index += 1
    d_index %= 4
  if(x == 0 and y == -1):
    break
  inc += 1

def blizzard(d, s):
  global shark, nn_array
  dx = 0
  dy = 0
  if(d == 1):
    dx = -1
  elif(d == 2):
    dx = 1
  elif(d == 3):
    dy = -1
  elif(d == 4):
    dy = 1

  for i in range(1, s+1):
    nn_array[shark+dx*i][shark+dy*i] = 0

  zip()

explosion_list = [0, 0, 0, 0]
value_list = []

def zip():
  global nn_array, value_list, next_list, shark
  value_list = []
  x = shark
  y = shark
  while(next_list[x][y] != None):
    t = next_list[x][y][0]
    y = next_list[x][y][1]
    x = t
    if(nn_array[x][y] != 0):
      value_list.append(nn_array[x][y])
  # print('zip')
  # print(value_list)
  explode()

def explode():
  global value_list, explosion_list
  while(True):
    is_explode = False
    temp_list = []
    temp = 0
    count = 0
    for value in value_list:
      if(value == 0):
        continue
      if(value != temp):
        if(count > 3):
          is_explode = True
          explosion_list[temp] += count
          while(count != 0):
            temp_list.pop()
            count -= 1
        temp = value
        count = 1
      else:
        count += 1
      temp_list.append(value)
    if(count > 3):
      is_explode = True
      explosion_list[temp] += count
      while(count != 0):
        temp_list.pop()
        count -= 1
    value_list = copy.deepcopy(temp_list)
    if(not is_explode):
      break
  #   print(value_list)
  # print('explode')
  # print(value_list)
  regenerate()

def regenerate():
  global value_list
  temp_list = []
  count = 0
  temp = 0
  for value in value_list:
    if(temp != value and temp != 0):
      temp_list.append(count)
      temp_list.append(temp)
      temp = value
      count = 1
    else:
      temp = value
      count += 1
  temp_list.append(count)
  temp_list.append(temp)
  value_list = []
  value_list = copy.deepcopy(temp_list)

  reallocate()

def reallocate():
  global value_list, nn_array, next_list, n
  nn_array = [[0 for i in range(0, n)] for j in range(0, n)]
  # print('reallocate')
  # print(value_list)
  x = shark
  y = shark
  for i in range(len(value_list)):
    if(i == n * n - 1):
      break
    next = next_list[x][y]
    nn_array[next[0]][next[1]] = value_list[i]
    x = next[0]
    y = next[1]

for ds in ds_array:
  blizzard(ds[0], ds[1])
  # print('blizzard')
  # for i in range(0, n):
  #   print(nn_array[i])

print(explosion_list[1] * 1 + explosion_list[2] * 2 + explosion_list[3] * 3)