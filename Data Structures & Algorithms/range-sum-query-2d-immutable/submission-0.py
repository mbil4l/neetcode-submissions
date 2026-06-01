class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # creating grid
        self.grid = []
        for _ in range(len(matrix) + 1):
            self.grid.append([0] * (len(matrix[0]) + 1))
        # populating/calculating
        for r in range(1, len(self.grid)):
            total = 0
            for c in range(1, len(self.grid[0])):
                total = matrix[r-1][c-1] + self.grid[r][c-1] + self.grid[r-1][c] - self.grid[r-1][c-1]
                self.grid[r][c] = total
                print(matrix[r-1][c-1], self.grid[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        return self.grid[r2][c2] - self.grid[r1-1][c2] - self.grid[r2][c1-1] + self.grid[r1-1][c1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)