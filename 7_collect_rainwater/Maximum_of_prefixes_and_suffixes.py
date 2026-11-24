# 前后缀最大值法相当于是创建了left_max列表和right_max列表，然后对每个位置的雨水量进行计算
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        # 从左向右寻找最高柱子
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        # 从右向左寻找最高柱子
        for i in range(n-2, -1, -1):     # range在这里生成的是一系列的整数，光看range还没有到和列表连结的地步。即这里生成的是从[0, n-2]的一系列数字
            right_max[i] = max(right_max[i+1], height[i])

        # 计算每个位置的雨水量
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water

solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
water = solution.trap(height)
print("water =", water)