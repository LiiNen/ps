t = int(input())

fibo_arr = [None for i in range(0, 41)]
fibo_count_zero = [None for i in range(0, 41)]
fibo_count_one = [None for i in range(0, 41)]
fibo_arr[0] = 0
fibo_arr[1] = 1
fibo_arr[2] = 1
fibo_count_zero[0] = 1
fibo_count_zero[1] = 0
fibo_count_zero[2] = 1
fibo_count_one[0] = 0
fibo_count_one[1] = 1
fibo_count_one[2] = 1

def fibo(n):
  global fibo_arr, fibo_count_one, fibo_count_zero
  za=oa=zb=ob=0
  if(fibo_arr[n] == None):
    za, oa = fibo(n-2)
    zb, ob = fibo(n-1)
    fibo_arr[n] = n
    fibo_count_zero[n] = za + zb
    fibo_count_one[n] = oa + ob
  return fibo_count_zero[n], fibo_count_one[n]
  
fibo(40)

for i in range(0, t):
  n = int(input())
  print(fibo_count_zero[n], fibo_count_one[n])