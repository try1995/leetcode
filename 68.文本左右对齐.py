class Solution(object):
    def findx(self, str, index):
        while index:
            if str[index] != '|':
                index -= 1
            else:
                return index

    def addSpace(self, str, lens):
        iCount = str.count("|")
        if iCount == 0:
            return str + " " * (lens - len(str))
        else:
            diff_x = (lens - len(str) + iCount) // iCount
            diff_y = (lens - len(str) + iCount) % iCount
            str_ls = str.split("|")
            str = ""
            while True:
                str += str_ls.pop(0)
                if len(str_ls) == 0:
                    break
                str += diff_x * " "
                if diff_y:
                    str += " "
                    diff_y -= 1
        return str

    def addSpaceLast(self, str, lens):
        iCount = str.count("|")
        if iCount == 0:
            return str + " " * (lens - len(str))
        else:
            str = str.replace("|", " ") + " " * (lens - len(str))
        return str

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = []
        strWords = '|'.join(words)
        while len(strWords) > maxWidth:
            index = self.findx(strWords, maxWidth)
            ret.append(self.addSpace(strWords[:index], maxWidth))
            strWords = strWords[index + 1:]
        ret.append(self.addSpaceLast(strWords, maxWidth))
        return ret


Words = ["What","must","be","acknowledgment","shall","be"]
MaxWidth = 16
s = Solution()
Ret = s.fullJustify(Words, MaxWidth)
print(Ret)