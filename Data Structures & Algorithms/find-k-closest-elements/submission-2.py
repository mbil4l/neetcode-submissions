class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        m, l, r = 0, 0, len(arr) - 1

        while l <= r:

            m = l + (r - l) // 2

            if arr[m] > x:
                r = m - 1
            elif arr[m] < x:
                l = m + 1
            else:
                break
        
        # After binary search, check if l or r are closer to x than m
        idx = m
        min_dist = abs(arr[m] - x)
        for i in [m - 1, m, m + 1]:
            if 0 <= i < len(arr):
                dist = abs(arr[i] - x)
                if dist < min_dist or (dist == min_dist and arr[i] < arr[idx]):
                    min_dist = dist
                    idx = i

        # now 'idx' is the closest/actual number idx.
        res = [arr[idx]]
        l = idx - 1
        r = idx + 1
        while len(res) < k:
            left_val = arr[l] if l >= 0 else float('inf')
            right_val = arr[r] if r < len(arr) else float('inf')
            
            if abs(left_val - x) <= abs(right_val - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        return sorted(res)