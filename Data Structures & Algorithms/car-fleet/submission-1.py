class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Logic
        # Zip position and speed together into a 2d array
        # Dist = target - position 
        # time to arrival = dist // speed 
        # monotonic decreasing stack
        # if not stack or time <= stack[-1]
        # stack.append(dist)
        # length of stack is fleet count
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        print(cars)
        for p, s in cars:
            time = (target - p) / s 
            if not stack or time > stack[-1]:
                stack.append(time)
        

        return len(stack)


        