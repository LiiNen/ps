n = int(input())
k = int(input())

arr = [[0 for i in range(0, n)] for i in range(0, n)]

for i in range(0, k):
  xy = input().split(' ')
  arr[int(xy[0])-1][int(xy[1])-1] = 1

l = int(input())
l_list = []
for i in range(0, l):
  temp = input().split(' ')
  l_list.append([int(temp[0]), temp[1]])

# x, y, direction
# direction 0 right 1 down 2 left 3 up
snake_queue = [[0, 0]]
head_d = 0

x_dir = [0, 1, 0, -1]
y_dir = [1, 0, -1, 0]
count = 0
if(len(l_list) == 0):
  l_head = None
else:
  l_head = l_list[0]
while(True):
  count += 1
  # print(snake_queue)
  head = snake_queue[0]
  # print(head, head_d)
  nx = head[0] + x_dir[head_d]
  ny = head[1] + y_dir[head_d]

  if(nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or [nx,ny] in snake_queue):
    break
  else:
    snake_queue = [[nx, ny]] + snake_queue
    if(arr[nx][ny] == 1):
      arr[nx][ny] = 0
    else:
      snake_queue.pop()

  if(l_head != None and count == l_head[0]):
    if(l_head[1] == 'L'):
      head_d = (head_d-1) % 4
    else:
      head_d = (head_d+1) % 4
    l_list.pop(0)
    if(len(l_list) != 0):
      l_head = l_list[0]
    else:
      l_head == None

print(count)