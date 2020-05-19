#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quot = []
    for i in range(0, list_length):
        try:
            quot.append(my_list_1[i] / my_list_2[i])
        except (TypeError):
            print("wrong type")
            quot.append(0)
        except (ZeroDivisionError):
            print("division by 0")
            quot.append(0)
        except (IndexError):
            print("out of range")
            quot.append(0)
        finally:
            pass
    return quot
