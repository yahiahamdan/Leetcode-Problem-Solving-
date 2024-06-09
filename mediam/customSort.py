"""
i have a string and i want to do a custom sort  for example i want to make no then upper then lower 
output A1b2xe3   result = 123Abex
"""
def customSort(s):
    s=sorted(s,key=lambda x:(x.isdigit(),x.isupper(),x))
    return ''.join(s)
print(customSort("A1b2xe3")) 

def customsort2(s):
    for i in range(len(s)):
        if s[i].isdigit():
          return [0,s[i]]
        elif s[i].isupper():
            return [1,s[i]]
        else:
            return [2,s[i]]

s="A1b2xe3"
print(''.join(sorted(s,key=customsort2)))


def customSort3(string1):
     digitList=[s for s in string1 if s.isdigit()]
     smallerLetter=[s for s in string1 if s.islower()]
     capitalLetter=[s for s in string1 if s.isupper()]
     digitList.sort()
     smallerLetter.sort()
     capitalLetter.sort()
     newword= ''.join(digitList+smallerLetter+capitalLetter)
     return newword
print(customSort3("aX123BDEbc"))


def customsort4(list1,list2):
    list1.sort()
    list2.sort()
    return list1+list2
print(customsort4([1,5,2,8],["a","x","d","c" ]))




















