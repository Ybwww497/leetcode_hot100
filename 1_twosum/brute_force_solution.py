class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):             # 左闭右开
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()
result = solution.twoSum([11, 2, 7, 15], 9)
print(result)