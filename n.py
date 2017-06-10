my_list = {'a':3, 'b':1, 'c':6, 'd':4, 'e':0}

numba = len(my_list)
allocated_offices = []

for no in my_list.keys():
    if numba > 3:
        print(my_list[no])

        allocated_offices.append(no)
        print(my_list)

for key in allocated_offices:
    del my_list[key]
print(my_list)
