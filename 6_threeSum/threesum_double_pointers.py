class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):

            # 第一个数大于0，不可能凑出0
            if nums[i] > 0:
                break

            # 第一个数去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # 第二个数去重
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # 第三个数去重
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res

solution = Solution()
nums = [-1, 0, 1, 2, -1, 4]
result = solution.threeSum(nums)
print(result)