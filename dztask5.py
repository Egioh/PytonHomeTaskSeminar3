list=[]
fib1 = fib2 = 1
list.append(fib1)
list.append(fib2)
 
n = int(input("n="))
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    list.append(fib2)
#print(list)
for i in range (len(list)):
    if i%2==1:
        list[i]=list[i]*-1
list.reverse()
list.append(0)

fib1 = fib2 = 1
list.append(fib1)
list.append(fib2)
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    list.append(fib2)

print (list)