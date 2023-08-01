from datetime import datetime as dt

def count_time(func):
    def count(*args, **kwargs):
        time_1 = dt.now()
        return_values = func(*args, **kwargs)
        time_2 = dt.now()
        print(f'Time of working program: {time_2-time_1}')
        return return_values
    return count

@count_time
def even_numbers(arr, n):
    return [item for item in arr if item%2==0][-n:]

@count_time
def distinct(seq):
    return_list = []
    for item in seq:
        if item not in return_list:
            return_list.append(item)
    return return_list


print(even_numbers([1, 4, 6, 8], 2))
print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))

