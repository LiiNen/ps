import copy

def move(x, y, dx, dy, arr, target):
  if(arr[x+dx][y+dy]=='O'):
    return x+dx, y+dy, arr
  if(arr[x+dx][y+dy] == '.'):
    return move(x+dx, y+dy, dx, dy, arr, target)
  else:
    arr[x][y] = target
    return x, y, arr

def rec_func(rx, ry, bx, by, length, arr, prev):
  global min_dist
  
  if(length < 11):
    # print('call')
    # print(arr)
    t_arr = copy.deepcopy(arr)
    t_rx = copy.deepcopy(rx)
    t_ry = copy.deepcopy(ry)
    t_bx = copy.deepcopy(bx)
    t_by = copy.deepcopy(by)
    if(prev != 'd' and prev != 'u'):
      t_arr[t_rx][t_ry] = '.'
      t_rx, t_ry, t_arr = move(t_rx, t_ry, -1, 0, t_arr, 'R')
      t_arr[t_bx][t_by] = '.'
      t_bx, t_by, t_arr = move(t_bx, t_by, -1, 0, t_arr, 'B')
      if(t_rx==ox and t_ry==oy and min_dist > length):
        if(not (t_bx==ox and t_by==oy)):
          min_dist = length
      t_arr[t_rx][t_ry] = '.'
      t_rx, t_ry, t_arr = move(t_rx, t_ry, -1, 0, t_arr, 'R')
      # print('up', t_rx, t_ry, prev)
      if(not (t_bx==ox and t_by==oy)):
        rec_func(t_rx, t_ry, t_bx, t_by, length+1, t_arr, 'u')
    
    # print(arr)
    t_arr = copy.deepcopy(arr)
    t_rx = copy.deepcopy(rx)
    t_ry = copy.deepcopy(ry)
    t_bx = copy.deepcopy(bx)
    t_by = copy.deepcopy(by)
    if(prev != 'u' and prev != 'd'):
      t_arr[t_rx][t_ry] = '.'
      t_rx, t_ry, t_arr = move(t_rx, t_ry, 1, 0, t_arr, 'R')
      t_arr[t_bx][t_by] = '.'
      t_bx, t_by, t_arr = move(t_bx, t_by, 1, 0, t_arr, 'B')
      if(t_rx==ox and t_ry==oy and min_dist > length):
        if(not (t_bx==ox and t_by==oy)):
          min_dist = length
      t_arr[t_rx][t_ry] = '.'
      t_rx, t_ry, t_arr = move(t_rx, t_ry, 1, 0, t_arr, 'R')
      # print('down', t_rx, t_ry, prev)
      if(not (t_bx==ox and t_by==oy)):
        rec_func(t_rx, t_ry, t_bx, t_by, length+1, t_arr, 'd')

    # print(arr)
    t_arr = copy.deepcopy(arr)
    t_rx = copy.deepcopy(rx)
    t_ry = copy.deepcopy(ry)
    t_bx = copy.deepcopy(bx)
    t_by = copy.deepcopy(by)
    if(prev != 'r' and prev != 'l'):
      t_arr[t_rx][t_ry] = '.'
      t_rx, t_ry, t_arr = move(t_rx, t_ry, 0, -1, t_arr, 'R')
      t_arr[t_bx][t_by] = '.'
      t_bx, t_by, t_arr = move(t_bx, t_by, 0, -1, t_arr, 'B')
      if(t_rx==ox and t_ry==oy and min_dist > length):
        if(not (t_bx==ox and t_by==oy)):
          min_dist = length
      t_arr[t_rx][t_ry] = '.'
      t_rx, t_ry, t_arr = move(t_rx, t_ry, 0, -1, t_arr, 'R')
      # print('left', t_rx, t_ry, prev)
      if(not (t_bx==ox and t_by==oy)):
        rec_func(t_rx, t_ry, t_bx, t_by, length+1, t_arr, 'l')

    # print(arr)
    t_arr = copy.deepcopy(arr)
    t_rx = copy.deepcopy(rx)
    t_ry = copy.deepcopy(ry)
    t_bx = copy.deepcopy(bx)
    t_by = copy.deepcopy(by)
    # print(t_rx, t_ry, t_arr[t_rx][t_ry+1])
    if(prev != 'l' and prev != 'r'):
      t_arr[t_rx][t_ry] = '.'
      t_rx, t_ry, t_arr = move(t_rx, t_ry, 0, 1, t_arr, 'R')
      t_arr[t_bx][t_by] = '.'
      t_bx, t_by, t_arr = move(t_bx, t_by, 0, 1, t_arr, 'B')
      if(t_rx==ox and t_ry==oy and min_dist > length):
        if(not (t_bx==ox and t_by==oy)):
          min_dist = length
      t_arr[t_rx][t_ry] = '.'
      t_rx, t_ry, t_arr = move(t_rx, t_ry, 0, 1, t_arr, 'R')
      # print('right', t_rx, t_ry, prev)
      if(not (t_bx==ox and t_by==oy)):
        rec_func(t_rx, t_ry, t_bx, t_by, length+1, t_arr, 'r')
  # print('return')

nm = input()
n = int(nm.split(' ')[0])
m = int(nm.split(' ')[1])

rx = 0
ry = 0
bx = 0
by = 0
ox = 0
oy = 0

input_arr = []
for i in range(0, n):
  temp_arr = []
  temp = input()
  for j in range(0, m):
    temp_arr.append(temp[j])
    if(temp[j] == 'R'):
      rx = i
      ry = j
    if(temp[j] == 'B'):
      bx = i
      by = j
    if(temp[j] == 'O'):
      ox = i
      oy = j
  input_arr.append(temp_arr)

min_dist = 11
rec_func(rx, ry, bx, by, 1, input_arr, '')

if(min_dist == 11):
  print(-1)
else:
  print(min_dist)