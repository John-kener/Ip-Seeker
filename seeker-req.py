import os,sys

print("\033[32m [+] Installing Requirements...\033[0m")
print()

os.system("pip install --upgrade pip")
os.system("pkg upgrade && pkg update")
os.system("pkg install python -y ")
os.system("pkg install python2 -y")
os.system("pip install requests")
os.system("pip install socket")
os.system("pip install json")
print()
print()
print("\033[32m [+] Now Run :- \033[34mpython tmail.py \033[32mHere  or \033[34mTmail\033[0m\033[32m At Any place \033[0m")
