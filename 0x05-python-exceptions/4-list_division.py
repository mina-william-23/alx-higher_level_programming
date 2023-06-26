#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    cnt = 0
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
            cnt += 1
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            if (cnt == i):
                cnt += 1
                new_list.append(0)
    return new_list
