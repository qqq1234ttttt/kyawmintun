# kyawmintun_hacker.py

import time
import os

GREEN = "\033[1;32m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def intro():
    clear()
    name = r"""
██╗  ██╗   ███╗   ███╗   ████████╗
██║ ██╔╝   ████╗ ████║   ╚══██╔══╝
█████╔╝    ██╔████╔██║      ██║   
██╔═██╗    ██║╚██╔╝██║      ██║   
██║  ██╗   ██║ ╚═╝ ██║      ██║   
╚═╝  ╚═╝   ╚═╝     ╚═╝      ╚═╝   

        >>> KYAW MIN TUN <<<
"""
    print(GREEN + name + RESET)
    time.sleep(2)

def loading():
    print(GREEN + "\n[+] Initializing system", end="")
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(RESET)
    time.sleep(1)

def banner():
    print(GREEN + r"""
[ SYSTEM READY ]
""" + RESET)

def fake_report(platform, link):
    clear()
    banner()
    print(GREEN + f"\n[+] Target: {link}")
    print(f"[+] Platform: {platform}\n" + RESET)

    count = 1
    while True:
        print(GREEN + f"[+] Sending report #{count}..." + RESET)
        count += 1
        time.sleep(0.6)

def main():
    intro()
    loading()

    print(GREEN + "\n[1] Facebook Report")
    print("[2] TikTok Report\n" + RESET)

    choice = input(GREEN + "Select option: " + RESET)

    if choice == "1":
        link = input(GREEN + "Enter Facebook link: " + RESET)
        fake_report("Facebook", link)

    elif choice == "2":
        link = input(GREEN + "Enter TikTok link: " + RESET)
        fake_report("TikTok", link)

    else:
        print(GREEN + "Invalid choice!" + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(GREEN + "\n\n[!] System Stopped" + RESET)
