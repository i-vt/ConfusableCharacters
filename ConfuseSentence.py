import random
import string
from CharacterSets.CharacterSetHelper import CharacterSetHelper as csh

def pick_random_letter() -> str:
    letters = string.ascii_letters
    return random.choice(letters)

def generate_random(type_char: str = "numeric", length: int = 1) -> str:
    type_char = type_char.lower()
    return_chars = ""
    if type_char == "numeric":
        return_chars = ''.join(str(random.randint(0, 9)) for _ in range(length))
    elif type_char == "alphabetic":
        return_chars = ''.join(pick_random_letter() for _ in range(length))
    return return_chars

def find_nth_occurrence(text: str, substring: str, n: int) -> int:
    start = -1
    for _ in range(n):
        start = text.find(substring, start + 1)
        if start == -1:
            break
    return start

def replace_characters_randomly(original_text: str, replaced: list, replacements: list, percent_chance_to_replace: int = 100) -> str:
    for replaced_sequence in replaced:
        occur_count = original_text.count(replaced_sequence)
        for count in range(1, occur_count + 1):
            if random.randint(0, 100) < percent_chance_to_replace:
                start_index = find_nth_occurrence(original_text, replaced_sequence, count)
                if start_index != -1:
                    end_index = start_index + len(replaced_sequence)
                    replaced_for = random.choice(replacements)
                    original_text = original_text[:start_index] + replaced_for + original_text[end_index:]
    return original_text

class ConfuseSentence:
    def __init__(self, og_text: str = ""):
        self.original_text = og_text
        self.original_text_backup = og_text
        self.default_dict = {
            "a": ["\u0430", "\u00e0", "\u00e1", "\u1ea1", "\u0105"],
            "c": ["\u0441", "\u0188", "\u010b"],
            "d": ["\u0501", "\u0257"],
            "e": ["\u0435", "\u1eb9", "\u0117", "\u00e9", "\u00e8"],
            "g": ["\u0121"],
            "h": ["\u04bb"],
            "i": ["\u0456", "\u00ed", "\u00ec", "\u00ef"],
            "j": ["\u0458", "\u029d"],
            "k": ["\u03ba"],
            "l": ["\u04cf", "\u1e37"],
            "n": ["\u0578"],
            "o": ["\u043e", "\u03bf", "\u0585", "\u022f", "\u1ecd", "\u1ecf", "\u01a1", "\u00f6", "\u00f3", "\u00f2"],
            "p": ["\u0440"],
            "q": ["\u0566"],
            "s": ["\u0282"],
            "u": ["\u03c5", "\u057d", "\u00fc", "\u00fa", "\u00f9"],
            "v": ["\u03bd", "\u0475"],
            "x": ["\u0445", "\u04b3"],
            "y": ["\u0443", "\u00fd"],
            "z": ["\u0290", "\u017c"]
        }

    def get_keywords_with_uuid(self, keywords: list, type_uuid: str = "numeric", length: int = 20) -> dict:
        return {kw.lower(): generate_random(type_uuid, length) for kw in keywords}

    def revert_keywords_with_uuid(self, keywords: dict) -> str:
        text = self.original_text
        for key, value in keywords.items():
            text = text.replace(value, key)
        return text

    def replace_keywords_with_uuid(self, keywords: dict) -> str:
        text = self.original_text
        lowered = text.lower()
        for key, value in keywords.items():
            while key in lowered:
                start = lowered.index(key)
                end = start + len(key)
                text = text[:start] + value + text[end:]
                lowered = text.lower()
        return text

    def replace_spaces(self) -> str:
        replacements = [" ", " ", " ", " ", " ", "  ", " ", " ", " ", " "]
        return replace_characters_randomly(self.original_text, [" "], replacements)

    def eng_to_int_chars(self, percent_chance_to_replace: int = 100, custom_dict: dict = None) -> str:
        if custom_dict is None:
            custom_dict = self.default_dict
        text = self.original_text
        for key, values in custom_dict.items():
            if not isinstance(values, list):
                values = [values]
            text = replace_characters_randomly(text, [key], values, percent_chance_to_replace)
        return text

    def auto_obfuscate(self, unobfuscated_words=None, percent_chance_to_replace: int = 100, custom_dict: dict = None) -> str:
        if unobfuscated_words is None:
            unobfuscated_words = []
        if custom_dict is None:
            custom_dict = self.default_dict

        words_dict = self.get_keywords_with_uuid(unobfuscated_words)
        self.original_text = self.replace_keywords_with_uuid(words_dict)
        self.original_text = self.replace_spaces()
        self.original_text = self.eng_to_int_chars(percent_chance_to_replace, custom_dict)
        self.original_text = self.revert_keywords_with_uuid(words_dict)

        result = self.original_text
        self.original_text = self.original_text_backup
        return result
