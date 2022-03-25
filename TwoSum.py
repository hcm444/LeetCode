class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counter = 0
        for i in range(0,len(nums)):
            #search for one index
            for j in range(0,len(nums)):
                #search for second
                if (i !=j):
                    #can't be equal or you might get[0,0]
                    if nums[i] + nums[j] == target:
                        #x + y = target
                        return [int(i),int(j)]
                        #return
                        counter +=1
