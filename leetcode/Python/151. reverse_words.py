class Solution:
    def reverseWords(self, s: str) -> str:
        str_lst = s.split()
        reverse_str = " ".join(str_lst[::-1])
        return reverse_str
