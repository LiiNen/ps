nmk = input().split(' ')
n = int(nmk[0])
m = int(nmk[1])
k = int(nmk[2])

arr = []

position = [0, 0]

top = 1
left = 4
right = 3
up = 2
down = 5

# direction 0 for east, 1 for south, 2 for west, 3 for north
direction = 0

def bottom():
  global top
  return 7-top

def right_move():
  global left, top, right, position
  temp = top
  right = top
  top = left
  left = 7-temp
  position[1] = position[1]+1

def left_move():
  global left, top, right, position
  temp = top
  left = top
  top = right
  right = 7-temp
  position[1] = position[1]-1

def up_move():
  global up, top, down, position
  temp = top
  up = top
  top = down
  down = 7-temp
  position[0] = position[0]-1

def down_move():
  global up, top, down, position
  temp = top
  down = top
  top = up
  up = 7-temp
  position[0] = position[0]+1

def set_direction():
  global arr, position, direction, top, left, right, up, down
  value = arr[position[0]][position[1]]
  if(bottom() > value):
    direction = (direction + 1)%4
  elif(bottom() < value):
    if(direction == 0):
      direction = 3
    else:
      direction = direction - 1

ans = 0

def dice_roll():
  global position, direction, ans
  if(direction == 0):
    if(position[1] == m-1):
      direction = 2
      left_move()
    else:
      right_move()
  elif(direction == 1):
    if(position[0] == n-1):
      direction = 3
      up_move()
    else:
      down_move()
  elif(direction == 2):
    if(position[1] == 0):
      direction = 0
      right_move()
    else:
      left_move()
  elif(direction == 3):
    if(position[0] == 0):
      direction = 1
      down_move()
    else:
      up_move()
  ans = ans + cal()

count = 0,
rem = []

def cal():
  global arr, position, top, count, rem
  count = 0
  rem = []
  value = arr[position[0]][position[1]]
  # print(value, position[0], position[1])
  dfs(value, position[0], position[1])
  for i in range(0, len(rem)):
    arr[rem[i][0]][rem[i][1]] = value
  # print(position, count * value, count, value)
  # print(arr)
  return count * value

def dfs(value, x, y):
  if(x >= n or x < 0 or y >= m or y < 0):
    return
  global arr, rem, count
  if(arr[x][y] == value):
    count = count + 1
    arr[x][y] = -1
    rem.append([x,y])
    dfs(value,x+1,y)
    dfs(value,x-1,y)
    dfs(value,x,y+1)
    dfs(value,x,y-1)
    return
  else:
    return

for i in range(0, n):
  temp = []
  line = input().split(' ')
  for j in range(0, m):
    temp.append(int(line[j]))
  arr.append(temp)

for i in range(0, k):
  dice_roll()
  set_direction()

print(ans)