"""
i have  oranage3 red5 green1 blue2 
green blue oraange red 
"""
def strchange(sent):
    sent=sent.rstrip( )
    stringsplit=sent.rsplit(' ')
    orderdict={}
    res=""
    for i in range(len(stringsplit)):
        word=stringsplit[i]
        orderdict[word[-1]]=word[:-1]
        print(orderdict)
    #now i want to make order consider to the key 
    sortedkey=sorted(orderdict)
    print(sortedkey)
    for j in range(len(sortedkey)):
      res+= orderdict[sortedkey[j]]+" "
    return res.rstrip()   
print(strchange("oranage3 red5 green1 blue2"))
