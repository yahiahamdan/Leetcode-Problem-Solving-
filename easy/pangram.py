"""
the problem ask will give us 2 paramters length,string
if the word 
f all the characters of the alphabet of this language appear in it at least once

"""
def pangram(length,word):
    if len(word)<26:
        return "NO"
    else:
        word=word.lower()
        for i in range(97,123):
            if chr(i) not in word:
                return "NO"
        return "YES"
    
print(pangram(35,"TheQuickrownFoxJumpsOverTheLazyDog")) #YES