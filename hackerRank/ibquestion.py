"""
i have 
[2,4,3]  

arr[0]=2
arr[1]=4 
compare with arr[0] =2 
"""
def ibmQuestion(n):
    res=[]
    for i in range(len(n)):
        counter=0
        for j in range(i):
            if n[j]>n[i]:
                counter-=abs(n[j]-n[i])
            elif n[j]<n[i]:
                counter+=abs(n[i]-n[j])
        res.append(counter)
    return res
print(ibmQuestion([2,4,3]))
