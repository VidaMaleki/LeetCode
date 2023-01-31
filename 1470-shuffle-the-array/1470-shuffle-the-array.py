class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list = []
        n_list = nums[:n]
        m_list = nums[n:]
        print(m_list)
        for i, j in zip(n_list, m_list):
            new_list.append(i)
            new_list.append(j)
        return new_list