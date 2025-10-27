class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers) - 1
        res = []
        while l<r:
            if numbers[l]+numbers[r]>target:
                r -= 1
            if numbers[l]+numbers[r]<target:
                l+=1
            if numbers[l]+numbers[r]==target:
                break
        res.append(l+1)
        res.append(r+1)
        return res
