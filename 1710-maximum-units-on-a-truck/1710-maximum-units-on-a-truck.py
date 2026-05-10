class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_units = sorted(boxTypes, key=lambda x: x[1] , reverse=True)
        
        total = 0
        size = 0
        for unit in sorted_units:
            if unit[0] + size <= truckSize:
                total += unit[0]* unit[1]
                size += unit[0]
            else:
                free_space = truckSize - size
                total += free_space * unit[1]
                return total
        return total
            