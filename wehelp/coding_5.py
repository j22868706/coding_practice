'''
5. 找到最大公因數
輸入兩個正整數，你的函式能找到並回傳這兩個正整數的最大公因數。

輸入範例一：6 和 4
回傳：2

輸入範例二：5 和 16
回傳：1

輸入範例一：12 和 6
回傳：6
'''

"""
    @param n1:{Integer}
    @param n2:{Integer}
    @return :{Boolean}
"""
def findGCD(n1, n2):
    # 你的程式碼
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

# This loop continues until n2 becomes zero, and in each iteration, it updates the values of n1 and n2 based on the 
# remainder of the division. Once n2 becomes zero, the loop exits, and the GCD is stored in n1.

# https://www.w3schools.com/python/python_while_loops.asp