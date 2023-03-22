class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        answer = []
        for i in range(len(spells)):
            left = 0
            right = len(potions) -1
            while left <= right:
                mid = (left + right) //2
                if potions[mid] * spells[i] >= success:
                # if potions[mid] >= (success + spells[i] - 1) // spells[i]:
                    right = mid -1
                else:
                    left = mid +1
            count = len(potions) - left
            answer.append(count)
        return answer
                