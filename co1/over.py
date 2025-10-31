numbers=[]
n = int(input("How many numbers? " ))
for i in range(n):
    num= int(input("Enter number: "))
    numbers.append(num)

result=[]
for num in numbers:
    if num>100:
        result.append("over")
    else:
        result.append(num)

print("Final list: ",result)
