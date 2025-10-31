li1=[]
li2=[]
n1=int(input("How many numbers in first list? "))
for i in range(n1):
    num= int(input("Enter number for list 1:  "))
    li1.append(num)

n2=int(input("How many numbers in second list? "))
for i in range(n2):
    num= int(input("Enter number for list 2:  "))
    li2.append(num)
    
print("List 1: ",li1)
print("List 2: ",li2)

if len(li1) == len(li2):
    print("Both lists have same length")
else:
    print("Lists have different lengths")

if sum(li1) == sum(li2):
    print("Sum of both lists are same")
else:
    print("Lists have different sum")

common=[]
for item in li1:
    if item in li2 and item not in common:
        common.append(item)
if len(common) > 0:
    print("Common values: ",common)
else:
    print("No common values")
