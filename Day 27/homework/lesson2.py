def transform_names(names):
    transformed_names = []
    for i, name in enumerate(names):
        if i % 2 == 0:  # თუ ლუწ ინდექსია
            transformed_names.append(name.upper())
        else:  # თუ კენტ ინდექსია
            transformed_names.append(name.lower())
    return transformed_names


my_names = ["chad1", "chad2", "chad3", "chad4"]
transformed_list = transform_names(my_names)
print(transformed_list)