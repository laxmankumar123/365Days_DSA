class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def function1(currunt, opened, closed, n):
            if len(currunt) == 2 * n:
                if opened == closed:
                    res.append(currunt)
                return

            if opened < n:
                function1(currunt + "(", opened + 1, closed, n)
            if opened > closed:
                function1(currunt + ")", opened, closed + 1, n)

        function1("", 0, 0, n)
        return res


           
#22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
        










        