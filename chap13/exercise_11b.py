# ME Computer, Mandalay.
# June 24, 2022
# exercise_11.py

# Write a program that solves word jumble problems.

#     1. Problem analysis
#        Given a scrambled sequence of letters, produce all possible words from those letters.
#        Note: I am assuming that the words produced can be of varying length.

#     2. Specification
#        Input: a jumble of letters (e.g., hatcife)
#        Output: All possible words of any length listed in alphabetical order
#               (e.g., a, at, ate, cat, fat, fate, hat, hate, hit, ice, tie)

#     3. Design
#        Ask user to input letters without spaces
#        Get input from user as a string
#        Generate every possible combination of string
#             For each list size of length 1 up to length of input string (e.g., 7)
#
#             [_] 7 possibilities                       (7)                         len(inputstr) - 0
#             [_][_] 42 possibilites                    (7 * 6)                     * len(inputstr) - 1
#             [_][_][_] 210 possibilities               (7 * 6 * 5)                 * len(inputstr) - 2
#             [_][_][_][_] 840 possibilites             (7 * 6 * 5 * 4)
#             [_][_][_][_][_] 2520 possibilites         (7 * 6 * 5 * 4 * 3)
#             [_][_][_][_][_][_] 7560 possibilities     (7 * 6 * 5 * 4 * 3 * 2) 
#             [_][_][_][_][_][_][_] 7560 possibilities  (7 * 6 * 5 * 4 * 3 * 2 * 1)
#
#            StringIN = hatcife
#            StringOUT = []
#            iStringIN = 0
#            for i in StringIN
#               while iStringIN < (StringIN(len) - i)   # add first row possibilities
#                   StringOUT.append.(StringIN[iStringIN(i)])
#                   iStringIN = iStringIN + 1
#                
#           if s == "":
#                return [s]
#               
#           else:
#                ans = []             
#
#        Perform binary search within appropriate section of dictionary
#        Print word if it is found in dictionary

#     4. Implementation
#     5. Test/debug
#     6. Maintentance
 

# Program generates all anagrams of an array, then checks them against 
# a dictionary. The program prints the dictionary word(s) > 4 letters that correspond(s) 
# with the anagram.

class WordTruer:
    def __init__(self, dictionary, string):
        self.dictionary = dictionary
        self.string = string
        self.anagrams = self.permute(self.string)
        self.twords = []
        self.dwords = []
        self.read_dict()
        
        self.check_anagrams()
        self.summary()

    def read_dict(self):
        with open(self.dictionary, 'r') as f:
            for word in f.readlines():
                self.dwords.append(word.strip())

    def permute(self, s):
        p = []
        if len(s) <= 1:
            p = [s]        
        else:
            for i, let in enumerate(s):
                for perm in self.permute(s[:i] + s[i+1:]):
                    p += [let + perm] 
        return p
    
    # TODO: Incorporate gaddag algorithm to speed up check anagrams 
    def gaddag(self):
        pass
        
    def check_anagrams(self):
        for an in self.anagrams:
            if self.binary_search(self.dwords, an):
                self.twords.append(an)

    def binary_search(self, arr, inword):
        # Base case: if empty array, inword not in dictionary
        if len(arr) == 0:
            return False
        else:
            # Find middle of list, assign value to variable dictword 
            mid = len(arr) // 2
            dictword = arr[mid]
            # if inword in dictionary, return True
            if inword == dictword:
                return True
            else:
                # Initiate variables for top and bottom of list 
                left = arr[:mid]
                right = arr[mid+1:]

                if inword < dictword:
                    return self.binary_search(left, inword)
                else:
                    return self.binary_search(right, inword)

    def summary(self):
        for word in self.twords:
            print(word)

# WordTruer('eng_dictionary.txt', 'viola')
WordTruer('eng_dictionary.txt', 'hates')