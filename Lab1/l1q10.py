def checkPrime(numb):
    for i in range(2, numb):
        if(numb % i == 0):
            return False

    return True


numb = int(input("Enter a number : "))

if(numb == 1):
    print(str(numb) + " is not prime number")
elif(numb == 2):
    print(str(numb) + " is prime number")
else:
    if(checkPrime(numb)):
        print(str(numb) + " is prime number")
    else:
        print(str(numb) + " is not prime number")
