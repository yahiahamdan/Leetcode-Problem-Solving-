
def generateUniqueString(length,un):
    uniqueChars=[chr(ord('a')+i) for i in range(un)]
    password=[]
    for i in range(length):
        password.append(uniqueChars[i%un])
    return ''.join(password)
print(generateUniqueString(5,3))