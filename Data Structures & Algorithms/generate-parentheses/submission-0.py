class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #stop when number of brackets exceeds 2*n
        #on each level we can make too choices
        #on each choice we can check if it is a valid parentheses

        res = []

        def isValid(choice):
            stack = []
            for val in choice:
                if val == '(':
                    stack.append(val)
                    continue

                if val == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False

            return not stack

        def dfs(choice):
            if len(choice) == 2*n:
                if isValid(choice):
                    res.append("".join(choice))
                return

            choice.append("(")
            dfs(choice)
            choice.pop()

            choice.append(")")
            dfs(choice)
            choice.pop()

        dfs(["("])
        return res    



        