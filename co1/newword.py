word= input("Enter a word: ")
first = word[0]
new_word= first
for ch in word[1:]:
    if ch == first:
        new_word += '$'
    else:
        new_word += ch

print("Modified word: ",new_word)
