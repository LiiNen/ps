import copy

nm = input()
n = int(nm.split(' ')[0])
m = int(nm.split(' ')[1])

nn_array = []
over_array = []

for i in range(0, n):
  temp = input().split(' ')
  temp_array = []
  over_temp_array = []
  for j in range(0, n):
    temp_array.append(int(temp[j]))
    if(int(temp[j]) >= 2):
      over_temp_array.append(True)
    else:
      over_temp_array.append(False)
  nn_array.append(temp_array)
  over_array.append(over_temp_array)

ds_array = []

for i in range(0, m):
  temp = input().split(' ')
  temp_array = []
  temp_array.append(int(temp[0]))
  temp_array.append(int(temp[1]))
  ds_array.append(temp_array)
  
cloud_list = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

def x_aesc(x, s):
  global n
  x = x + s
  while x >= n:
    x -= n
  return x

def y_aesc(y, s):
  global n
  y = y + s
  while y >= n:
    y -= n
  return y

def x_desc(x, s):
  global n
  x = x - s
  while x < 0:
    x += n
  return x

def y_desc(y, s):
  global n
  y = y - s
  while y < 0:
    y += n
  return y

def move_axis(x, y, d, s):
  if(d == 1):
    y = y_desc(y, s)
  elif(d == 2):
    x = x_desc(x, s)
    y = y_desc(y, s)
  elif(d == 3):
    x = x_desc(x, s)
  elif(d == 4):
    x = x_desc(x, s)
    y = y_aesc(y, s)
  elif(d == 5):
    y = y_aesc(y, s)
  elif(d == 6):
    x = x_aesc(x, s)
    y = y_aesc(y, s)
  elif(d == 7):
    x = x_aesc(x, s)
  elif(d == 8):
    x = x_aesc(x, s)
    y = y_desc(y, s)
  return [x, y]
    
def move(ds):
  global nn_array, cloud_list
  temp_list = []
  for cloud in cloud_list:
    temp = (move_axis(cloud[0], cloud[1], ds[0], ds[1]))
    nn_array[temp[0]][temp[1]] += 1
    temp_list.append(temp)
  for temp in temp_list:
    copybug(temp[0], temp[1])
  cloud_create()

def copybug(x, y):
  global nn_array, over_array
  if(x+1 < n and y+1 < n):
    if(nn_array[x+1][y+1] > 0):
      nn_array[x][y] += 1
  if(x+1 < n and y-1 >= 0):
    if(nn_array[x+1][y-1] > 0):
      nn_array[x][y] += 1
  if(x-1 >= 0 and y-1 >= 0):
    if(nn_array[x-1][y-1] > 0):
      nn_array[x][y] += 1
  if(x-1 >= 0 and y+1 < n):
    if(nn_array[x-1][y+1] > 0):
      nn_array[x][y] += 1
  over_array[x][y] = False

def cloud_create():
  global nn_array, over_array, cloud_list
  temp_array = []
  for i in range(0, n):
    for j in range(0, n):
      if(over_array[i][j]):
        nn_array[i][j] -= 2
        temp_array.append([i, j])
      if(nn_array[i][j] >= 2):
        over_array[i][j] = True
      else:
        over_array[i][j] = False
  cloud_list = copy.deepcopy(temp_array)

for i in range(0, m):
  move(ds_array[i])
  # print(i, 'cycle')
  # for j in range(0, n):
  #   print(nn_array[j])

sum = 0
for i in range(0, n):
  # print(nn_array[i])
  for j in range(0, n):
    sum += nn_array[i][j]

print(sum)