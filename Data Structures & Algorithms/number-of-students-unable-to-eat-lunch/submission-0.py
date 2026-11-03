from collections import Counter
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        stuFreq = Counter(students)

        i = 0
        while i < len(sandwiches):
            sand = sandwiches[i]
            if sand in stuFreq:
                stuFreq[sand] -= 1
                if not stuFreq[sand]: 
                    del stuFreq[sand] 
                i += 1
            else:
                break
        return sum(stuFreq.values())    
            
