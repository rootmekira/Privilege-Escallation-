# Thia acript will be use to turn off the tamper protection.


import pyautogui
import time

def open_tamper_protection():
    # Brief pause to allow the system to be ready
    time.sleep(0)

    # Open Start menu and search for 'tamper protection'
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('tamper protection')
    time.sleep(1)
    pyautogui.press('enter')  # Open the search result
    time.sleep(1.0)

    # Press Tab 7 times to navigate to the toggle
    for _ in range(7):
        pyautogui.press('tab')
        time.sleep(0)

    # Toggle the setting with Space
    pyautogui.press('space')
    time.sleep(2)


    pyautogui.press('win + d')
    time.sleep(2)

# Call the function
open_tamper_protection()
