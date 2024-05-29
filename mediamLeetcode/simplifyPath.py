#solv ed in this leetcode but needed upgradation
def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        words=path.split('/')
        for ch in words : 
            if ch == '.' or ch== '':
              continue
            if ch=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "/"+('/'.join(stack))
print(simplifyPath("/a/"))

