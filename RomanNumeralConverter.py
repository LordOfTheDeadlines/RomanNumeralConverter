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

    def romanToInt(self, roman_num):

        roman_num = roman_num.upper().replace(' ', '')

        if not self.isCorrect(roman_num):
            return -1

        print(self.convert(roman_num))

    def convert(self, roman_num):
        previous_char = 0
        result = 0

        for i in range(len(roman_num) - 1, -1, -1):
            temp_char = roman_num[i]

            if self.roman_chars[temp_char] >= previous_char:
                result += self.roman_chars[temp_char]
            else:
                result -= self.roman_chars[temp_char]

            previous_char = self.roman_chars[temp_char]

        return result

    def isCorrect(self, roman_num):

        length = len(roman_num)

        if length < 1:
            return False
        elif length > 15:
            print('Длина числа должна быть не более 15-ти символов')
            return False
        elif self.isConsistArabicDigits(roman_num):
            print('Римское число включает арабские цифры')
            return False
        elif self.isConsistWrongChars(roman_num):
            print('Римское число включает недопутимые символы')
            return False
        return True

    def isConsistArabicDigits(self, value):
        for symbol in value:
            if symbol.isdigit():
                return True
        return False

    def isConsistWrongChars(self, value):
        for symbol in value:
            if symbol not in self.roman_chars:
                return True
        return False

