      stack=[]
        matching={
         ")":"(",
         "}":"{",
         "]":"["
         }
        for char in s :
          if char in matching : #if it is  closed
             if stack and  stack[-1]==matching[char]:
                stack.pop()
             else:
                return False
          else:
            stack.append(char)          
        return not stack
     