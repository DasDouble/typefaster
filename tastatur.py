import keyboard
import enchant
import itertools

# Initialize the English dictionary
d = enchant.Dict("en_US")

# Initialize an empty buffer
buffer = ''

def keypress(e):
    global buffer
    if e.name == 'space':
        print('Buffer:', buffer)  # print the contents of the buffer

        # Generate all permutations of the buffer
        perms = [''.join(p) for p in itertools.permutations(buffer)]
        print('Permutations:', perms)  # print the generated permutations

        # Check each permutation if it is a valid word
        for perm in perms:
            if d.check(perm):
                print('Word:', perm)  # print the valid word
                break

        # Reset the buffer
        buffer = ''
    elif e.name == 'backspace':
        buffer = buffer[:-1]  # delete the last character
    else:
        buffer += e.name

# Register the keypress event handler
keyboard.on_press(keypress)

# Wait for the 'esc' key to be pressed to exit the program
keyboard.wait('esc')
