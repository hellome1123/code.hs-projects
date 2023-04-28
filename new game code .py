from random import randint
from time import sleep
import time
import sys

username = input("Enter username:")
print("Username is: " + username)

#animation = "|/-\\"

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
    sys.stdout.flush()
    
print("\nDone!")

while True:
  a = randint(1000000000000000000000000000000000000000000000000, 9999999999999999999999999999999999999999999999999)
  b = randint(0, 75)
  if b == 0:
    print('\033[91m' + 'ERROR: Virus detected')
    print('\033[91m' + 'ERROR: Could not open AVG Antivirus: insufficient permissions')
    sleep(1.5)
  if b ==  1:
    c = randint(300, 900)
    print('\033[93m' + 'Deleted ' + str(c) + ' files')
    sleep(0.75)
  else:
    print('\033[92m' + str(a))
    sleep(0.01)
