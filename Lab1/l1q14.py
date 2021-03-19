def reverseSentence(sentence):
    c = sentence.split(" ")
    reverse = ""
    for i in range(len(c)-1, -1, -1):
        reverse += str(c[i]) + " "

    return reverse


sentence = input("Enter a long string : ")


print(reverseSentence(sentence))
