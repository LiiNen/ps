import math

rck = input().split(' ')
r = int(rck[0])
c = int(rck[1])
k = int(rck[2])

arr = []
right_arr = []
left_arr = []
up_arr = []
down_arr = []
target_arr = []
for i in range(0, r):
  cline = input().split(' ')
  temp = []
  for j in range(0, c):
    _id = int(cline[j])
    if(_id == 1):
      right_arr.append([i, j])
    elif(_id == 2):
      left_arr.append([i, j])
    elif(_id == 3):
      up_arr.append([i, j])
    elif(_id == 4):
      down_arr.append([i, j])
    elif(_id == 5):
      target_arr.append([i, j])
    temp.append(0)
  arr.append(temp)

w = int(input())

# wall cell 0 for east, 1 for south, 2 for west, 3 for north
warr = []
for i in range(0, r):
  wall_line = []
  for j in range(0, c):
    wall_cell = []
    wall_line.append(wall_cell)
  warr.append(wall_line)

for i in range(0, w):
  xyt = input().split(' ')
  x = int(xyt[0])-1
  y = int(xyt[1])-1
  if(int(xyt[2]) == 0):
    warr[x][y].append(3)
    warr[x-1][y].append(1)
  else:
    warr[x][y].append(0)
    warr[x][y+1].append(2)

chocolate = 0
def check_temp():
  global target_arr, arr, k, chocolate
  chocolate += 1
  complete = True
  if(chocolate > 100):
    print(101)
  else:
    for target in target_arr:
      if arr[target[0]][target[1]] < k:
        complete = False
        break
    if(complete):
      print(chocolate)
  return complete

wind_status = [[0 for j in range(0, c)] for i in range(0, r)]
def right_wind():
  global right_arr, arr, wind_status
  for right in right_arr:
    wind_status = [[0 for j in range(0, c)] for i in range(0, r)]
    wind_status[right[0]][right[1]+1] = 5
    right_wind_blow(5, right[0], right[1]+1)
    for i in range(0, r):
      for j in range(0, c):
        if(wind_status[i][j] > 0):
          arr[i][j] += wind_status[i][j]

def right_wind_blow(value, x, y):
  global wind_status
  if(value==1):
    return
  if(y == c-1):
    return
  if(0 not in warr[x][y]):
    wind_status[x][y+1] = value-1
    right_wind_blow(value-1, x, y+1)
  else:
    wind_status[x][y+1] = -1
  if(x-1 >= 0):
    if(2 not in warr[x-1][y+1] and 3 not in warr[x-1][y+1]):
      if(wind_status[x-1][y+1] != -1):
        wind_status[x-1][y+1] = value-1
        right_wind_blow(value-1, x-1, y+1)
  if(x+1 < r):
    if(2 not in warr[x+1][y+1] and 1 not in warr[x+1][y+1]):
      if(wind_status[x+1][y+1] != -1):
        wind_status[x+1][y+1] = value-1
        right_wind_blow(value-1, x+1, y+1)

  

def left_wind():
  global left_arr, arr, wind_status
  for left in left_arr:
    wind_status = [[0 for j in range(0, c)] for i in range(0, r)]
    wind_status[left[0][left[1]-1]] = 5
    left_wind_blow(5, left[0], left[1]-1)
    for i in range(0, r):
      for j in range(0, c):
        if(wind_status[i][j] > 0):
          arr[i][j] += wind_status[i][j]

def left_wind_blow(value, x, y):
  global wind_status
  if(value==1):
    return
  if(y == 0):
    return
  if(2 not in warr[x][y]):
    wind_status[x][y-1] = value-1
    left_wind_blow(value-1, x, y-1)
  else:
    wind_status[x][y-1] = -1
  if(x-1 >= 0):
    if(0 not in warr[x-1][y-1] and 3 not in warr[x-1][y-1]):
      if(wind_status[x-1][y-1] != -1):
        wind_status[x-1][y-1] = value-1
        left_wind_blow(value-1, x-1, y-1)
  if(x+1 < r):
    if(0 not in warr[x+1][y-1] and 1 not in warr[x+1][y-1]):
      if(wind_status[x+1][y-1] != -1):
        wind_status[x+1][y-1] = value-1
        left_wind_blow(value-1, x+1, y-1)
  

def up_wind():
  global up_arr, arr, wind_status
  for up in up_arr:
    wind_status = [[0 for j in range(0, c)] for i in range(0, r)]
    wind_status[up[0]-1][up[1]] = 5
    up_wind_blow(5, up[0]-1, up[1])
    for i in range(0, r):
      for j in range(0, c):
        if(wind_status[i][j] > 0):
          arr[i][j] += wind_status[i][j]

