a= [2, 3, 4, 5, 6]
mult=0
j=len(a) -1
i=0
while i!=j:
    mult = a[i]*a[j]
    i+=1
    j-=1
    print (mult)
if a[i]==a[j]:
    mult = a[i]*a[j]
print(mult)