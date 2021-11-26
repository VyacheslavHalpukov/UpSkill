def disarium_number(number):
    number_str = str(number)
    new_number = list(number_str)
    result_number = 0
    for i, j in enumerate(new_number):
        result_number = result_number + int(j)**int(i + 1)
    if number == result_number:
        return "Disarium !!"
    else:
        return "Not !!"
    # return new_number

nu = disarium_number(1024)
print(nu)