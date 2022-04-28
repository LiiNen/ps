import math

n = int(input())

arr = []
arr.append([0 for i in range(0, n+4)])
arr.append([0 for i in range(0, n+4)])
for i in range(0, n):
  temp = input().split(' ')
  temp_arr = [0, 0] + [int(t) for t in temp] + [0, 0]
  arr.append(temp_arr)
arr.append([0 for i in range(0, n+4)])
arr.append([0 for i in range(0, n+4)])

west_x = [-1, 1, -2, 2, 0, -1, 1, -1, 1, 0]
west_y = [1, 1, 0, 0, -2, 0, 0, -1, -1, -1]
south_x = [-1, -1, 0, 0, 2, 0, 0, 1, 1, 1]
south_y = [-1, 1, -2, 2, 0, -1, 1, -1, 1, 0]
east_x = [1, -1, 2, -2, 0, 1, -1, 1, -1, 0]
east_y = [-1, -1, 0, 0, 2, 0, 0, 1, 1, 1]
north_x = [1, 1, 0, 0, -2, 0, 0, -1, -1, -1]
north_y = [1, -1, 2, -2, 0, 1, -1, 1, -1, 0]

## direction 0, 1, 2, 3 west, south, east, north
def sand_move(x, y, direction):
  global arr, n
  global west_x, west_y, south_x, south_y, east_x, east_y, north_x, north_y

  sand = arr[x][y]
  sand01 = math.floor(sand * 0.01)
  sand02 = math.floor(sand * 0.02)
  sand05 = math.floor(sand * 0.05)
  sand07 = math.floor(sand * 0.07)
  sand10 = math.floor(sand * 0.1)
  sand_left = sand - (2 * (sand01 + sand02 + sand07 + sand10)) - sand05
  sand_move_list = [sand01, sand01, sand02, sand02, sand05, sand07, sand07, sand10, sand10, sand_left]

  if(direction == 0):
    for i in range(0, 10):
      arr[x+west_x[i]][y+west_y[i]] += sand_move_list[i]
    arr[x][y] = 0
  elif(direction == 1):
    for i in range(0, 10):
      arr[x+south_x[i]][y+south_y[i]] += sand_move_list[i]
    arr[x][y] = 0
  elif(direction == 2):
    for i in range(0, 10):
      arr[x+east_x[i]][y+east_y[i]] += sand_move_list[i]
    arr[x][y] = 0
  elif(direction == 3):
    for i in range(0, 10):
      arr[x+north_x[i]][y+north_y[i]] += sand_move_list[i]
    arr[x][y] = 0

order_arr = []
dir_arr = []
move_weight = 0
move_x = [0, 1, 0, -1]
move_y = [-1, 0, 1, 0]

center = math.floor((n+4)/2)
x = center
y = center-1
direction_count = 1
count = 1
isFirst = True

while(True):
  if(x == 2 and y == 1):
    break

  order_arr.append([x, y])
  dir_arr.append(move_weight)

  if(direction_count == count):
    move_weight = (move_weight + 1)%4
    x = x + move_x[move_weight]
    y = y + move_y[move_weight]
    direction_count = 1
    if(isFirst):
      isFirst = False
    else:
      isFirst = True
      count = count + 1
  else:
    x = x + move_x[move_weight]
    y = y + move_y[move_weight]
    direction_count += 1

for i in range(0, len(order_arr)):
  sand_move(order_arr[i][0], order_arr[i][1], dir_arr[i])

sum = 0
for i in range(0, n+4):
  sum += arr[0][i]
  sum += arr[1][i]
  sum += arr[n+2][i]
  sum += arr[n+3][i]
  sum += arr[i][0]
  sum += arr[i][1]
  sum += arr[i][n+2]
  sum += arr[i][n+3]
for i in range(0, 2):
  for j in range(0, 2):
    sum -= arr[i][j]
    sum -= arr[i][n+2+j]
    sum -= arr[n+2+i][j]
    sum -= arr[n+2+i][n+2+j]
print(sum)
