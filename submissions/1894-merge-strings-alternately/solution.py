class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = []
        i, j = 0, 0

        while i < len(word1) and j <len(word2):
            mergedString.append(word1[i])
            mergedString.append(word2[j])
            i+=1
            j+=1
        if i<len(word1):
            mergedString.append(word1[i:])
        if j<len(word2):
            mergedString.append(word2[j:])
        return ''.join(mergedString)
