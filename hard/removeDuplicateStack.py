class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_count={}
        for ch in s:
            if ch in char_count:
                char_count[ch]+=1
            else:
                char_count[ch]=1
        visited=set()
        stack=[]
        for ch in s : 
            char_count[ch]-=1
            if ch in visited:
                continue
            while stack and stack[-1] > ch and char_count[stack[-1]] >0:
               visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
        return ''.join(stack)

        