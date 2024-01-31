'''
16. 偶數測試
輸入一個整數，若輸入的整數是偶數，回傳真；否則，回傳假。

輸入範例一：0
回傳：真

輸入範例二：-7
回傳：假

輸入範例一：102
回傳：真
'''

"""
    @param n:{Integer}
    @return :{Boolean}
"""
def checkEven(n):
    # 你的程式碼
    if n == 0:
        return True
    elif n % 2 == 0:
        return True
    else: 
        return False