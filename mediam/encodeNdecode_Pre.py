"""
its very decent list of string
encode   we want tonc
need code convert to single string 
encoded into a single likst 
another singlestring
leet#code
speical character  it bound remaining portion 
neet#co#de   in orignal who have 2 words 
solution dh s7 any a store lenght bs they want it statless
if we say 4neet5codes
4#delimter between integer and delimter 
next 4 charcter
4# integet followed by boundsign  
4#leet4#cod38##mon#key
"""


def encode(string):
 res=""
 for s in string:
   res+=str(len(s))+'#'+s
 return res


def decode (words):
  res=[]
  i=0
  while  i < len(words):
     
     j=words.find('#',i)
     length=int(words[i:j])
     res.append(words[j+1:length+j+1])
     i=j+1+length
  return res
print(decode("3#lee5#yahia"))


