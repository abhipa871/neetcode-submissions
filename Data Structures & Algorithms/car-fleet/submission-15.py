class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in sorted_pairs:
            time_remaining = (target - pos) / spd

            if not stack or time_remaining > stack[-1]:
                stack.append(time_remaining)

        return len(stack)
































