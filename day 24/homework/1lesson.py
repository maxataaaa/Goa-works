def int_sum(arr):
    sum = 0
    for i in arr:
     if type(i) == int:
        sum += i
    print(sum)

int_sum([1, 2, 3, True, False, 1.5, 3.14, 5, "Hello"])