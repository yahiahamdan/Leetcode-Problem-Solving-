"""
i have string 3a2bc 
aaabbc
string gdeed =""
"""
def convertString(s):
  res=""
  i=0
  while i<len(s):
    if s[i].isdigit():
        count=int(s[i])
        i+=1
        if(i<len(s)):
           res+=s[i]*(count-1)
    else:
     res+=s[i]
     i+=1
  return res

print(convertString("3a2cab5y"))