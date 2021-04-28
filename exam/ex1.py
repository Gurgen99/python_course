import random
def genarate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-10,10)
        arr.append(a)    
    return arr
arr = genarate_arr(8)
print(arr)
k = arr[0]
t = 0
for i in range(1,len(arr)):
    if arr[i]==k:
        t+=1
print(t)
