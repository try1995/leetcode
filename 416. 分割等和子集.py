class Solution:
    def canPartition(self, nums: list) -> bool:
        if len(nums) < 2:
            return False
        nums.sort(reverse=True)
        len_nums = len(nums) // 2
        print(nums)

        # 每次取出n个来比较
        def helper(n):
            if n > len_nums:
                return False
            ls_a = []
            ls_b = []
            while n:
                n -= 1
                ls_a.append(nums.pop(0))
                sum_a = sum(ls_a)
                sum_b = sum(nums)
                if sum_a == sum_b:
                    return True
                elif sum_b > sum_a:
                    return False
                else:
                    return
