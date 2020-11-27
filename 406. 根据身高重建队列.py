class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
            首先要记得一点，高的人不会受低的人影响，所以优先处理高的人，排序完后，
            按从高到低和优先级处理，先处理高的并且序号小的，序号便是插入的位置
        '''

        # 身高从高到底排，位置从低往高排
        people = sorted(people, key=lambda x:(-x[0],x[1]))
        res = []
        for i in people:
            res.insert(i[1],i)
        return res


s = Solution()
data = s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
print(data)
