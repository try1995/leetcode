class Solution:
    def matrixScore(self, A):
        if len(A) == 1:
            return int("1"*len(A[0]),2)
        for index, a in enumerate(A):
            if a[0] == 0:
                A[index] = [abs(i-1) for i in a]
        for j in range(len(A[0])):
            count =  0
            for i in range(len(A)):
                if A[i][j] == 0:
                    count += 1
                    if count >= len(A) // 2 + 1:
                        for k in range(len(A)):
                            A[k][j] = abs(A[k][j] - 1)
                        break
        ls = []
        for item in A:
            ls.append(int("".join([str(i) for i in item]),2))
        return sum(ls)


s = Solution()
data = s.matrixScore([[0,0,0,0]])
print(data)