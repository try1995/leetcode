"""
x & (−x) 可以获得 x的二进制表示中的最低位的 1 的位置；

x & (x−1) 可以将 x 的二进制表示中的最低位的 1 置成 0。
"""


class Solution:
    def count(self, x):
        num = 0
        while x:
            x = x & (x - 1)
            num += 1
        return num

    def sortByBits(self, arr):
        dict_arr = {}
        ls_arr = []
        for i in arr:
            index = self.count(i)
            dict_arr.setdefault(index, [])
            dict_arr[index].append(i)
        data = sorted(dict_arr.items(), key=lambda x: x[0])
        for _, i in data:
            i = sorted(i)
            ls_arr.extend(i)
        return ls_arr


s = Solution()
data = s.sortByBits(arr=[8, 7, 6, 5, 4, 3, 2, 1])
print(data)
