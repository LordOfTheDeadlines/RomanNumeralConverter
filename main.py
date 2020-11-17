from RomanNumber import RomanNumber
from RomanNumeralConverter import RomanNumeralConverter


class Solution:
    converter = RomanNumeralConverter()
    print('Введите значение римского числа')
    roman_num = RomanNumber(str(input()))
    converter.romanToInt(roman_num)
    print(roman_num.value)
    print(roman_num.status)
