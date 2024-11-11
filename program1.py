class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map={')':'(','}':'{',']':'['}
        st=[]
        for c in s :
            if c in bracket_map:
                # if not st:
                #     return False
                # top_ele=st.pop() if st else "#"
                # if bracket_map[c]!=top_ele:
                #     return False
                if not st or st[-1]!=bracket_map[c]:
                    return False
                st.pop()
            else:
                st.append(c)
        return not st

sol=Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([{}])"))
print(sol.isValid("{[()]}"))
print(sol.isValid("{[(])}"))
print(sol.isValid("{{[[(())]]}}"))        
print(sol.isValid(""))             
print(sol.isValid("((((()))))"))   
print(sol.isValid("(()"))         
print(sol.isValid("())"))         
print(sol.isValid("((()))"))      
print(sol.isValid("([)]"))        
print(sol.isValid("{[()]}"))      
print(sol.isValid("{[(])}"))      


    



  

