class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1) 
            subset.pop()
            dfs(i+1)
        dfs(0)
        sorted_subsets = [tuple(sorted(subset)) for subset in res]

        unique_subsets = list(set(sorted_subsets))
        return [list(subset) for subset in unique_subsets]
       
