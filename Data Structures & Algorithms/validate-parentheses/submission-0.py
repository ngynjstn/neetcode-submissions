class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #needs a stack because it will use the push and pop operations for LAST in fFIRST OUT
        closeToOpen = { ")": "(", "]" : "[", "}" : "{"} # this is the hash map dictionary for for the stack to understand if it gets closde or not

        #every key in this dictionary is always a closing bracket
        #so if c is in closetoopen, we want to make sure the stack is not empty and the value at the top of the stack is macthing the pop out/opening parentheses

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: #if this match is good
                    stack.pop() #removes top most 
                else:
                    return False
            else: #if we get open parenthese just append to stack and keep going
                stack.append(c)

        return True if not stack else False





        
        