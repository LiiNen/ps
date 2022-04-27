import copy
import math

nmk = input().split(' ')
n = int(nmk[0])
m = int(nmk[1])
k = int(nmk[2])

fireball = [[[] for i in range(0, n)] for i in range(0, n)]
new_fireball = [[[] for i in range(0, n)] for i in range(0, n)]

for i in range(0, m):
  temp = input().split(' ')
  msd = {
    'm': int(temp[2]),
    's': int(temp[3]),
    'd': int(temp[4])
  }
  fireball[int(temp[0])-1][int(temp[1])-1].append(msd)

# print(fireball)

def move_over(x, y):
  global n
  nx = x
  ny = y
  while(nx < 0):
    nx += n
  while(nx >= n):
    nx -= n
  while(ny < 0):
    ny += n
  while(ny >= n):
    ny -= n
  return [nx, ny]

def fireball_move(x, y, massive, dir, speed):
  global new_fireball
  nx = x
  ny = y
  if(dir == 0):
    nx -= speed
  elif(dir == 1):
    nx -= speed
    ny += speed
  elif(dir == 2):
    ny += speed
  elif(dir == 3):
    ny += speed
    nx += speed
  elif(dir == 4):
    nx += speed
  elif(dir == 5):
    nx += speed
    ny -= speed
  elif(dir == 6):
    ny -= speed
  elif(dir == 7):
    ny -= speed
    nx -= speed
  new_position = move_over(nx, ny)
  new_fireball[new_position[0]][new_position[1]].append({
    'm': massive,
    's': speed,
    'd': dir
  })

def fireball_cast():
  global fireball, n
  for i in range(0, n):
    for j in range(0, n):
      if(len(fireball[i][j]) == 0):
        continue
      else:
        for fire in fireball[i][j]:
          fireball_move(i, j, fire['m'], fire['d'], fire['s'])

def fireball_sum():
  global new_fireball, n
  for i in range(0, n):
    for j in range(0, n):
      if(len(new_fireball[i][j]) < 2):
        continue
      else:
        even = (new_fireball[i][j][0]['d'] % 2 == 0)
        dir_weight = 0
        isbreak = False
        sum_m = 0
        sum_s = 0
        for fire in new_fireball[i][j]:
          sum_m += fire['m']
          sum_s += fire['s']
          if(not isbreak):
            if(even != (fire['d'] % 2 == 0)):
              dir_weight = 1
              isbreak = True
        
        new_m = math.floor(sum_m/5)
        if(math.floor(sum_m / 5) == 0):
          new_fireball[i][j] = []
          continue
        new_s = math.floor(sum_s/len(new_fireball[i][j]))
        
        new_fireball[i][j] = []
        for k in range(0, 4):
          new_fireball[i][j].append({
            'm': new_m,
            's': new_s,
            'd': 2*k + dir_weight
          })

for i in range(0, k):
  fireball_cast()
  fireball_sum()
  fireball = copy.deepcopy(new_fireball)
  new_fireball = [[[] for i in range(0, n)] for i in range(0, n)]
  # print(fireball)

t_sum = 0
for i in range(0, n):
  for j in range(0, n):
    for fire in fireball[i][j]:
      t_sum += fire['m']
print(t_sum)