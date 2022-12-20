a=[1.1, 1.2, 3.1, 5, 10.001]
max=0
min=0.99
b=a[1]%int(a[1])
for i in range (len(a)):
    if round(a[i]%int(a[i]),3)!=0:
        b=round(a[i]%int(a[i]),3)
        if b>max:
            max=b
        elif b<min:
            min=b
print (max-min)