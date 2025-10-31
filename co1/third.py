numbers = [int(x) for x in input("Enter  integers: ").split()]
positive_num= [num for num in numbers if num > 0]
print("Positive numbers: ",positive_num)

n = int(input("enter no.of elements: "))
nums = [int(input(f"enter number {i+1}: ")) for i in range(n)]
squares = [x ** 2 for x in nums]
print("squares: ",squares)

word = input("Enter a word: ")
vowels = [ch for ch in word if ch.lower() in 'aeiou']
print("Vowels: ",vowels)

word = input("enter a word: ")
ord_value= [ord(ch) for ch in word]
print("Ordinal values: ",ord_value)
