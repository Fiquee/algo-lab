def destroyDuplicate(list_):
    newlist = []
    for i in range(len(list_)):
        if(list_[i] not in newlist):
            newlist.append(list_[i])

    return newlist


list_ = [1, 1, 1, 1, 2, 4, 5, 5, 8, 7, 6, 6]

print(destroyDuplicate(list_))
