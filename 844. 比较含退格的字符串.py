class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 栈方法
        ls_S = []
        ls_T = []
        for i in list(S):
            if i == "#" and ls_S:
                ls_S.pop(-1)
            else:
                ls_S.append(i)
        for i in list(T):
            if i == "#" and ls_T:
                ls_T.pop(-1)
            else:
                ls_T.append(i)
        if ls_S == ls_T:
            return True
        else:
            return False


    # 算