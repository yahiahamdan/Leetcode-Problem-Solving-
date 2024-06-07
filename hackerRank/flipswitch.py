def minNumberOfFlipe(pwd):
    minNumber=0
    for i in range(0,len(pwd),2):
        if i+1 < len(pwd) and pwd[i]!=pwd[i+1]:
            minNumber+=1
    return minNumber

print(minNumberOfFlipe("0101010"))