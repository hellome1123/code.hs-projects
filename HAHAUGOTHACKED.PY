import sys
import os
os.system("color 2")



print("Hack - ")

target = input()

print("Searching all known addresses for " + target )


print("                ")

print("Searching all Databases for " + target)

print("               ")

print("Searching all Servers for " + target)

print("          ")
print("......................")

print("One match found [INSTAGRAM]")

print("              ")

print("Proceed?")

Reply = input()

print("Proceeding ...")

print("Start attack  ")

reply = input()





def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


import time

for i in progressbar(range(35), "Attacking: ", 40):
    time.sleep(0.1)

print("Done")    

print("Files secured")   
reply = input()
print("      ")

print("Files saved to machine")

reply = input()
