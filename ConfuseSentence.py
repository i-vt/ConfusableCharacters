import random, string, json, re
if __name__!="__main__":
from CharacterSets.CharacterSetHelper import CharacterSetHelper as csh

def pick_random_letter() -> str:
    letters = string.ascii_letters
    return_char = random.choice(letters)
    return return_char

def pick_random_letter() -> str:
    letters = string.ascii_letters
    return_char = random.choice(letters)
    return return_char

def generate_random(type_char: str = "numeric", length: int=1) -> str:
    type_char = type_char.lower()
    return_chars = ""
    if "numeric" == type_char: 
        for _ in range(length): return_chars += str(random.randint(0,10))
    elif "alphabetic" == type_char: 
        for _ in range(length): return_chars += pick_random_letter()
    return return_chars

def find_nth_occurrence(text: str, substring: str, n: int) -> int:
    """
    Finds the n-th occurrence of a substring in a string.
    
    Args:
    text (str): The text to search within.
    substring (str): The substring to search for.
    n (int): The occurrence number to find (1-based).

    Returns:
    int: The index of the n-th occurrence of the substring, or -1 if not found.

    text = "In a world where intelligence illuminates the path to success, my brother stands tall as a beacon of brilliance. world world""
    index = find_nth_occurrence(text, "wor)
    """
    start = -1
    for _ in range(n):
        start = text.find(substring, start + 1)
        if start == -1:
            break
    return start


def replace_characters_randomly(original_text: str = "", 
                                replaced: list = [], 
                                replacements: list = [],
                                percent_chance_to_replace: int = 100) -> str:
    total_opportunities = 0
    total_replaced = 0
    for replaced_sequence in replaced:
        total_opportunities += original_text.count(replaced_sequence)
        occur_count = original_text.count(replaced_sequence)
        for count in range(1, occur_count + 1):
            if random.randint(0, 100) < percent_chance_to_replace:
                total_replaced += 1
                start_index = find_nth_occurrence(original_text, replaced_sequence, count)
                if start_index != -1:
                    end_index = start_index + len(replaced_sequence)
                    replaced_for = random.choice(replacements)
                    original_text = original_text[:start_index] + replaced_for + original_text[end_index:]
    #if total_opportunities > 0:
    #    print(total_replaced / total_opportunities)
    return original_text



class ConfuseSentence:
    def __init__(self, og_text: str=""):
        self.original_text = og_text
        self.original_text_backup = self.original_text
        self.default_dict = {
        "a": [
            "\u0430",
            "\u00e0",
            "\u00e1",
            "\u1ea1",
            "\u0105"
        ],
        "c": [
            "\u0441",
            "\u0188",
            "\u010b"
        ],
        "d": [
            "\u0501",
            "\u0257"
        ],
        "e": [
            "\u0435",
            "\u1eb9",
            "\u0117",
            "\u0117",
            "\u00e9",
            "\u00e8"
        ],
        "g": [
            "\u0121"
        ],
        "h": [
            "\u04bb"
        ],
        "i": [
            "\u0456",
            "\u00ed",
            "\u00ec",
            "\u00ef"
        ],
        "j": [
            "\u0458",
            "\u029d"
        ],
        "k": [
            "\u03ba"
        ],
        "l": [
            "\u04cf",
            "\u1e37"
        ],
        "n": [
            "\u0578"
        ],
        "o": [
            "\u043e",
            "\u03bf",
            "\u0585",
            "\u022f",
            "\u1ecd",
            "\u1ecf",
            "\u01a1",
            "\u00f6",
            "\u00f3",
            "\u00f2"
        ],
        "p": [
            "\u0440"
        ],
        "q": [
            "\u0566"
        ],
        "s": [
            "\u0282"
        ],
        "u": [
            "\u03c5",
            "\u057d",
            "\u00fc",
            "\u00fa",
            "\u00f9"
        ],
        "v": [
            "\u03bd",
            "\u0475"
        ],
        "x": [
            "\u0445",
            "\u04b3"
        ],
        "y": [
            "\u0443",
            "\u00fd"
        ],
        "z": [
            "\u0290",
            "\u017c"
        ]
        }

    def get_keywords_with_uuid(self, keywords: list = [], type_uuid: str = "numeric", length: int = 20) -> dict:
        return_dict = {}
        for keyword in keywords:
            return_dict[keyword.lower()] = generate_random(type_uuid, length)
        return return_dict




    def revert_keywords_with_uuid(self, keywords: dict = {}) -> str:
        original_text = self.original_text
        for key, value in keywords.items():
            while value in original_text: 
                original_text = original_text.replace(value, key)
        return original_text

    def replace_keywords_with_uuid(self, keywords: dict = {}) -> str:
        """
        example usage:
        words_dict = {'real estate': 'uuid899453654uuid', 'sell house for cash': 'uuid886129467uuid', 'buy house': 'uuid894106703uuid'}
        og_text = "Real estate house buy sell house, because sell house for cash"
        replaced = replace_keywords_with_uuid(og_text, words_dict) 
        # Expected output
        # uuid899453654uuid house buy sell house, because uuid886129467uuid
        """
        text_changed = self.original_text
        original_text_lower = text_changed.lower()
        for key, value in keywords.items():
            while key in original_text_lower:
                start_index = original_text_lower.index(key)
                end_index = start_index + len(key)
                text_changed = text_changed[:start_index] + value + text_changed[end_index:]
                original_text_lower = text_changed.lower()
        return text_changed

    def replace_spaces(self) -> str:
        replacements = [" ", " ", " ", " ", " ", "  ", " ", " ", " ", " "]
        return_str = replace_characters_randomly(self.original_text, [" "], replacements)
        return return_str


    def eng_to_int_chars(self, 
                        percent_chance_to_replace: int=100,
                        custom_dict: dict = {}) -> str:
        
        if {} == custom_dict: custom_dict = self.default_dict
        original_text = self.original_text
        for key, value in custom_dict.items():
            if type(value) != type([]): value = [value]
            original_text = replace_characters_randomly(original_text, 
                                                        [key], 
                                                        value, 
                                                        percent_chance_to_replace)
            #print(key, value, original_text, input())
        #self.original_text = self.original_text_backup
        return original_text

    def auto_obfuscate(self, 
                        unobfuscated_words = [], 
                        percent_chance_to_replace: int=100, 
                        custom_dict: dict = {}) -> str:

        #print(custom_dict)
        if {} == custom_dict: custom_dict = self.default_dict
        original_text = self.original_text
        #print(custom_dict)
        if percent_chance_to_replace < 0: 
            percent_chance_to_replace(random.randint(0,int(percent_chance_to_replace * -1)))

        words_dict = self.get_keywords_with_uuid(unobfuscated_words)
        #print(words_dict)
        self.original_text = self.replace_keywords_with_uuid(words_dict)
        #print(self.original_text)
        self.original_text = self.replace_spaces()
        #print(self.original_text)
        self.original_text = self.eng_to_int_chars(percent_chance_to_replace, custom_dict)
        #print(self.original_text)
        self.original_text = self.revert_keywords_with_uuid(words_dict)
        
        return_str = self.original_text
        
        self.original_text = self.original_text_backup


        return return_str




if __name__ == "__main__":
    og_text = '''By downloading, installing, or using "ConfusableCharacters" you acknowledge that you have read, understood, and agreed to abide by this disclaimer. If you do not agree to these terms, do not use the software.'''
    desired_words = ["ConfusableCharacters", "No Liability", "disclaimer"]

    print(ConfuseSentence(og_text).auto_obfuscate(desired_words, 10, csh().get_full()))


