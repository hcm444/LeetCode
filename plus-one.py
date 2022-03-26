class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = int(''.join(str(i) for i in digits))
        res = [int(x) for x in str(sum+1)]
        return res
