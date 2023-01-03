import colorama
from colorama import Fore, Back, Style
import keyboard
import os
import time

old_time = time.time()
colorama.init(autoreset=True)
text = "sentence is used to get you to summarize a topic we are discussing clearly and correctly I know a 50 word sentence is a run on sentence and would make English teachers cringe That is why when I assign for word sentence is a run on sentence and would make English teachers cringe That is why when I assign for  why when I assign for word sentence is a run on sentence and would make English teachers cringe That is why when I assign for sentence is used to get you to summarize a topic we are discussing clearly and correctly I know a 50 word sentence is a run on sentence and would make English teachers cringe That is why when I assign for word sentence is a run on sentence and would make English teachers cringe That is why when I assign for  why when I assign for word sentence is a run on sentence and would make English teachers cringe That is why when I assign for".lower()
old_text = text
wrong = 0
for j,i in enumerate(old_text):
    os.system("cls")
    typed_text = text[:j]
    new_text = Fore.GREEN + text[0:j] + Fore.WHITE + text[j:]
    stop_time = time.time() - old_time
    if stop_time >= 60:
        break
    print(new_text[:j+30])
    while stop_time <= 60:
        if i != " " and keyboard.read_key() == i:
            break
        elif i == " " and keyboard.read_key() == "space":
            break
        else:
            wrong += 1
            pass
os.system("cls")
print(f"You Typed {len(typed_text.split())} words per minute")
print(f"Your Accuracy Is: {100 - (wrong/100)}%")
print(Fore.CYAN + "Nice!!")
time.sleep(5)