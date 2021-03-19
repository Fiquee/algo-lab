numb = int(input("Enter a number : "))

list_ = []

for i in range(1, numb+1):
    if(numb % i == 0):
        list_.append(i)


print("Divisor for " + str(numb) + " is : " + str(list_))
