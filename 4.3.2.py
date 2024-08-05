def multip(*nums):
    result = 1
    for i in nums:
        result *= i
    return result

print(multip(3, 2, 8))

def adder(*nums):
   sum_ = 0
   for n in nums:
       sum_ += n
  
   return sum_

print(adder(8, 3, 7))