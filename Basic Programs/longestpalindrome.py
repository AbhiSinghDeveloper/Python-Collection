# Longest Palidrome Substring
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
 def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Return if string is empty
        if not s: return s

        res = ""
        for i in range(len(s)):
            j = i + 1
            # While j is less than length of string
            # AND res is *not* longer than substring s[i:]
            while j <= len(s) and len(res) <= len(s[i:]):
                # If substring s[i:j] is a palindrome
                # AND substring is longer than res
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1

        return res
