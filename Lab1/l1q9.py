import random
rand_numb = random.randint(1, 9)
# print(rand_numb)

guess_numb = int(input("Guess a number between 1-9 : "))

if(guess_numb < rand_numb):
    print("too low")

elif(guess_numb > rand_numb):
    print("too high")

else:
    print("Exactly right !")
