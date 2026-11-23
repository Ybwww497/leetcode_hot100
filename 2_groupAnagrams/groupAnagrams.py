# 字母异位词：哈希表分组/按特征分类，把具有相同特征的东西映射到同一个key，然后用哈希表分组
class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        hashmap = {}

        for s in strs:
            key = ''.join(sorted(s))    # 以s = "eat" 举例，sorted(s)会把s排序成一个列表['a','e','t'](注意不是字符串)，''.join(['a', 'e', 't'])表示把列表里的字符用''连接起来，因为''是空字符串，所以得到"aet",所以这个语句最终得到结果"aet"，需要注意，python字典的key不能是列表，所以需要转成字符串
            if key not in hashmap:
                hashmap[key] = []       # 字典dict[key] = 值value
            hashmap[key].append(s)      

        return list(hashmap.values())   # hashmap.values()是["eat", "tea", "ate"],["tan", "nat"],["bat"]    因为题目只要求返回分组结果，所以需要取出所有的value,并转换为列表

solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagrams(strs)
print("result =", result)