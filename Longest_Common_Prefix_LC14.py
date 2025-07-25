class Solution:
    def longestCommonPrefix(self, words):
        prefix = words[0]
        if not words:
            return ""
        for word in words[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
