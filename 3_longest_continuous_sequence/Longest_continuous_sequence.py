class Solution:
    def longestConsecutive(self, nums:list[int]) -> int:     # nums作为整数列表在这个方法里定义，但是注意：类型标注只是表示一种期望，而不会创建一个具体的列表，在下面result = solution.longestConsecutive(nums)调用方法时，才会传入具体的数据
        num_set = set(nums)    # set()可以实现：1.列表转集合 2.字符串转集合 3.直接创建空集合     用哈希查找时间复杂度是O(1)  创建集合的时间复杂度是O(n)
        longest = 0

        for num in num_set:
            if num -1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current +=1
                    length +=1

                longest = max(longest, length)          # max(a, b)  返回两个数中较大的一个

        return longest

solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
result = solution.longestConsecutive(nums)
print("result =", result)
