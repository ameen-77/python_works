word= input("enter a word: ")
if len(word) > 1:
    new_word = word[-1] + word[1:-1] + word[0]
else:
    new_word=word

print("after swapping: ",new_word)
