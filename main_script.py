import pyautogui
import time
import subprocess
import os

print("Welcome to Microsoft Teams Automation")

# Step 1: Taking co-ordinates of Teams application
screen_width, screen_height = pyautogui.size() # Get the screen resolution from PyAutoGUI library
print("screen width = ",screen_width)
print("screen height = ", screen_height)
vertical = screen_height - 30 # Vertical position of Teams
horizontal = screen_width - 820 # Horizontal position of Teams


# Step 2: Simulate mouse movement to stay active
while True: # Runs infinitely until the program is stopped OR the mouse is bought to any one of the screen edge
    print("Simulating mouse movement...")

    pyautogui.moveTo(horizontal, vertical, duration=0.5) # Move the mouse to the location of teams application
    pyautogui.leftClick() # Left click on the Teams application
    time.sleep(0.5) # Wait for the Teams to open

    center_x, center_y = screen_width // 2, screen_height // 2 # Get the center co-ordinates of the screen
    pyautogui.moveTo(center_x, center_y, duration=0.5) # Move the mouse cursor to the center of the screen

    pyautogui.moveRel(200, 0, duration=0.5)  # Move right
    pyautogui.moveRel(-200, 0, duration=0.5)  # Move back

    pyautogui.moveTo(horizontal, vertical, duration=0.5) # Move the mouse cursor back to the Teams application
    pyautogui.leftClick() # Make a left click which closes the Teams application

    # Start the timer after which the mouse simulation starts again
    timer = 10 # Adjust timer in seconds
    print(f"Timer set for {timer} seconds")
    for sec in range(timer):
        print(f"Time in sec: {sec + 1}")
        time.sleep(1) # Simulates each second
    print("----------------------------------------------") # Represents end of one infinite cycle
