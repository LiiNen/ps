t = int(input())

field_array = []
queue = []

def bfs(x, y):
  global field_array, queue
  field_array[x][y] = 0
  if(x+1 < n and field_array[x+1][y] == 1):
    field_array[x+1][y] = 0
    queue.append([x+1, y])
  if(y+1 < m and field_array[x][y+1] == 1):
    field_array[x][y+1] = 0
    queue.append([x, y+1])
  if(x-1 >= 0 and field_array[x-1][y] == 1):
    field_array[x-1][y] = 0
    queue.append([x-1, y])
  if(y-1 >= 0 and field_array[x][y-1] == 1):
    field_array[x][y-1] = 0
    queue.append([x, y-1])
    

for case in range(0, t):
  line = input().split(' ')
  m = int(line[0])
  n = int(line[1])
  k = int(line[2])
  p_list = []
  field_array = [[0 for i in range(0, m)] for j in range(0, n)]
  for position in range(0, k):
    temp = input().split(' ')
    p_list.append([int(temp[1]), int(temp[0])])
    field_array[int(temp[1])][int(temp[0])] = 1
  count = 0
  
  # for i in range(0, n):
  #   print(field_array[i])

  for p in p_list:
    # print(p[0], p[1], count)
    if(field_array[p[0]][p[1]] == 0):
      continue
    else:
      queue.append([p[0], p[1]])
      while(1):
        bfs(queue[0][0], queue[0][1])
        queue.pop(0)
        if(len(queue) == 0):
          break
        # print(queue)
      count+=1
      # print('')
      # for i in range(0, n):
      #   print(field_array[i])
  print(count)