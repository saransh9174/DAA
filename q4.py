l=[]

n=int(input("Enter the size of array: "))
print("accepted")
for i in range(n):
    ele=int((input("Enter element for array: ")))
    l.append(ele)
    print(l)
for i in range(len(l)):
    print("sum: ")
    print(sum(l))   