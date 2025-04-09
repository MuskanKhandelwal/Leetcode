class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for ele in nums:
            if nums.count(ele)>1:
                return ele
                break
        return None
