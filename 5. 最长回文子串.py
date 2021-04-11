class Solution:
    def check(self, s):
        a = 0
        b = len(s) - 1
        while a < b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        for i in range(1, len(s) + 1)[::-1]:
            for j in range(len(s) - i + 1):
                if self.check(s[j:i + j]):
                    return s[j:i + j]


s = Solution()
print(s.longestPalindrome("xfsxwjqovpvchyjzdqphjsligzljscmzmjzelmbfnqpukbninfbbljouesngmbdyzhqysroeyagglkgorllkrcditzisqhihmithgjcpilkgfdxxqqjpqnoavgkjhojrldsyucfgtzimdbjehrxxqlpaqdddzismsodvternodzxusuehllpujmjjukrilrubbwzdjxbpmvmmwzbrxcxsjsqljjezgyzmsjpucghjxksdfyucpbvwloyhwevzgudhpspgtvsbjqlzmpequxthdonvbmjpeirttllvmtonqmbqxqtdkgichbfzkbhmhotqpkaeshhecshqjvdwgwkegmujwcnmseicesxddrvutxomsgjeylpqiuyezdccarsiprmoqgyifidxhufocfdrbnqczhtztutspaftwctsmynozhakqgvfsvoffyslhoaptkcktopabrxxwrcbyfftleaotwpoqvjjdzxwwqxjnyszjqwjsghkzpvirwnwgsofkjluyxzgboxybzhnmqhkwgltwdjgnemaaadvflrzdqmjufwyuwzoimnvhlxhxjywbopresdrepulsaaexdeddyzeosqfwlnovfpxothrcxhxnumnymofkkuxvclwvuhcelieengfbhvinckrpbjuuewnwvnrvimgmpsfdlcffpdfwmydgzdvluaejwalueygvvojfovuxwhlwojldfpieqqpoqfxhbkcnrtzrnbaagonnawwaqdzamhnvwdtoxlkexihvrqwwimjn"))