def up_wind_blow(value, x, y):
  global wind_status
  if(value==1):
    return
  if(x == 0):
    return
  if(3 not in warr[x][y]):
    wind_status[x-1][y] = value-1
    up_wind_blow(value-1, x-1, y)
  else:
    wind_status[x-1][y] = -1
  if(y-1 >= 0):
    if(1 not in warr[x-1][y-1] and 2 not in warr[x-1][y-1]):
      if(wind_status[x-1][y-1] != -1):
        wind_status[x-1][y-1] = value-1
        up_wind_blow(value-1, x-1, y-1)
  if(y+1 < c):
    if(1 not in warr[x-1][y+1] and 0 not in warr[x-1][y+1]):
      if(wind_status[x-1][y+1] != -1):
        wind_status[x-1][y+1] = value-1
        up_wind_blow(value-1, x-1, y+1)

def down_wind():
  global down_arr, arr, wind_status
  for down in down_arr:
    wind_status = [[0 for j in range(0, c)] for i in range(0, r)]
    wind_status[down[0]+1][down[1]] = 5
    down_wind_blow(5, down[0]+1, down[1])
    for i in range(0, r):
      for j in range(0, c):
        if(wind_status[i][j] > 0):
          arr[i][j] += wind_status[i][j]

def down_wind_blow(value, x, y):
  global wind_status
  if(value==1):
    return
  if(x == r-1):
    return
  if(1 not in warr[x][y]):
    wind_status[x+1][y] = value-1
    down_wind_blow(value-1, x+1, y)
  else:
    wind_status[x+1][y] = -1
  if(y-1 >= 0):
    if(2 not in warr[x+1][y-1] and 3 not in warr[x+1][y-1]):
      if(wind_status[x+1][y-1] != -1):
        wind_status[x+1][y-1] = value-1
        down_wind_blow(value-1, x+1, y-1)
  if(y+1 < c):
    if(0 not in warr[x+1][y+1] and 3 not in warr[x+1][y+1]):
      if(wind_status[x+1][y+1] != -1):
        wind_status[x+1][y+1] = value-1
        down_wind_blow(value-1, x+1, y+1)

def wind_blow():
  right_wind()
  left_wind()
  up_wind()
  down_wind()

def average_temp():
  global arr
  diff_arr = []
  for i in range(0, r):
    temp_arr = []
    for j in range(0, c):
      temp_var = 0
      if(i > 0 and 3 not in warr[i][j]):
        ld = (arr[i-1][j] - arr[i][j])/4
        if(ld < 0):
          temp_var += math.ceil(ld)
        else:
          temp_var += math.floor(ld)
      if(i < r-1 and 1 not in warr[i][j]):
        rd = (arr[i+1][j] - arr[i][j])/4
        if(rd < 0):
          temp_var += math.ceil(rd)
        else:
          temp_var += math.floor(rd)
      if(j > 0 and 2 not in warr[i][j]):
        ud = (arr[i][j-1] - arr[i][j])/4
        if(ud < 0):
          temp_var += math.ceil(ud)
        else:
          temp_var += math.floor(ud)
      if(j < c-1 and 0 not in warr[i][j]):
        dd = (arr[i][j+1] - arr[i][j])/4
        if(dd < 0):
          temp_var += math.ceil(dd)
        else:
          temp_var += math.floor(dd)
      temp_arr.append(temp_var)
    diff_arr.append(temp_arr)
  for i in range(0, r):
    for j in range(0, c):
      arr[i][j] += diff_arr[i][j]

def down_temp():
  global arr
  for i in range(1, c-1):
    if(arr[0][i] != 0):
      arr[0][i] -= 1
    if(arr[r-1][i] != 0):
      arr[r-1][i] -= 1
  for i in range(1, r-1):
    if(arr[i][0] != 0):
      arr[i][0] -= 1
    if(arr[i][c-1] != 0):
      arr[i][c-1] -= 1
  if(arr[0][0] != 0):
    arr[0][0] -= 1
  if(arr[0][c-1] != 0):
    arr[0][c-1] -= 1
  if(arr[r-1][0] != 0):
    arr[r-1][0] -= 1
  if(arr[r-1][c-1] != 0):
    arr[r-1][c-1] -= 1

while(True):
  wind_blow()
  # print('after wind')
  # for i in range(0, r):
  #   print(arr[i])
  # input()
  average_temp()
  # print('after av')
  # for i in range(0, r):
  #   print(arr[i])
  # input()
  down_temp()
  # print('after down')
  # for i in range(0, r):
  #   print(arr[i])
  # input()
  isComplete = check_temp()
  if(isComplete):
    break