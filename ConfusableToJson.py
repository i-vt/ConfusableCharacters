import string, json, re

def remove_front_back_space(string: str = "") -> str:
    if len(string) <= 1: return string
    while " " == string[0]: 
        if len(string) <= 1: return string
        string = string[1:]
    while " " == string[-1]: string = string[:-1]
    return string

def get_eng_leading_set(char1: string = "", char2: string = "") -> list:
    if (char1 in string.ascii_letters) or (char2 in string.ascii_letters):
        if len(char1) <= len(char2) and char1 in string.ascii_letters:
            return [char1, char2]
        elif len(char1) >= len(char2) and char2 in string.ascii_letters:
            return [char2, char1]
        elif char1 in string.ascii_letters:
            return [char1, char2]
        else: return [char2, char1]
    else:
        return char1, char2

def make_ascii_letter_set() -> set:
    return_set = {}
    for i in string.ascii_letters:
        return_set[i] = []
    return return_set

def add_to_set(set_passed: set = {}, char1: str = "", char2: str="") -> set:
    if char1 in set_passed:
        array_extracted = set_passed[char1]
        if type(array_extracted) == type(""): array_extracted = [array_extracted]
        array_extracted.append(char2)
        set_passed[char1] = array_extracted
    else:
        set_passed[char1] = [char2]
    return set_passed


def make_json(file, content) -> bool:
    try:
        with open(file, 'w', encoding='utf-8') as json_file:
            json.dump(content, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def is_unicode_notation(input_string):
    unicode_pattern = re.compile(r'(\\u[0-9a-fA-F]{4})+')
    match = unicode_pattern.fullmatch(input_string)
    return match is not None

def to_unicode_notation(input_string: str = "", unicode_slashes: bool = True) -> str:
    unicode_notations = []
    for char in input_string: 
        if unicode_slashes: unicode_notations.append(f"\\u{ord(char):04x}")
        else: unicode_notations.append(f"{ord(char):04x}")
    return ''.join(unicode_notations)

def unicode_escape_to_char(escape):
    hex_value = int(escape[2:], 16) #Ignore \u
    return chr(hex_value)

def open_confusables_and_parse(filepath: str = "confusables.txt", 
                                unicode_encoding: bool = False) -> set:

    """
    Set contents:
    {
    ...
    I ['l']
    J ['Ｊ', '𝐉', '𝐽', '𝑱', '𝒥', '𝓙', '𝔍', '𝕁', '𝕵', '𝖩', '𝗝', '𝘑', ...
    K ['K', ...
    ...
    }
    """
    # Source: http://www.unicode.org/Public/security/latest/confusables.txt
    with open(filepath, "r") as file_open:
        text_read = file_open.read()    

    variables = [] # Used for debugging, can be commented out if not needed.
    variable_set = make_ascii_letter_set()
    for line in text_read.split("\n"):
        
        special_character_splitter = "\u2192"
        if special_character_splitter not in line: continue
        key = line.split(special_character_splitter)
        if ("(" not in key[0]) or  (")" not in key[1]): continue
        char1 = key[0].split("(")[1]
        char2 = key[1].split(")")[0]
        char1 = remove_front_back_space(char1)
        char2 = remove_front_back_space(char2)
        if (char1 in string.ascii_letters) or (char2 in string.ascii_letters):
            char_list = get_eng_leading_set(char1, char2)
            char1, char2 = char_list[0], char_list[1]
            if False == is_unicode_notation(char2) and unicode_encoding: 
                char2 = to_unicode_notation(char2)
            variable_set = add_to_set(variable_set, char1, char2) 
            variables.append([char1, char2]) 
            # Used for debugging, can be commented out if not needed.
    return variable_set



if __name__ == "__main__":
    char_set = open_confusables_and_parse()
    for i,j in char_set.items(): print(i, j)
    make_json("full_characters.json", char_set)
