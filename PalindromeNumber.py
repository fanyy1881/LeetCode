class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > 2147483647 or x < 0:
            return False   
        reverse_num = 0
        x_tmp = x
        while x_tmp:
            x_tmp, m = divmod(x_tmp, 10)
            reverse_num = reverse_num * 10 + m
        return x == reverse_num

if __name__ == '__main__':
    print(Solution().isPalindrome(-1))
    print(Solution().isPalindrome(0))
    print(Solution().isPalindrome(1))