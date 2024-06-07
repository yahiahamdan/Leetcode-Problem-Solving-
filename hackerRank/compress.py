def compress(word):
    res=""
    counter=1
    for i in range(1,len(word)):
        if word[i-1]==word[i]:
           counter+=1
        else:
            if counter>1:
              res+=word[i-1]+str(counter)
            else:
               res+=word[i-1]
            counter=1
    if counter>1:
        res+=word[-1]+str(counter)
    return res

print(compress("aababbcdcccc"))
        



