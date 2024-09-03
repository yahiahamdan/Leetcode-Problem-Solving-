"""
ana 3ndy length we no of unique values 

"""

def generateUnique(l,u):
    uniqueString=[]
    result=""
    for i in range(u):
        uniqueString.append(chr(ord('a')+i))
    for i in range(l):
        result+=uniqueString[i%u]
    return result

print(generateUnique(5,3))

           