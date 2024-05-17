def reverseWords(s):
#this first solution 
    res=""
    string=s.strip()
    stringArray=string.split()
    for i in range(len(stringArray)-1,-1,-1):
        res+=stringArray[i]+" "
    return f" '{res.strip()}'"
print(reverseWords("this sky is blue     "))
#second solution
def reverseWords2(s):
     return " ".join([i for i in reversed(s.split()) if i])