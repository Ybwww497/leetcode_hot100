class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
# 使用双指针法，slow指向下一个非零元素应该放置的位置，fast遍历整个数组
# 经历过交换操作，fast走到了slow前面；而且只要经历过一次交换操作，slow的值就会变成一个位于slow和fast之间的零元素的头部
        for fast in range(len(nums)):
            if nums[fast] != 0:                                        # fast指向的元素不为0时，才会执行操作；如果为0，产生的结果是fast指向下一个元素，而slow不向前，这就是fast可以超过slow的原因
                if slow != fast:
                    nums[slow], nums[fast] = nums[fast], nums[slow]    # 列表元素交换位置
                slow += 1

solution = Solution()
nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print("nums =", nums)