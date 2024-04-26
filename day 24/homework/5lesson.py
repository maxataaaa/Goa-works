def most_repeated(arr):
    newarr = []
    for i in arr:
        count = arr.count(i)
        newarr.append(count)
    print(max(newarr))

most_repeated([1, 1, 1, 1, 3, 4, 5, 6])

