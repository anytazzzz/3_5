def get_multiplied_digits(number):
    str_number = str(number)

    if len(str_number) > 1:

        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        first = int(str_number[0])
        if first != 0:
            return first
        else:
            return 1
        return int(str_number)

result = get_multiplied_digits(4020203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)