class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_array = sorted(zip(position, speed), reverse = True)
        fleets = 0
        last_time = 0
        for pos, speed in new_array:
            time = (target - pos)/speed
            if time > last_time:
                last_time = time 
                fleets += 1
        return fleets