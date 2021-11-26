def disarium_number(number):
    new_number = list(number)
    result_number = 0
    for i, j in enumerate(new_number):
        result_number = result_number + int(j)**int(i)
    return result_number
    # return new_number

nu = disarium_number('12')
print(nu)