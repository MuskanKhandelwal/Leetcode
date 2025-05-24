class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        total = 0 
        def dfs(i,subset,total):
            if ((sum(subset))==target):
                res.append(subset.copy())
                return
            if (sum(subset)>target or i>=len(candidates)):
                return 

            subset.append(candidates[i])
            dfs(i+1,subset,total+sum(subset))
            subset.pop()
            dfs(i+1,subset,total)
            
        dfs(0,subset,total)
        sorted_subsets = [tuple(sorted(subset)) for subset in res]

        unique_subsets = list(set(sorted_subsets))
        return [list(subset) for subset in unique_subsets]
       
