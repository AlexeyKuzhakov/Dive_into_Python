my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4)
print(spam)
aggs = my_list.index(4, spam + 1, 90)
print(aggs)