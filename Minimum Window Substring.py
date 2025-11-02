class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT, window={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        have, need=0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c=s[r]
            window[c] = 1+window.get(c,0)
            if c in countT and window[c]==countT[c]:
                have+=1
            while have ==need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        target = {}
        window = {}
        res,resLen = [-1,-1], float("infinity")
        for k in t:
            target[k] = 1+target.get(k,0)
        need,have = len(target),0
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in target and target[s[r]] == window[s[r]]:
                have+=1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""


        
