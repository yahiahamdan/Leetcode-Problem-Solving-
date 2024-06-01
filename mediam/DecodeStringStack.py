def decodeString(s: str) :
        stack=[]
        for ch in s:
            if ch.isdigit():
                if stack and  stack[-1].isdigit():
                    stack[-1]=stack[-1]+ch
                else:
                    stack.append(ch)
            elif ch =='[':
                stack.append(ch)
            elif ch==']':
              answer=""
              while stack and stack[-1] !='[':
                answer=stack.pop()+answer
              stack.pop() # remove the [
              num=""
              while stack and stack[-1].isdigit():
                num=stack.pop()+num   #if no is 15   
              if num:
                num=int(num)
              else:
                num=1
              stack.append(answer * num)
            else:
                stack.append(ch)
        return ''.join(stack)

def decodeString2(s):
    stack=[]
    for ch in s :
        if ch !=']':
            stack.append(ch)
        else:
            temp=""
            while stack and stack[-1]!='temp':
                temp=stack.pop()+temp
            stack.pop()
            num=""
            while stack and stack[-1].isdigit():
                num=stack.pop()+num
            stack.append(temp*int(num))
    return ''.join(stack)

