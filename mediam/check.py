from collections import Counter
def validstring(string):
    hashdict=Counter(string)
    mostFreqChar=hashdict.most_common(1)[0][0]
    print(mostFreqChar)
validstring("abcdeaaa")