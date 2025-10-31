class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target == nums[m]:
                return m
                break
            if (nums[l]<= nums[m]):
                if target > nums[m] or target < nums[l]:
                    l=m+1
                else:
                    r=m-1
            else:
                if target < nums[m] or target > nums[r]:
                    r=m-1
                else:l=m+1

        return -1
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l<=r:
            mid = (l+r)//2
            if (nums[mid]) == target:
                return mid
            if nums[l]<=nums[mid]:
                if  nums[l] <= target <= nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return - 1
