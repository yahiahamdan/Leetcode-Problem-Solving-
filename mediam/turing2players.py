"""
i have numseq of players [3,6,2,3,5]
ist round firstplayer 3 the remianing 6,2,3,5
2nd round  even 6  reverse the others 5,3,2
"""

def twoplayers(numseq):
    evenPlayer=0
    oddPlayer=0
    turn=0
    while numseq:
        currentNumber=numseq.pop()
        if turn==0:
          evenPlayer+=currentNumber
        else:
          oddPlayer+=currentNumber
        if currentNumber%2==0:
            numseq.reverse()
        turn=1-turn 
        
    return evenPlayer-oddPlayer


print("this is return method" ,twoplayers([3,6,2,3,5])) 
