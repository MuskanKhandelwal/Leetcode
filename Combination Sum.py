class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        sums=0
        def dfs(i,subset,sums):
            if sums>target or i>=len(nums):
                return
            if sums==target:
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i,subset,sums+nums[i])
            subset.pop()
            dfs(i+1,subset,sums)

        dfs(0,subset,sums)
        return res
