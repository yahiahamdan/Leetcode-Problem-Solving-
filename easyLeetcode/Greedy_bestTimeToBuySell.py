"""
first i solved this problem brute force solution 0(n)

"""
def maxProfit(prices):
        MaxValue=-342133
        for i in range(len(prices)):
           for j in range(i+1,len(prices)):
               MaxValue=max(MaxValue,prices[j]-prices[i])
        return MaxValue if MaxValue >0 else 0

def maxProfit(prices):
        minPrice=float('inf')
        maxProfit=0
        for price in prices:
          if price < minPrice:
             minPrice=price
          elif price-minPrice >maxProfit:
              maxProfit=price-minPrice
        return maxProfit