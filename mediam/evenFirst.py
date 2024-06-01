"""
ana 3ndy array of numbers [1,2,3,4,5,6,7,8,9,10]
ana 3ayz [2,4,6,8,10] ykonon fe awel el array w [1,3,5,7,9] ykonon fe akher el array

"""
def evenfirst(numlist):

 numlist.sort(key=lambda x: x%2 )
 return numlist

print(evenfirst([1,2,3,4,5,6,7,8,9,10]))
#this will take o(nlogn) time complixity we space 1  bs lw ana 3ayz a3mlha fe o(n) what i will do 
def evenFirst1(numlist):
  left =0
  right=len(numlist)-1
  while left<right:
       if numlist[left]%2==0 :
          left+=1
       if  numlist[right]%2==1:
          right-=1  
       if numlist[left]%2==1 and numlist[right]%2==0:
           numlist[left],numlist[right]=numlist[right],numlist[left]
           left+=1
           right-=1 
  return numlist
print(evenFirst1([1,2,3,4,5,6,7,8,9,10]))