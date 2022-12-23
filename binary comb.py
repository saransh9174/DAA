def per(n):
    for i in range(1<<n):
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        print (list(map(int,list(s))))

print("Enter number: ")
n=int(input("Enter value of n: "))
per(n)       