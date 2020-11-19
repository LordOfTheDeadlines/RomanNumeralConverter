from Solution import Solution


converter = Solution()
while True:
    print('Введите значение римского числа')
    roman_num = str(input())
    result = converter.romanToInt(roman_num)
    if result != -1:
        print(result)
