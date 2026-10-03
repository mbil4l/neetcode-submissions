from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.datastruct = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.datastruct[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if not self.datastruct[key]: return res

        l, r = 0, len(self.datastruct[key]) - 1
        
        while l <= r:
            
            m = l + (r - l) // 2

            if self.datastruct[key][m][0] == timestamp: 
                return self.datastruct[key][m][1]
            
            if timestamp > self.datastruct[key][m][0]:  
                res = self.datastruct[key][m][1]
                l = m + 1
            else: 
                r = m - 1
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)