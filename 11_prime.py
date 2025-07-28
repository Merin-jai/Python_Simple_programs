# 11. Print all prime numbers between 1 and 50

for n in range(2,51) :
    prime = 1
    l = int(n/2)
    for i in range(2,l+1) :
        if n%i==0 :
            prime=0
    if prime == 1 :
        print(n,end=" ")

