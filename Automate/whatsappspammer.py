import pyautogui as troll
import time
import random

# Define a list of random messages
messages = [
    "https://www.instagram.com/reel/DBbLTu6tlmT/?igsh=ODVweXFyeGVlN2tm", 
    "https://www.instagram.com/reel/DBS-HhMuYhs/?igsh=MTNlcG82bWFqa3RoOA==", 
    "https://www.instagram.com/reel/C_2Z7m_MMan/?igsh=dTJka2g3dmdqa3Rp", 
    "https://www.instagram.com/reel/DBXzzs9IDmK/?igsh=bXJsZTFxYnlhMzIw", 
    "https://youtu.be/elgbG0Q_UCU?si=wRti6uF0rtavzrk3", 
    "https://www.youtube.com/watch?v=ruuxbxbWL_0", 
    "https://www.youtube.com/watch?v=rTKYuH0PnhQ", 
    "https://www.youtube.com/watch?v=CUl_nAIRu0A", 
    "https://www.youtube.com/watch?v=iFvy1XR0Ueg", 
]

limit = input("Enter the number of messages: ")

i = 0
time.sleep(2)

# Loop to send random messages
while i < int(limit):
    msg = random.choice(messages)  # Choose a random message from the list
    troll.typewrite(msg)
    troll.press("Enter")
    i += 1
