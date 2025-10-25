class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0] * len(nums)
        for i in range(len(nums)):
            total_prod=1
            for j in range(len(nums)):
                if i==j:
                    continue
                
                total_prod=total_prod*nums[j]
            res[i] = total_prod
        

        print(res)
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(1)
        p = 1
        for i in range(len(nums)-1):
            p=p*nums[i]
            prefix.append(p)
        suffix = [0] * len(nums)
        suffix[len(nums)-1] = 1 
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        return res
        
