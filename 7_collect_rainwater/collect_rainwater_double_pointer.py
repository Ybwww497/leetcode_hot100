class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1 

        left_max = 0
        right_max = 0
        water = 0

        while left <= right:
            # 更新两侧最高柱子
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water

solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
water = solution.trap(height)
print("water =", water)