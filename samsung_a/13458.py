import math

n = int(input())
arr = [int(t) for t in input().split(' ')]
bc = input().split(' ')
b = int(bc[0])
c = int(bc[1])

count = len(arr)
for s in arr:
  if(s-b <= 0):
    continue
  count += math.ceil((s-b)/c)
print(count)