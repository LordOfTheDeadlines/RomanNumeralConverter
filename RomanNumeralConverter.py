class RomanNumeralConverter:
    def romanToInt(self, roman_num):
        roman_digits = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        previous_char = 0
        result = 0

        for i in range(len(roman_num.value) - 1, -1, -1):
        # for i in range(0, len(roman_num.value), 1):
            temp_char = roman_num.value[i]

            if roman_digits[temp_char] >= previous_char:
                result += roman_digits[temp_char]
            else:
                result -= roman_digits[temp_char]

            previous_char = roman_digits[temp_char]

        print(result)