class Solution(object):
    def findSubstring(self, s, words):
          word_len=len(words[0])
          noOfWords=len(words)
          result=[]
          totalLength=noOfWords*word_len
          wordsdict={}
          for word in words:
            if word in wordsdict :
                wordsdict[word]+=1
            else:
                wordsdict[word]=1
       
          for i in range(word_len):
             left=i
             right=i
             checkdict={}
             while right+word_len <= len(s):
               right_word=s[right:right+word_len]
               right += word_len
               if right_word in wordsdict:
                  if right_word in checkdict:
                     checkdict[right_word]+=1
                  else:
                      checkdict[right_word]=1
                  while checkdict[right_word]>wordsdict[right_word]:
                       left_word=s[left:left+word_len]
                       checkdict[left_word]-=1
                       left+=word_len
                  if right-left==totalLength :
                     result.append(left)
               else:
                  checkdict.clear()
                  left=right
          return result
  




                