from flask import Flask, render_template, request
from random import randint
import string
from ConfuseSentence import ConfuseSentence
from CharacterSets.CharacterSetHelper import CharacterSetHelper as csh

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/obfuscate', methods=['POST'])
def obfuscate():
    if request.method == 'POST':
        # Get the user input from the form
        og_text = request.form.get('text_input')
        
        # Get the keywords to obfuscate (if provided)
        keywords_input = request.form.get('keywords', "")
        words_to_obfuscate = [kw.strip() for kw in keywords_input.split(",,,") if kw.strip()]
        
        # Get the percent chance to obfuscate (default to 100%)
        percent_chance = int(request.form.get('percent_chance', 100))
        
        # Get the selected character set (either 'basic' or 'full')
        char_set = request.form.get('char_set', 'full')  # Default to 'full' if not provided
        
        # Initialize the ConfuseSentence object with the original text
        confuser = ConfuseSentence(og_text)
        
        # Select the character set based on the user's choice
        if char_set == 'basic':
            char_set_dict = csh().get_basic()
        else:
            char_set_dict = csh().get_full()
        
        # Perform the obfuscation
        result = confuser.auto_obfuscate(words_to_obfuscate, percent_chance, char_set_dict)
        
        # Pass the result, keywords, selected character set, and percent chance back to the template
        return render_template(
            'index.html',
            original_text=og_text,
            obfuscated_text=result,
            keywords=keywords_input,
            char_set=char_set,
            percent_chance=percent_chance  # Pass the percent chance back to the template
        )


if __name__ == "__main__":
    app.run(debug=True)
