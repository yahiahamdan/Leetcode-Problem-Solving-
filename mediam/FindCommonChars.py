from collections import Counter
res=[]
def findCommonChars(words):
    firstCounter=Counter(words[0])
    for word in words:
        counterWord=Counter(word)
        for key in firstCounter:
           firstCounter[key]= min(firstCounter[key],counterWord[key])
    for c in  firstCounter:
        if c*firstCounter[c]:
            res.append(c)
    return res

print(findCommonChars(['labels','lab','labbey']))


def findsinglechars(word):
    newlist=[]
    freqchar=Counter(word)
    newlist= [key for key , value in freqchar.items() if value==1]
    return newlist
print(findsinglechars("aaabbbcde"))


    

