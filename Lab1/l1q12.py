def generateFibonacci(numb):
    a = [1, 1]
    if(numb == 1):
        return a[0]
    elif(numb == 2):
        return a

    else:
        for i in range(2, numb):
            a.append(a[i-1] + a[i-2])
        return a


numb = int(input("How many Fibonacci numbers to generate? : "))

print(generateFibonacci(numb))
