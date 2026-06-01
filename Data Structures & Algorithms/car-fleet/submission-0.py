class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        def calcTime(pos, speed):
            return (target - pos) / speed

        data = list(zip(position, speed))

        data.sort(reverse=True)

        prevTime = calcTime(data[0][0], data[0][1])

        resFleets = 1

        for i in range(1, len(data)):

            curTime = calcTime(data[i][0], data[i][1])

            if prevTime >= curTime:
                continue
            else:
                resFleets += 1
            
            prevTime = curTime

        return resFleets 





        


        
        