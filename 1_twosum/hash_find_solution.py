# 哈希查找，用空间换时间
class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:   # 参数冒号后边是类型标注

        hashmap = {}

        for i, num in enumerate(nums):       # enumerate(nums)可以同时得到列表的下标和数字

            need = target - num
            if need in hashmap:
                return [hashmap[need], i]
            hashmap[num] = i

solution = Solution()
result = solution.twoSum([11, 2, 7, 15], 9)
print("idx =",result)