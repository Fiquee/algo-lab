a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number_list = ""
for i in range(len(a)):
    if(a[i] < 5):
        number_list += str(a[i]) + ", "


print(number_list)
