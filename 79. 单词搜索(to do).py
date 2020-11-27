class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        queue = list(word)
        n = len(word)

        def search_list(board_, word_ch, line, queue_):
            if (line < 0) | (line >= n):
                return False
            if word_ch in board_[line]:
                queue_.pop(0)
                board_[line].remove(word_ch)
                if len(queue_) == 0:
                    return True
                return search_list(board_, queue_[0], line, queue_)
            else:
                if line > 0:
                    return search_list(board_, word_ch, line - 1, queue_)
                els

        return search_list(board, queue[0], 0, queue)


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

s = Solution()
data = s.exist(board, "ABCCD")
print(data)