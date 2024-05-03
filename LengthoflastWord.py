def lengthOfLastWord(s):
    leadingSpace=s.strip() 
    stringArray=leadingSpace.rsplit(' ')
    return len(stringArray[-1]) 
print(lengthOfLastWord("hello world   "))