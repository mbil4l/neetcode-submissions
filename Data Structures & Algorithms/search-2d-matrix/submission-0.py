class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:

        rows, cols = len(grid), len(grid[0])
        top, btm = 0, rows - 1

        while top <= btm:

            mid = (btm - top) // 2 + top

            if target < grid[mid][0]: btm = mid - 1

            elif target > grid[mid][-1]: top = mid + 1
            
            else: 

                l, r = 0, len(grid[mid]) - 1

                while l <= r:

                    m = l + (r-l)//2

                    if grid[mid][m] > target: r = m - 1

                    elif grid[mid][m] < target: l = m + 1

                    else: return True
                
                return False
                
        
        return False


         