class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, *nums):
        sum = 0
        for value in nums:
            sum+=value
        self.result += sum
        return self
    def subtract(self, *nums):
        sum = 0
        for value in nums:
            sum+=value
        self.result -= sum
        return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

