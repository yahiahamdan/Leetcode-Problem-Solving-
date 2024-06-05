"""
the problem says we have abcddddeeeeaabbbcd 
return index of most than 3 
[]
"""
def validString(string):
  left=0
  n=len(string)
  res=[]
  for right in range(1,n):
     if string[right] !=string[right-1] or right == n :
             if right-left >=3 :
                 res.append([left,right-1])
             left=right
    
  if n-left >=3:
         res.append([left,n-1])  
  return res

print(validString("aaaabcdddeeee"))

#decodeStrng 
def decodeString(string):
     newstring=""
     word=""
     multipler=1
     for c in string:
          if c.isdigit():
               multipler= int(c)
          else:
               newstring+=c*multipler
               multipler=1
     return newstring
print(decodeString("a3b4cd"))
        