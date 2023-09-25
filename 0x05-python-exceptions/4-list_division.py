#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    out_list = []
    for i in range(list_length):
        current = 0
        try:
            current = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            out_list.append(current)

    return out_list
