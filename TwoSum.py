class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counter = 0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (i !=j):
                    if nums[i] + nums[j] == target:
                        return [int(i),int(j)]
                        counter +=1
