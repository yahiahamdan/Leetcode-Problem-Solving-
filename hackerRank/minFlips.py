def minflips(s1,s2):
    flips=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            flips+=1
    return flips
print(minflips("11001","10011"))