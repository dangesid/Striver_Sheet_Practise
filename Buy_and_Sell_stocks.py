# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
import sys

minPrice = sys.float_info.max
maxPro = 0
arr = [7,1,5,3,6,4]

for i in range(len(arr)):
    minPrice = min(minPrice,arr[i])
    maxPro = max(maxPro,arr[i]-minPrice)
print(maxPro)


