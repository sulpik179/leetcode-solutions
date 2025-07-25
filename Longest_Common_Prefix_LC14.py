class Solution:
    def longestCommonPrefix(strs):
        prefix = strs[0]         # Берём первую строку как префикс
        for s in strs[1:]:       # Для каждой следующей строки
            while not s.startswith(prefix):   # Пока строка не начинается с префикса
                prefix = prefix[:-1]           # Укорачиваем префикс
                if not prefix:                 # Если префикс закончился
                    return ""                  # Выходим сразу
        return prefix

print(Solution.longestCommonPrefix(["flower","flow","flight"]))