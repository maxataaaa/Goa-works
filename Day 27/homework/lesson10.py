def unique_elements(collection):
    # სიაში შევქმნით ცარიელი set
    unique_set = set()
    # შევავსოთ set ელემენტებით სიის უნიკალურ ელემენტები
    for item in collection:
        unique_set.add(item)
    # შევაბრუნოთ სია, რომელშიც იქნება საწყის სიის უნიკალური ელემენტები
    return list(unique_set)


original_list = [1, 1, 1, 2, 3, 4]
new_list = unique_elements(original_list)
print(new_list)