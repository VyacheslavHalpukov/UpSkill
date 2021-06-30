def PalindromeSwapper(strParam):
    mirr = strParam[::-1]

    if mirr == strParam:
        return strParam

    variants = [mirr[:i] + mirr[i:i + 2][::-1] + mirr[i + 2:] for i in range(len(strParam) - 1)]

    for i in range(len(variants)):
        print(i, 'I', variants[i], strParam)
        if variants[i] == strParam:
            return strParam
        else: return '-1'


print(PalindromeSwapper("anna"))