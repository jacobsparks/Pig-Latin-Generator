# this program translates any word you input into pig latin


userWord = input("Enter any word:")

pig = "ay"


if len(userWord) > 0 and userWord.isalpha():
    word = userWord.lower()
    first = word[0]
    new = word[1:] + first + pig
    print(new)
else:
    print("INPUT INVALID")




