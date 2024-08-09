class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        number = set(nums)
        count = 0

        for num in nums:
            if (num + diff in number) and (num + 2 * diff in number):
                count += 1
        return count
