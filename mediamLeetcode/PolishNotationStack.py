
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        result=0
        for ch in tokens:
            if ch in {'+', '-', '*', '/'}:
               first=stack.pop()
               second=stack.pop()
            if ch=='+':
              stack.append(first+second)
            elif ch=='*':
                stack.append(first*second)
            elif ch=='-':
                stack.append(second-first)
            elif ch=='/': 
                 stack.append(int(float(second) / float(first)))
            else:
                stack.append(int(ch))
            
        return stack[-1]

               
              