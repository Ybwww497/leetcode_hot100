class Solution:
    def maxArea(self, height: list[int]) -> int:
          left = 0
          right = len(height) - 1
          max_area = 0
          while left < right:                      # 移动高度较小一边指针的原因在于：低指针所对应的高度小于高指针对应的高度，同样都是宽度缩减的情况下，移动较高的一方，面积一定不会增长；移动较低的一方，面积有可能增大；为了追求这个可能，我们朝着这个方向去努力，并保存了当前面积的最大值，这样即使出现先减小再增大的情况，仍可以与最大值记录进行比较，保证得到最大面积
               width = right - left
               h = min(height[left], height[right])
               area = width * h
               max_area = max(max_area, area)
               if height[left] < height[right]:
                    left +=1
               else:
                    right -=1
          return max_area

solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area = solution.maxArea(height)    
print("max_area =", max_area)