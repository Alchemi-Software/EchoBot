import os

if os.path.exists("hooks.txt"):
    f = open("hooks.txt","a+")
    f.write(input("> "))
else:
    f = open("hooks.txt","w")
    f.write("\n"+input("> "))
f.close()
