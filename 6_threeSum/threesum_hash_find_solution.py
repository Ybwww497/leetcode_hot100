class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()               # 这里使用集合而非列表，集合的底层是哈希表，查找时效率要大于列表

        for i in range(len(nums)):

            # 第一个数大于0，不可能凑出0
            if nums[i] > 0:
                break        

            # 第一个去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            seen = set()       # 这里使用集合而非列表，集合的底层是哈希表，查找时效率要大于列表

            for j in range(i+1, len(nums)):
                # 计算需要寻找的第三个数
                target = -nums[i] - nums[j]

                if target in seen:
                    triplet = (nums[i], target, nums[j])

                    # 防止结果重复
                    if triplet not in res:
                        res.add(triplet)

                # 将当前数字加入哈希集合
                seen.add(nums[j])

        return [list(triplet) for triplet in res]

nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))