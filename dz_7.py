input_list = [23, 45, 23, 33, 1, 2, 4, 4, 45, 33]

def count_number(num: int) -> int:
    return input_list.count(num)

def create_dict():
    return {num: count_number(num) for num in set(input_list)}

print(input_list)
print(create_dict())