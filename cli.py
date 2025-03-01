import argparse
import json
from ConfuseSentence import ConfuseSentence
from CharacterSets.CharacterSetHelper import CharacterSetHelper

def load_character_set(file_path):
    """Load character set from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(description="Text Obfuscation Tool")
    
    # Adding arguments
    parser.add_argument('text', type=str, help="Text to obfuscate")
    parser.add_argument('-k', '--keywords', type=str, default='', help="Comma-separated keywords to obfuscate specifically")
    parser.add_argument('-p', '--percent', type=int, default=100, help="Percentage chance to obfuscate [0-100]")
    parser.add_argument('-c', '--charset', type=str, choices=['basic', 'full'], default='full', help="Character set to use ('basic' or 'full')")

    args = parser.parse_args()

    # Load character set based on user choice
    if args.charset == 'basic':
        character_set = load_character_set('CharacterSets/basic_characters.json')
    else:
        character_set = load_character_set('CharacterSets/full_characters.json')

    # Process keywords
    keywords = args.keywords.split(',') if args.keywords else []

    # Create ConfuseSentence object
    confuser = ConfuseSentence(args.text)

    # Obfuscate text
    result = confuser.auto_obfuscate(keywords, args.percent, character_set)

    # Output the result
    print("\nOriginal Text:", args.text)
    print("Obfuscated Text:", result)

if __name__ == "__main__":
    main()
