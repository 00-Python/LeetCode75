class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for i in range(min(len(word1), len(word2))):
            result += word1[i] + word2[i]
        result += word1[min(len(word1), len(word2)):] + word2[min(len(word1), len(word2)):]
        return result

class Solution_one_liner:
    def mergeAlternately(self, word1: str, word2: str) -> str:
         return ''.join([word1[i] + word2[i] for i in range(min(len(word1), len(word2)))] + [word1[min(len(word1), len(word2)):], word2[min(len(word1), len(word2)):]])
