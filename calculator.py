a = input("gorcoxutyun:")
ind = []
tiv = []
for i in range(len(a)):
    if a[i] == "*" or a[i] == "/" or a[i] == "+" or a[i] == "-":
        ind.append(a[i])
    else:
        tiv.append(int(a[i]))
print(ind, tiv)

j = 0
while j < len(ind) and j>=0:
    if ind[j] == "*": 
        b = tiv[j] * tiv[j+1]
        tiv.pop(j)
        tiv.pop(j)
        tiv.insert(j,b)
        ind.pop(j)    
        print(tiv,ind)
        j-=1
    elif ind[j] == "/":
        b = tiv[j] / tiv[j+1]
        tiv.pop(j)
        tiv.pop(j)
        tiv.insert(j,b)
        ind.pop(j)    
        print(tiv,ind)
        j-=1
    j+=1

k = 0  
while k < len(ind) and k>=0:
    if ind[k] == "+":
        d = tiv[k] + tiv[k+1]
        tiv.pop(k)
        tiv.pop(k)
        tiv.insert(k,d)
        ind.pop(k)
        print(tiv,ind)
        k-=1
    elif ind[k] == "-":
        d = tiv[k] - tiv[k+1]
        tiv.pop(k)
        tiv.pop(k)
        tiv.insert(k,d)
        ind.pop(k)
        print(tiv,ind)
        k-=1
    k+=1
print(tiv[])