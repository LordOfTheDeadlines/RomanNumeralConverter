from RomanNumeralException import RomanNumeralException


class RomanNumber:
    def __init__(self, value):
        self.status = self.isCorrect(value)
        self.value = value

    romanChars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}

    def isCorrect(self, value):
        if self.isConsistArabicDigits(value):
            raise RomanNumeralException('Римское число включает в себя арабские цифры')
        value = value.upper().replace(' ', '')
        return True
    def isConsistArabicDigits(self, value):
        for symbol in value:
            if symbol.isdigit():
                return True
        return False



