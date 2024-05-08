def process_numbers(numbers):
    processed_numbers = []
    for num in numbers:
        if num.is_integer():  # თუ რიცხვი მთელია
            processed_numbers.append(num * 2)
        else:  # თუ რიცხვი ათწილადია
            processed_numbers.append(num * 4)
    return processed_numbers


my_numbers = [1, 1.5, 2, 2.5]
processed_list = process_numbers(my_numbers)
print(processed_list)