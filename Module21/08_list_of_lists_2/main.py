nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def recursion_1(user_list):
    result = []
    for item in user_list:
        if isinstance(item, list):
            result.extend(recursion_1(item))
        else:
            result.append(item)
    return result


def recursion_2(user_list):
    if not user_list:
        return user_list
    if isinstance(user_list[0], list):
        return recursion_2(user_list[0]) + recursion_2(user_list[1:])
    else:
        return [user_list[0]] + recursion_2(user_list[1:])


flat_list = recursion_1(nice_list)
print(flat_list)
flat_list = recursion_2(nice_list)
print(flat_list)