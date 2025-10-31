names=[]
n = int(input("How many names? "))
for i in range(n):
    name= input("enter name: ")
    names.append(name)

count_a=0
for name in names:
    count_a += name.lower().count('a')

print("List of names: ",names)
print("Total occurences of 'a': ",count_a)
