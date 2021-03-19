def newList(a):
    c = []
    c.append(a[0])
    c.append(a[len(a)-1])
    return c


a = [5, 10, 15, 20, 25]

list_ = newList(a)
print(list_)
