def num(numbers):
    positive = 0
    negative = 0

    for num in numbers:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += num

    return positive, negative,


numbers = [1, -2, 3, -4, 5]
positive, negative, = num(numbers)
print("dadebiti ricxvebis jami:", positive)
print("uaryopiti ricxvebis jami:", negative)