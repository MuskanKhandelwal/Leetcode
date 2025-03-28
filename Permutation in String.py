class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s2) < k:
            return False
        s1_count = Counter(s1)  
        window_count = Counter()
        for i in range(k):
            window_count[s2[i]] += 1

        if window_count == s1_count:
            return True
        for i in range(k, len(s2)):
            window_count[s2[i]] += 1
            print(window_count)
            window_count[s2[i - k]] -= 1
            print(window_count)
            if window_count[s2[i - k]] == 0:
                del window_count[s2[i - k]]
            if window_count == s1_count:
                return True
        
        return False
        
