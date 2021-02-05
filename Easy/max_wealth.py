class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int: 
        maxTotal = 0 
        for person in accounts: 
            total = 0
            for i in range(len(person)): 
                total += person[i]
            if (total >= maxTotal): 
                maxTotal = total
        return maxTotal