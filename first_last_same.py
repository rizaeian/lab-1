def first_last_same(number_list):
    print("your_list:", number_list)

    first_num = number_list[0]
    last_num = number_list[-1]

    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [4, 5, 6, 7, 4]
print("result is", first_last_same(numbers_x))

numbers_y = [8, 9, 10, 11, 12]
print("result is", first_last_same(numbers_y))