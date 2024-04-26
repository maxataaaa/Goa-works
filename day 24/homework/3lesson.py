def num():
    new_arr = []
    user_input = int(input('enter num:'))
    for i in range(1,user_input + 1):
        if user_input % i == 0:
            new_arr.append(i)
    print(new_arr)

num()