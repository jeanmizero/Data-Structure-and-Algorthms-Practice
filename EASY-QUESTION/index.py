#  121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution:
    def maxProfit(self,prices):
      left = 0 #Buy
      right = 1 #Sell
      max_profit = 0
      while right < len(prices):
          currentProfit = prices[right] - prices[left] #our current Profit
          if prices[left] < prices[right]:
              max_profit =max(currentProfit,max_profit)
          else:
              left = right
          right += 1
      return max_profit
    
    
# QUESTION 1
# Clock hands
# Write a function that returns the acute angle between two clock hands, with two integers for the number of hours and number of minutes.
# E.g. For 3:00, the acute angle would be 90°. For 6:00, it would be 180°.

# Python program to find angle  
# between hour and minute hands 
# Function to Calculate angle b/w  
# hour hand and minute hand  
def calcAngle(h,m):  
        # validate the input 
        if (h < 0 or m < 0 or h > 12 or m > 60): 
            print('Wrong input') 
    
        if (h == 12): 
            h = 0
        if (m == 60): 
            m = 0
        # Calculate the angles moved by  
        # hour and minute hands with  
        # reference to 12:00 
        hour_angle = 0.5 * (h * 60 + m) 
        minute_angle = 6 * m 
        # Find the difference between two angles 
        angle = abs(hour_angle - minute_angle) 
        # Return the smaller angle of two  
        # possible angles 
        angle = min(360 - angle, angle) 
        return angle 
# Driver program   
h = 6
m = 60
print('Angle ', calcAngle(h,m)) 

# This code is contributed by Danish Raza 



# QUESTION 2

# Is Scrambled Palindrome
# Write a function that, given a string of letters, returns true or false for whether the letters in the string could be arranged to form a palindrome.
# E.g. For “torro”, the answer is True, because the letters can be rearranged to spell “rotor”.

def canFormPalindrome(strr):
    # Create a listt
    listt = []

    # For each character in input strings,
    # remove character if listt contains
    # else add character to listt
    for i in range(len(strr)):
        if (strr[i] in listt):
            listt.remove(strr[i])
        else:
            listt.append(strr[i])
    # if character length is even
    # list is expected to be empty
    # or if character length is odd
    # listt size is expected to be 1
    if (len(strr) % 2 == 0 and len(listt) == 0 or
        (len(strr) % 2 == 1 and len(listt) == 1)):
        return True
    else:
        return False
# Driver code
if (canFormPalindrome("torro")):
    print("Yes")
else:
    print("No")

# if (canFormPalindrome("rotor")):
#     print("Yes")
# else:
#     print("No")
