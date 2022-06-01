nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

flatter_list = [loop3 for loop in nice_list
                for loop2 in loop
                for loop3 in loop2]

print(flatter_list)
