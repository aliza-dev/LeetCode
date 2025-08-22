class Solution(object):
    def plusOne(self, digits):
      digits = str(digits)
      digits = digits.replace(" ","").replace(",","").replace("[","").replace("]","")
      digits = int(digits)
      digits = digits + 1
      digits = str(digits)
      digits = [int(digits) for digits in digits]
      return digits