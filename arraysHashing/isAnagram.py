class Solution(object):
    def isAnagram(self, s, t):
        # creates two seperate dictionaries for two seperate strings, s and t
        letterCount1 = {}
        letterCount2 = {}

        # loops through both strings and checks if the character you are on is already in our dictionary for that string. 
        # -> if so, increments the amount of that character, because we are tracking the frequency that each character comes up
        # -> if not, adds it and says that there is 1 of that character present
        for char in s:
            if char in letterCount1:
                letterCount1[char] += 1
            else:
                letterCount1[char] = 1
        for char in t:
            if char in letterCount2:
                letterCount2[char] += 1
            else:
                letterCount2[char] = 1
        
        # compares if both dictionaries are the same - if so, they that means they meet the conditions of an anagram (same length,  same letters, same number of times)
        # key note, order does not matter for number of direct equality comparison, just checks same keys and same numbers of said keys
        return letterCount1 == letterCount2