s = "hgzgazjkzfzizzzz"
x = 0
for i in range(len(s)):
    if s[i]=="a":
        t = i
for i in range(t,len(s)):
    if s[i]=="z":
        x+=1
print(x) 