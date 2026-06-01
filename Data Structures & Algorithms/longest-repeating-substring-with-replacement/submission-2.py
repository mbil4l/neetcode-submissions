class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r, res = 0, 0, 0
        cnt = defaultdict(int)

        while r < len(s):

            cnt[s[r]] += 1
            windowSize = r - l + 1

            if windowSize - max(cnt.values()) > k:
                cnt[s[l]] -= 1
                l += 1
            else:
                res = max(res, windowSize)
            
            r += 1
        
        return res