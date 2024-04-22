def manual_pop(colection,delete_index):
    new_colection = []

    for index in range(0,len(colection)):
        if index != delete_index:
            new_colection.append(colection[index])

    return new_colection
names = ['anastasia','nika','gio']
print(manual_pop(names,0))