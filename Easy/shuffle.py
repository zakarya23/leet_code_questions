class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = 0 
        y = n 
        out = []
        for i in range(n): 
            out.append(nums[x]) 
            out.append(nums[y])
            x += 1
            y += 1
        return out