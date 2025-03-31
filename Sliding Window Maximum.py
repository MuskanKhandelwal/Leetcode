class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range (0,len(nums)-k+1):
            max_=nums[i]
            for j in range (i,i+k):
                max_ = max(max_, nums[j])
            res.append(max_)
        return res
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q=deque() #appending indices not values 
        l=r=0

        while r<len(nums):
            # pop smaller values from queue
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            if l>q[0]:
                q.popleft()
            # remove left val from window
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
