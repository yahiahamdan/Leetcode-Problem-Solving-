def beaut(string):
    counter=0
    for i in range(1,len(string)):
        if string[i]==string[i-1] or abs(ord(string[i-1]-ord(string[i])))==1:
            counter+=1
    return counter

print(beaut("abcefbc")) 

