import copy

nm = input()
n = int(nm.split(' ')[0])
m = int(nm.split(' ')[1])

nn_array = []
for i in range(0, n):
  temp_array = []
  temp = input().split(' ')
  for j in range(0, n):
    temp_array.append(int(temp[j]))
  nn_array.append(temp_array)

exception_list = []
exception_temp = []
block_list = []
block_temp = []

rainbow_count = 0
temp_rainbow = 0

def dfs(x, y, color, count):
  global nn_array, block_temp, temp_rainbow
  if(nn_array[x][y] == color and color != 0):
    block_temp.append([x, y])
    
    count += 1
  elif(nn_array[x][y] == 0):
    block_temp.append([x, y])
    count += 1
    temp_rainbow += 1
  else:
    return count

  if(x-1 >= 0 and [x-1, y] not in block_temp):
    count = dfs(x-1, y, color, count)
  if(x+1 < n and [x+1, y] not in block_temp):
    count = dfs(x+1, y, color, count)
  if(y-1 >= 0 and [x, y-1] not in block_temp):
    count = dfs(x, y-1, color, count)
  if(y+1 < n and [x, y+1] not in block_temp):
    count = dfs(x, y+1, color, count)

  return count

def find_king(xylist):
  x = 100
  y = 100
  for i in range(0, len(xylist)):
    if(nn_array[xylist[i][0]][xylist[i][1]] == 0):
      continue
    if xylist[i][0] < x:
      x = xylist[i][0]
      y = xylist[i][1]
    elif xylist[i][0] == x and xylist[i][1] < y:
      x = xylist[i][0]
      y = xylist[i][1]
  return [x,y]


def find_block():
  global nn_array, block_list, block_temp, temp_rainbow
  # for i in range(0, n):
  #   print(nn_array[i])
  min_count = 0
  block_list = []
  for i in range(0, n):
    for j in range(0, n):
      if([i, j] in block_list or nn_array[i][j] == 0 or nn_array[i][j] == -1 or nn_array[i][j] == -2):
        continue
      block_temp = []
      temp_rainbow = 0
      temp_count = dfs(i, j, nn_array[i][j], 0)
      if(temp_count == temp_rainbow):
        continue
      if(temp_count >= min_count and temp_count >= 2):
        if(len(block_list) == 0):
          min_count = temp_count
          block_list = copy.deepcopy(block_temp)
          block_temp = []
          rainbow_count = temp_rainbow
        elif(temp_count == min_count):
          if(rainbow_count < temp_rainbow):
            min_count = temp_count
            block_list = copy.deepcopy(block_temp)
            block_temp = []
            rainbow_count = temp_rainbow
          elif(rainbow_count == temp_rainbow):
            rem_xy = find_king(block_list)
            tem_xy = find_king(block_temp)
            if(rem_xy[0] < tem_xy[0]):
              min_count = temp_count
              block_list = copy.deepcopy(block_temp)
              block_temp = []
              rainbow_count = temp_rainbow
            elif(rem_xy[0] == tem_xy[0] and rem_xy[1] < tem_xy[1]):
              min_count = temp_count
              block_list = copy.deepcopy(block_temp)
              block_temp = []
              rainbow_count = temp_rainbow
        else:
          min_count = temp_count
          block_list = copy.deepcopy(block_temp)
          block_temp = []
          rainbow_count = temp_rainbow
      # print([i, j], nn_array[i][j], temp_count, block_list)
  return min_count

def deletion():
  global nn_array, block_list, n
  for block in block_list:
    nn_array[block[0]][block[1]] = -2
  block_list = []
  # print('deletion', block_list)
  # for i in range(0, n):
  #   print(nn_array[i])

def rotate():
  global nn_array, n
  rotated_array = [[None for i in range(0, n)] for i in range(0, n)]
  for i in range(0, n):
    for j in range(0, n):
      x = (n-1)-j
      rotated_array[x][i] = nn_array[i][j]
  nn_array = copy.deepcopy(rotated_array)

  # print('rotate')
  # for i in range(0, n):
  #   print(rotated_array[i])


def gravity():
  global nn_array
  for i in range(n-2, -1, -1):
    for j in range(0, n, 1):
      if(nn_array[i][j] >= 0):
        is_push = False
        for k in range(i+1, n):
          if(nn_array[k][j] == -2):
            continue
          else:
            if(i != k-1):
              nn_array[k-1][j] = nn_array[i][j]
              nn_array[i][j] = -2
            is_push = True
            break
        if(not is_push):
          nn_array[n-1][j] = nn_array[i][j]
          nn_array[i][j] = -2
  # print('gravity')
  # for i in range(0, n):
  #   print(nn_array[i])

point = 0
while(True):
  min_count = find_block()
  # print(min_count)
  if(min_count == 0):
    break
  else:
    point += (min_count*min_count)
  # input()
  deletion()
  # input()
  gravity()
  # input()
  rotate()
  # input()
  gravity()
  # input()

# for i in range(0, n):
#   print(nn_array[i])

print(point)