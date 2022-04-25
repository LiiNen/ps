import copy

ms = input().split(' ')
m = int(ms[0])
s = int(ms[1])

## direction start with west, clockwise
fish_arr = []
for i in range(0, m):
  temp = input().split(' ')
  temp_arr = [int(temp[0])-1, int(temp[1])-1, int(temp[2])]
  fish_arr.append(temp_arr)
shark = input().split(' ')
shark_xy = [int(shark[0])-1, int(shark[1])-1]

rem_fish_arr = []

smell_arr_one = [[False for i in range(0, 4)] for j in range(0, 4)]
smell_arr_two = [[False for i in range(0, 4)] for j in range(0, 4)]

fish_count_arr = [[0 for i in range(0, 4)] for j in range(0, 4)]

max_fish = [0, 0, 0]

def fish_remember():
  global rem_fish_arr, fish_arr
  rem_fish_arr = copy.deepcopy(fish_arr)

def check_move(x, y, direction, index):
  global shark_xy, smell_arr_one, smell_arr_two, fish_arr
  count = 0
  while(count < 8):
    dx = x
    dy = y
    if(direction == 1):
      dy = y - 1
    elif(direction == 2):
      dy = y - 1
      dx = x - 1
    elif(direction == 3):
      dx = x - 1
    elif(direction == 4):
      dx = x - 1
      dy = y + 1
    elif(direction == 5):
      dy = y + 1
    elif(direction == 6):
      dy = y + 1
      dx = x + 1
    elif(direction == 7):
      dx = x + 1
    elif(direction == 8):
      dx = x + 1
      dy = y - 1
    if(dx < 0 or dy < 0 or dx > 3 or dy > 3 or (dx == shark_xy[0] and dy == shark_xy[1]) or smell_arr_one[dx][dy] == True or smell_arr_two[dx][dy] == True):
      count += 1
      direction = direction - 1
      if(direction == 0):
        direction = 8
    else:
      break
  if(count == 8):
    fish_count_arr[x][y] += 1
  else:
    fish_arr[index] = [dx, dy, direction]
    fish_count_arr[dx][dy] += 1
  # print(count)

max_num = -1
eat_list = []

def shark_step(x, y, eat_num, step_count, prev):
  global max_num, eat_list, shark_xy, max_fish
  new_prev = copy.deepcopy(prev)
  new_prev.append([x, y])
  if([x, y] not in prev):
    eat_num += fish_count_arr[x][y]

  if(step_count == 3):
    if(eat_num > max_num):
      max_num = eat_num
      eat_list = copy.deepcopy(new_prev)
      shark_xy = [x, y]
    return
  else:
    if(step_count == 2):
      if(eat_num + max_fish[0] < max_num):
        return
    if(step_count == 1):
      if(eat_num + max_fish[0] + max_fish[1] < max_num):
        return

  if(x-1 >= 0):
    shark_step(x-1, y, eat_num, step_count+1, new_prev)
  if(y-1 >= 0):
    shark_step(x, y-1, eat_num, step_count+1, new_prev)
  if(x+1 < 4):
    shark_step(x+1, y, eat_num, step_count+1, new_prev)
  if(y+1 < 4):
    shark_step(x, y+1, eat_num, step_count+1, new_prev)

def shark_move():
  global shark_xy, eat_list, fish_arr, max_fish
  x = shark_xy[0]
  y = shark_xy[1]

  if(x-1 >= 0):
    shark_step(x-1, y, 0, 1, [])
  if(y-1 >= 0):
    shark_step(x, y-1, 0, 1, [])
  if(x+1 < 4):
    shark_step(x+1, y, 0, 1, [])
  if(y+1 < 4):
    shark_step(x, y+1, 0, 1, [])

  new_arr = []
  for fish in fish_arr:
    if([fish[0], fish[1]] not in eat_list):
      new_arr.append(fish)
  fish_arr = copy.deepcopy(new_arr)

  
def smell():
  global smell_arr_one, smell_arr_two, eat_list
  smell_arr_two = copy.deepcopy(smell_arr_one)
  smell_arr_one = [[False for i in range(0, 4)] for j in range(0, 4)]
  for eat in eat_list:
    if(fish_count_arr[eat[0]][eat[1]] > 0):
      smell_arr_one[eat[0]][eat[1]] = True

def copy_fish_remember():
  global rem_fish_arr, fish_arr
  for i in range(0, len(rem_fish_arr)):
    fish_arr.append(rem_fish_arr[i])
  rem_fish_arr = []

for i in range(0, s):
  max_num = -1
  eat_list = []
  fish_count_arr = [[0 for i in range(0, 4)] for j in range(0, 4)]

  fish_remember()

  for i in range(0, len(fish_arr)):
    check_move(fish_arr[i][0], fish_arr[i][1], fish_arr[i][2], i)
  
  max_fish = [0, 0, 0]

  for i in range(0, 4):
    for j in range(0, 4):
      tc = fish_count_arr[i][j]
      if(tc >= max_fish[1]):
        max_fish[1] = tc
        if(tc >= max_fish[0]):
          max_fish[1] = max_fish[0]
          max_fish[0] = tc       

  shark_move()

  smell()
  # for i in range(0, 4):
  #   print(smell_arr_one[i])
  
  copy_fish_remember()
  # for i in range(0, 4):
  #   print(fish_count_arr[i])

print(len(fish_arr))