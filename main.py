from RomanNumeralConverter import RomanNumeralConverter


class Solution:
    converter = RomanNumeralConverter()
    while True:
        print('Введите значение римского числа')
        roman_num = str(input())
        result = converter.romanToInt(roman_num)
        if result != -1:
            print(result)
