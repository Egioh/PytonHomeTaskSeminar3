a= [2, 3, 5, 9, 3,3]
sum=0
for i in range (len(a)):
    print(i)
    if i%2!=0:
        sum+=a[i]
print (sum)