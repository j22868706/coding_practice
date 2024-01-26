'''
9. 用預設值填滿空字串
輸入一個可能包含空字串的字串陣列 / 列表，以及一個預設值，你的函式能把陣列 / 列表中的空字串用預設值取代。

輸入範例一：["Hello", "World", ""]、以及預設值 "test"
回傳：["Hello", "World", "test"]

輸入範例二：["", "ok", ""]、以及預設值 "failed"
回傳：["failed", "ok", "failed"]

輸入範例一：["no empty"]、以及預設值 "word"
回傳：["no empty"]
'''

"""
    @param words:{[String]}
    @param value:{String}
    @return :{[String]}
"""
def fill(words, value):
    # 你的程式碼
    for i in range(len(words)):
        if words[i] == "":
            words[i] = value
        return words
    

'''
    Note:
    Fills empty strings in the given list with the specified value.
    1. Firstly, use a for loop to iterate over each value in the list.
    2. If the value is "", replace it with the specified value.
    3. Return the result.
'''
