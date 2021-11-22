def divisors(n):
    divis = n
    answer = 0
    while divis:
        if n%divis == 0:
            answer += 1
        divis -= 1
    return answer

div = divisors(5)
print(div)