n = int(input())

p_list = []
t_list = []
max_list = [0 for i in range(0, n+1)]
for i in range(0, n):
  pt = input().split(' ')
  p = int(pt[0])
  if(i + p > n):
    p_list.append(0)
    t_list.append(0)
    continue
  t = int(pt[1])
  p_list.append(t)
  t_list.append(p)

def select(day, value):
  if(max_list[day] > value):
    return
  else:
    max_list[day] = value
  if(day == n):
    return
  while(day < n and p_list[day] == 0):
    day += 1
    if(day == n):
      return
    if(max_list[day] < value):
      max_list[day] = value
  select(day+t_list[day], value+p_list[day])
  if(day+1 == n):
    return
  else:
    select(day+1, value)

select(0, 0)

# print(p_list)
# print(max_list)
print(max(max_list))
