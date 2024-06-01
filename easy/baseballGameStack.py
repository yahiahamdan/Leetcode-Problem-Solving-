def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        for ch in operations:
               
            if stack and ch=='C':
                stack.pop()
            elif stack and ch=='D':
                newscore= stack[-1]*2
                stack.append(newscore)
            elif len(stack)>=2 and ch=='+':
              stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(ch))
        total = sum(stack)
        return total
        