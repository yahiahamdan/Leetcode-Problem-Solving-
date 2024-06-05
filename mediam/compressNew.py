from collections import Counter
def compress(word):
    res=""
    count=1
    for i in range(1,len(word)):
        if word[i-1] == word[i]:
          count+=1
        else:
           if count>1:
              res+=word[i-1]+str(count)
              
           else:
                res+=word[i-1]
           count=1
    if count>1:
        res+=word[-1]+str(count)
    else:
        res+=word[-1]
    return res
       
print(compress("aabcc"))

def compress2(word):
    res=""
    wordCount=Counter(word)
    for key,value in wordCount.items():
        if value>1:
            res+=key+str(value)
        else:
            res+=key
    return res
print(compress2("aabcc"))
