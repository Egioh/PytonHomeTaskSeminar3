b = 45
c = 4
d= 0
list =[]
i=0
while c//2!=0: 
    c = b//2
    d= b%2
    b=c
    list.append(d)
    i+=1
if c//2!=1:
    list.append(c)
list.reverse()
print (list)