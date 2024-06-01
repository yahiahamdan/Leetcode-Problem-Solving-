def reverse(x):
    lastelement=0
    reminder=0
    is_negitive= x < 0
    rangeNum=abs(x)
    while rangeNum!=0:
        lastelement=rangeNum%10
        reminder=reminder*10+lastelement
        rangeNum=rangeNum//10
    if is_negitive:
        return reminder * -1
    return reminder
print(reverse(-123))