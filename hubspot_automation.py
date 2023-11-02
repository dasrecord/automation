import pyautogui
import time

# Individual coordinates
# first_template = (2463,502)
# second_template = (2499,530)
# third_template = (2499,596)
# next_name = (2183,453)
# create_email = (2054,447)
# templates = (3067,454)
# send_and_complete = (3122,1024)
# browser_back = (1942,47)

first_template = (2463,502)
second_template = (2499,530)
third_template = (2499,596)
next_name = (2183,453)
create_email = (2054,447)
templates = (3067,454)
send_and_complete = (3122,1024)
browser_back = (1942,47)

# Macro Sequence
macro_sequence = [next_name,create_email,templates,first_template,send_and_complete,browser_back]

# Task number
task_number = 3

# Time buffer
time_buffer = 5

# Click on a specific coordinate
def click(x, y):
    pyautogui.click(x, y)

# Perform macro by clicking on each coordinate
def perform_macro(coords):
    for coord in coords:
        click(coord[0], coord[1])
        time.sleep(time_buffer)  # Wait for n seconds between clicks

# Record macro by clicking on each coordinate and storing in list
def record_macro():
    time.sleep(10)
    print("Recording macro... press Ctrl-C to stop recording.")
    coords = []
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Position: {x}, {y}")
            time.sleep(0.2)  # Refresh Rate
    except KeyboardInterrupt:
        print("Macro recording stopped.")


# Uncomment the following line to record a macro
# macro_coords = record_macro()

# Uncomment the following line to perform the macro
for iteration in range(task_number):
    perform_macro(macro_sequence)
