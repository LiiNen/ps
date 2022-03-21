import copy

n = int(input())
input_arr = []

max = 0

for i in range(0, n):
  temp = input().split(' ')
  temp_arr = []
  for j in range(0, n):
    temp_arr.append(int(temp[j]))
    if(temp_arr[j] > max):
      max = temp_arr[j]
  input_arr.append(temp_arr)

def left(arr):
  global max
  for i in range(0, n):
    temp_x = 0
    for j in range(0, n+1):
      if(j==n):
        for k in range(temp_x, n):
          arr[i][k] = 0
        break
      else:
        if(arr[i][j] == 0):
          continue
        temp = arr[i][j]
        for k in range(j+1, n+1):
          if(k == n):
            arr[i][temp_x] = temp
            break
          if(arr[i][k] == 0):
            continue
          elif(arr[i][k] != temp):
            arr[i][temp_x] = temp
            break
          else:
            arr[i][temp_x] = temp * 2
            arr[i][k] = 0
            if(max < arr[i][temp_x]):
              max = arr[i][temp_x]
            break
        temp_x += 1
  # print('l', arr)
  return arr

def right(arr):
  global max
  for i in range(0, n):
    temp_x = n-1
    for j in range(n-1, -2, -1):
      if(j==-1):
        for k in range(temp_x, -1, -1):
          arr[i][k] = 0
        break
      else:
        if(arr[i][j] == 0):
          continue
        temp = arr[i][j]
        for k in range(j-1, -2, -1):
          if(k==-1):
            arr[i][temp_x] = temp
            break
          if(arr[i][k] == 0):
            continue
          elif(arr[i][k] != temp):
            arr[i][temp_x] = temp
            break
          else:
            arr[i][temp_x] = temp * 2
            arr[i][k] = 0
            if(max < arr[i][temp_x]):
              max = arr[i][temp_x]
            break
        temp_x -= 1
  # print('r', arr)
  return arr

def up(arr):
  global max
  for i in range(0, n):
    temp_y = 0
    for j in range(0, n+1):
      if(j==n):
        for k in range(temp_y, n):
          arr[k][i] = 0
        break
      else:
        if(arr[j][i] == 0):
          continue
        temp = arr[j][i]
        for k in range(j+1, n+1):
          if(k==n):
            arr[temp_y][i] = temp
            break
          if(arr[k][i] == 0):
            continue
          elif(arr[k][i] != temp):
            arr[temp_y][i] = temp
            break
          else:
            arr[temp_y][i] = temp * 2
            arr[k][i] = 0
            if(max < arr[temp_y][i]):
              max = arr[temp_y][i]
            break
        temp_y += 1
  # print('u', arr)
  return arr

def down(arr):
  global max
  for i in range(0, n):
    temp_y = n-1
    for j in range(n-1, -2, -1):
      if j==-1:
        for k in range(temp_y, -1, -1):
          arr[k][i] = 0
        break
      else:
        if(arr[j][i] == 0):
          continue
        temp = arr[j][i]
        for k in range(j-1, -2, -1):
          if(k==-1):
            arr[temp_y][i] = temp
            break
          if(arr[k][i] == 0):
            continue
          elif(arr[k][i] != temp):
            arr[temp_y][i] = temp
            break
          else:
            arr[temp_y][i] = temp * 2
            arr[k][i] = 0
            if(max < arr[temp_y][i]):
              max = arr[temp_y][i]
            break
        temp_y -= 1
  # print('d', arr)
  return arr

def rec_func(count, rec_arr):
  if(count > 5):
    return
  arr = copy.deepcopy(rec_arr)
  arr = left(arr)
  rec_func(count+1, arr)
  
  arr = copy.deepcopy(rec_arr)
  arr = right(arr)
  rec_func(count+1, arr)

  arr = copy.deepcopy(rec_arr)
  arr = up(arr)
  rec_func(count+1, arr)

  arr = copy.deepcopy(rec_arr)
  arr = down(arr)
  rec_func(count+1, arr)

rec_func(1, input_arr)
print(max)