class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indexedNums = [(num, i) for i, num in enumerate(nums)]
        sortedNums = sorted(indexedNums)

        result = [0] * len(nums)

        result = [0] * len(nums)
        smallerCount = {}

        numSmaller = 0

        for i in range(len(sortedNums)):
            if i>0 and sortedNums[i][0] != sortedNums[i-1][0]:
                numSmaller = i
            smallerCount[sortedNums[i][0]] = numSmaller

        for num, index in indexedNums:
            result[index] = smallerCount[num]

        return result
