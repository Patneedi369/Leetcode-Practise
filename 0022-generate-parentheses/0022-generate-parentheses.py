class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_count: int, close_count: int, current_str: str):
            # Base case: string length is 2 * n (valid combination complete)
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            # Add an opening parenthesis if we haven't reached 'n' opening brackets
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            # Add a closing parenthesis if it won't exceed open brackets
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")

        backtrack(0, 0, "")
        return res