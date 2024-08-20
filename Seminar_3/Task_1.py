
my_list = [1, 1, 2, 33, 3, 3, 4, 4, 5, 6, 7]

result = list(set(my_list))

result_2 = []
for item in my_list:
    if not item in result_2:
        result_2.append(item)
print(f'{result = }')
print(f'{result_2 = }')