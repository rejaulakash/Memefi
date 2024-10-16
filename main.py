import os
import subprocess
import webbrowser
import webbrowser as wb
# Define ANSI escape codes for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Colorful banner
banner = f"""{GREEN}

CCCCC  RRRRR  Y   Y PPPPP  TTTTT  OOOOO     III  N   N  OOOOO  V   V  AAAAA  CCCCC  EEEEE
C       R   R   Y Y  P   P    T   O     O    I   NN  N O     O V   V A     A C      E    
C       RRRR     Y   PPPPP    T   O     O    I   N N N O     O V   V AAAAAAA C      EEEE 
C       R  R     Y   P        T   O     O    I   N  NN O     O  V V  A     A C      E    
 CCCCC  R   R    Y   P        T    OOOOO     III N   N  OOOOO    V   A     A  CCCCC  EEEEE
                                                                             \033[1;91m 
  RRRR   EEEEE  JJJJJ  AAAAA  U   U  L
  R   R  E        J    A   A  U   U  L
  RRRR   EEEE     J    AAAAA  U   U  L
  R  R   E        J    A   A  U   U  L
  R   R  EEEEE  JJJ    A   A   UUU   LLLLL                                                 
{RESET}"""

# Colorful info
info = f"""{YELLOW}
--------------------------------------------------------
Author     : {CYAN}@rejaulakash{YELLOW}
Github     : {CYAN}@rejaulakash{YELLOW}
Telegram   :{CYAN} @rejaulakash{YELLOW}
TOOLS      : {CYAN}MEMEFI COIN UP{YELLOW}
------------------------------------------------------
\033[1;30m 𝘕𝘰𝘵 𝘍𝘰𝘳 𝘚𝘦𝘭𝘭, 𝘐𝘵’𝘴 𝘛𝘰𝘵𝘢𝘭𝘭𝘺 𝘍𝘳𝘦𝘦
--------------------------------------------------------{RESET}
"""

os.system("clear")
print(banner)
print(info)

auth_token = input(f"{MAGENTA}Enter your Query Id: {RESET}")

# Step 2: Delete the old query_id.txt file if it exists
file_path = 'query_id.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{GREEN}----------------------------------------------------------{RESET}")
else:
    print(f"{YELLOW}does not exist, creating a new one.{RESET}")

# Step 3: Save the new auth token into query_id.txt
with open(file_path, 'w') as file:
    file.write(auth_token)
    print(f"{GREEN}----------------------------------------------------------{RESET}")

# Step 4: Run memefi.py
try:
    subprocess.run(['python', 'memefi.py'])
except Exception as e:
    print(f"{RED}Failed to run memefi.py: {e}{RESET}")

webbrowser.open('https://t.me/rejaulakash')
