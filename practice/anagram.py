class AnagramClass:
    def isAnagram(self, string1: str, string2: str) -> bool:
        if len(string1) != len(string2):
            return False
        frequency_string1 = {}

        for letter in string1:
            if letter in frequency_string1.keys():
                frequency_string1[letter] = frequency_string1[letter] + 1
            else:
                frequency_string1[letter] = 1

        for letter in string2:
            if not letter in frequency_string1.keys():
                return False
            frequency_string1[letter] -= 1

        for counts in frequency_string1:
            if frequency_string1[counts] != 0:
                return False

        return True


anagram = AnagramClass()
print(anagram.isAnagram("abc", "bca"))
print(anagram.isAnagram("abc", "bcs"))
