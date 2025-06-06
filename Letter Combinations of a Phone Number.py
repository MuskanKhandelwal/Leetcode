class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitTochar={"2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        def backtrack(i,charstr):
            if len(charstr) == len(digits):
                res.append(charstr)
                return 
            
            for c in digitTochar[digits[i]]:
                backtrack(i+1,charstr+c)

        if digits:
            backtrack(0,"")
        
        return res
