def round_to_next5(n):
    while n%5:
        n+=1
    return n

next_num = round_to_next5(-2)
print(next_num)