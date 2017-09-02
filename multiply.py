class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans=""
        multiplied,j=int(num1),len(num2)-1
        carry=0
        product,base=0,1
        while j>=0:
            product=product+int(num2[j])*base*multiplied
            base=base*10
            j=j-1
        return str(product)
so=Solution()
print so.multiply("11","19")
