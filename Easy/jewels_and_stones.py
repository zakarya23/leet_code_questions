# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        same = 0 
        for jewel in range(len(jewels)): 
            for stone in range(len(stones)): 
                if (stones[stone] == jewels[jewel]): 
                    same += 1
        return same