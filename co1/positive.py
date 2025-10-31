numbers = [int(x) for x in input("Enter  integers: ").split()]
positive_num= [num for num in numbers if num > 0]
print("Positive numbers: ",positive_num)

n = int(input("enter no.of elements: "))
nums = [int(input(f"enter number {i+1}: ")) for i in range(n)]
squares = [x ** 2 for x in nums]
print("squares: ",squares)
