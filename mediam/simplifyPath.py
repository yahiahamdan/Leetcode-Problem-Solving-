#solv ed in this leetcode but needed upgradation
def simplifyPath(path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        words=path.split('/')
        print(words)
        for ch in words : 
            if ch == '.' or ch== '':
              continue
            if ch=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "/"+('/'.join(stack))
print(simplifyPath("/a//efwe/"))

def simplifyPath(path2):
    stack=[]
    cur=""
    for c in path2:
        if c=="/":
            if cur=="..":
                if stack:
                    stack.pop()
            elif cur!="" and cur!=".":
                stack.append(cur)
            cur=""
        else:
           cur+=c
                
    return "/"+"/".join(stack) 
      

