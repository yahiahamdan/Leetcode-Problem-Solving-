""""
text jsutiifcation problem lets see what will give me 
text probelm  is to justify the text in the given width 
"""
def text(words,k):
    lenofline=0
    current_line=[]
    lines=[]
    for word in words:
        if len(word)+lenofline+1 <= k:
            current_line.append(word)
            lenofline+=len(word)+1
        else:
            lines.append(current_line)
            current_line=[word]
            lenofline=len(word)
    lines.append(current_line)
    return lines
print(text(["this","is","the","best","people","a7laaayam"],16))
           
     


 
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # 3ayz a2smha keda keda ely hya tkoon maxwidth 
        line=[] 
        result=[]
        wordslength=0
        i=0
        while(i<len(words)):
            if wordslength+len(line)+len(words[i])>maxWidth:
                spaces=maxWidth-wordslength
                wordPerSpace= spaces //max(1,len(line)-1)
                remainderSpace= spaces % max((len(line)-1),1)
                
                for j in range(max(1,len(line)-1)):
                    line[j]+=" "*wordPerSpace
                    if remainderSpace >0:
                        line[j]+=" "
                        remainderSpace-=1
                result.append(''.join(line))
                line=[]
                wordslength=0 
            line.append(words[i])
            wordslength+=len(words[i])
            i+=1   
        if line:
          last_line = ' '.join(line)
          trial_space=maxWidth-len(last_line)
          last_line+=" "*trial_space
          result.append(last_line) 
        return result





    
