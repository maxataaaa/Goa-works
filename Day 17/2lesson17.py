def number(number6, num5, num6,):
    if num5 >= len(number6):
        print("Error The specified index is out of range.")


    number6[num5] = num6

    result = " ".join(number6)
    print("Result", result)


number6 = ["baro", "salami", "DDD", "gg"]
number7 = int(input("Enter the index you want to change: "))
number8 = input("Enter the new string: ")
number(number6, number7, number8)