import keyboard
import time

# Define the list of numbers to input
numbers = """
3
3
3
3
3
3
2
2
3
2
2
1
1
1
1
3
3
3
1
3
3
2
1
1
1
1
1
1
1
1
"""

# Delay between each key press in seconds
delay = 0.2

# Wait for 5 seconds before starting
time.sleep(2)

# Loop through each number in the list and input it
for i, number in enumerate(numbers.split("\n")):
    # Loop through each digit in the number and input it
    for digit in number:
        keyboard.press(digit)
        time.sleep(delay)
        keyboard.release(digit)

    time.sleep(.1)
    keyboard.press("enter")
    time.sleep(.1)
    keyboard.release("enter")
    
    # Wait for a short delay before inputting the next number
    time.sleep(delay)
