def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) == 0 or len(arr) == 1:
        return 0
    else:
        return sum(arr) - min(arr) - max(arr)

print(sum_array(None))