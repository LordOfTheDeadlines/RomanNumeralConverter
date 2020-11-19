class RomanNumeralConverter:
    roman_chars = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    def romanToInt(self, roman_num: str) -> int:

        roman_num = roman_num.upper().replace(' ', '')

        if not self.is_correct(roman_num):
            return -1

        return self.convert(roman_num)

    def convert(self, roman_num):
        previous_num = 0
        result = 0

        for i in range(len(roman_num) - 1, -1, -1):
            temp_char = roman_num[i]
            temp_num = self.roman_chars[temp_char]

            if temp_num >= previous_num:
                result += temp_num
            else:
                result -= temp_num

            previous_num = temp_num

        return result

    def is_correct(self, roman_num):

        length = len(roman_num)

        if length < 1:
            return False
        elif length > 15:
            print('Длина числа должна быть не более 15-ти символов')
            return False
        elif self.is_consist_arabic_digits(roman_num):
            print('Римское число включает арабские цифры')
            return False
        elif self.is_consist_wrong_chars(roman_num):
            print('Римское число включает недопутимые символы')
            return False
        return True

    def is_consist_arabic_digits(self, value):
        for symbol in value:
            if symbol.isdigit():
                return True
        return False

    def is_consist_wrong_chars(self, value):
        for symbol in value:
            if symbol not in self.roman_chars:
                return True
        return False
