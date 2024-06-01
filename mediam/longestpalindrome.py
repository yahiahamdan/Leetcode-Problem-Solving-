#brute force solution to solve this type of problem 0(npow3)
def isPlaindrome(string):
    news=string[::-1]
    return news==string
def longestpalindrom(string):
    maxlength=0
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            newSubstring=string[i:j]
            #print(newSubstring)
            if isPlaindrome(newSubstring):
                maxlength=max(maxlength,len(newSubstring))
    return maxlength
    #return maxlength if maxlength !=float('-inf') else 0 

print(longestpalindrom("babad"))
