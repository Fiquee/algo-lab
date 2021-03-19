word = input("Enter a word : ")

word = word.replace(" ", "")
reverseword = word[::-1].replace(" ", "")

if(word == reverseword):
    print("palindrome")

else:
    print("non-palindrome")
