'''
13. 翻轉一個字串
輸入一個字串，你的函式能夠翻轉這個字串。

輸入範例一：Hello
回傳：olleH

輸入範例二：abcd
回傳：dcba

輸入範例一：Good Job
回傳：boJ dooG
'''

"""
    @param s:{String}
    @return :{String}
"""
def reverseString(s):
    # 你的程式碼
    return s[::-1]

# to use a slice that steps backwards, -1.
# https://www.w3schools.com/python/python_howto_reverse_string.asp
# https://www.w3schools.com/python/gloss_python_string_slice.asp

