def range(start,end):
    string="123456789"
    startLen=len(str(start))
    endLen=len(str(end))
    result=set()
    for i in range(startLen,endLen+1):
       for j in range(len(string) - i+1):
           num_str=string[j:j+i]
           num=int(num_str)
           if start<num<end:
               result.add(num_str)
        
    return result
print(range(50,150))
