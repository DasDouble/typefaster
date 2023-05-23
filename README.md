# Keyboard Typefaster

This Python script listens to keyboard input and checks for valid English words in the entered text. It uses the `keyboard` library to capture keypress events and the `enchant` library to validate words against an English dictionary.

## Prerequisites

- Python 3.x
- `keyboard` library (install using `pip install keyboard`)
- `enchant` library (install using `pip install pyenchant`)

## Usage

1. Run the script by executing `python word_checker.py` in the terminal.
2. Start typing in any text.
3. Press the **space** key to check for valid words in the entered text.
4. The script will print the entered text, generated permutations of the text, and the first valid English word found.
5. Press the **backspace** key to delete the last character in the entered text.
6. Press any key other than alphabetic characters (a-z) to stop the script from further processing.
7. Press the **esc** key to exit the program.

Please note that the current implementation has some limitations and may require heavy modifications for advanced functionality. Here are some considerations:

- **Character Limitations**: The script currently only detects alphabetic characters (a-z). Pressing any other key will stop the script from further processing.
- **English Word Detection**: The script uses the `enchant` library to validate words against an English dictionary. However, this approach may not be foolproof and could produce false positives or miss certain valid words.
- **Resource Usage**: Generating permutations of the entered text can consume a significant amount of memory, especially for longer input. Consider implementing optimizations or constraints to limit resource usage if necessary.
- **Modification**: Depending on your specific requirements, you may need to modify the script significantly to meet your needs. Feel free to customize and extend the functionality as required.
- **Word Detection**: The script currently detects words based on their position in the dictionary. It selects the first valid English word found. An improvement for anyone interested in working on this project would be to explore alternative word ranking algorithms, such as analyzing word frequency or context, to provide more accurate or relevant suggestions.
- **Project Enhancement**: If you are interested in enhancing this project, you could consider incorporating advanced natural language processing techniques, building a more comprehensive word database, or implementing machine learning algorithms to improve word detection accuracy and offer better word suggestions.

Feel free to modify the script according to your needs and explore different functionalities. Happy coding!
