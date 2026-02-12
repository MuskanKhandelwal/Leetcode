#Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) ==k:
                    return res

#This is the bucket sort solution with O(n) time complexity for it 
'''first we need to create the freq list whose indices acts as freq and the sublist will have elements with that freq
[[],[],[]..len(n)+1]. Now we will have a hashmap with number and the freq of it. We will use this to create freq list and then we traverse the freq in reverse. and append the res.
Things tricky for me after even knowing the solution. The count.get syntax, i did a mistake in reversing freq in reverse. an also i did append[] instead of append(). Fixixng minute blunders to become unbeatable.
'''
'''
Also the other solutions are working with sorting and also using heapify most top k problems are ususally solved using heaps
'''
