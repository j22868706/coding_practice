'''
6. 找到最小公倍數
輸入兩個正整數，你的函式能找到並回傳這兩個正整數的最小公倍數。

輸入範例一：6 和 4
回傳：12

輸入範例二：5 和 16
回傳：80

輸入範例一：12 和 6
回傳：12
'''

"""
    @param n1:{Integer}
    @param n2:{Integer}
    @return :{Boolean}
"""
def findLCM(n1, n2):
    # 你的程式碼
    for i in range(1, n1 * n2 + 1):
        if i % n1 == 0 and i % n2 == 0:
            return i

# range's syntax: range(start, stop, step)

# refernece: https://www.w3schools.com/python/ref_func_range.asp
        