class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        """
        find substring for each arr[i]
        check if substring[i] is not in arr[i]
        find shortest substring if not ""
        return answer
        """
        
        def is_unique(sub, arr, i):
            for j in range(len(arr)):
                if  j != i and sub in arr[j]:
                    return False
            return True

        def find_unique_sub(sub, arr, i):
            for length in range(1, len(sub)+1):
                uniques = []
                for start in range(len(sub) - length + 1):
                    s= sub[start: start + length]
                    if is_unique(s, arr, i):
                        uniques.append(s)
                if uniques:
                    return min(uniques)
            return ""

        answer = []
        for i in range(len(arr)):
            answer.append(find_unique_sub(arr[i], arr, i))

        return answer

