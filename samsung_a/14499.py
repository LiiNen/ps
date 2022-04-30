nmxyk = input().split(' ')
n = int(nmxyk[0])
m = int(nmxyk[1])
x = int(nmxyk[2])
y = int(nmxyk[3])
k = int(nmxyk[4])

top = 0
left = 0
right = 0
up = 0
down = 0
bottom = 0

arr = []
for i in range(0, n):
  temp = [int(t) for t in input().split(' ')]
  arr.append(temp)

command_list = [int(c) for c in input().split(' ')]

def roll_right():
  global top, left, right, bottom
  temp = right
  right = top
  top = left
  left = bottom
  bottom = temp
  global y
  y += 1

def roll_left():
  global top, left, right, bottom
  temp = left
  left = top
  top = right
  right = bottom
  bottom = temp
  global y
  y -= 1

def roll_up():
  global top, up, down, bottom
  temp = up
  up = top
  top = down
  down = bottom
  bottom = temp
  global x
  x -= 1

def roll_down():
  global top, up, down, bottom
  temp = down
  down = top
  top = up
  up = bottom
  bottom = temp
  global x
  x += 1

def check():
  global arr, bottom
  if(arr[x][y] == 0):
    arr[x][y] = bottom
  else:
    bottom = arr[x][y]
    arr[x][y] = 0

for command in command_list:
  if(command == 1):
    if(y == m-1):
      continue
    roll_right()
  elif(command == 2):
    if(y == 0):
      continue
    roll_left()
  elif(command == 3):
    if(x == 0):
      continue
    roll_up()
  else:
    if(x == n-1):
      continue
    roll_down()
  check()
  print(top)