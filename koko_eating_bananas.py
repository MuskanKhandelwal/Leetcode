import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res= r
        while l<=r:
            hours=0
            m=(l+r)//2
            for i in piles:
                hours+= math.ceil(i/m)
            if hours<=h:
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res
