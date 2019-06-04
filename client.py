#
# Henry Samuelson 
# 
# June 2 2019 
#
# This is the main client for git message 


import subprocess
import requests
import os
import base64
from bs4 import BeautifulSoup

from contextlib import contextmanager
import sys, os

#Starting Messages
#print("            o8o      .   ooo        ooooo ")                                                           
#print("            `'    .o8   `88.       .888'           ")                                                 
#print(" .oooooooo oooo  .o888oo  888b     d'888   .ooooo.   .oooo.o  .oooo.o  .oooo.    .oooooooo  .ooooo.  ")
#print("888' `88b  `888    888    8 Y88. .P  888  d88' `88b d88(  '8 d88(  '8 `P  )88b  888' `88b  d88' `88b ")
#print("888   888   888    888    8  `888'   888  888ooo888 `'Y88b.  `'Y88b.   .oP'888  888   888  888ooo888 ")
#print("`88bod8P'   888    888 .  8    Y     888  888    .o o.  )88b o.  )88b d8(  888  `88bod8P'  888    .o ")
#print("`8oooooo.  o888o   '888' o8o        o888o `Y8bod8P' 8""888P' 8""888P' `Y888""8o     `8oooooo.`Y8bod8P' ")
#print("d'     YD                                                                       d'     YD            ")
#print("'Y88888P'                                                                       'Y88888P'            ")
os.system("cls")                       
print("")                                                                              
print("  ▄████  ██▓▄▄▄█████▓ ███▄ ▄███▓▓█████   ██████   ██████  ▄▄▄        ▄████ ▓█████") 
print(" ██▒ ▀█▒▓██▒▓  ██▒ ▓▒▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ▒██    ▒ ▒████▄     ██▒ ▀█▒▓█   ▀ ")
print("▒██░▄▄▄░▒██▒▒ ▓██░ ▒░▓██    ▓██░▒███   ░ ▓██▄   ░ ▓██▄   ▒██  ▀█▄  ▒██░▄▄▄░▒███   ")
print("░▓█  ██▓░██░░ ▓██▓ ░ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒  ▒   ██▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ")
print("░▒▓███▀▒░██░  ▒██▒ ░ ▒██▒   ░██▒░▒████▒▒██████▒▒▒██████▒▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒")
print(" ░▒   ▒ ░▓    ▒ ░░   ░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░")
print("  ░   ░  ▒ ░    ░    ░  ░      ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░")
print("░ ░   ░  ▒ ░  ░      ░      ░      ░   ░  ░  ░  ░  ░  ░    ░   ▒   ░ ░   ░    ░   ")
print("      ░  ░                  ░      ░  ░      ░        ░        ░  ░      ░    ░  ░")
print("")
print("'I don't want my name on this project' - Henry Samuelson 2019")
print("")
print("Connect to Sever (git repo):")


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout




noServer = True
client = requests.session()
ServerPath = ""
REPOPATH = ""

while noServer:
    repoPath  = str(input("(usr/repo)> "))
    if repoPath != "":
        r = client.get(str("https://github.com/" + repoPath))
        if r.status_code == 200:
            ServerPath = "https://github.com/" + repoPath
            REPOPATH = repoPath
            noServer = False

            #clone repo
            #with open(os.devnull, 'wb') as devnull:
            #    subprocess.check_call(['git clone ' + ServerPath], stdout=devnull, stderr=subprocess.STDOUT)
            command = "git clone " + ServerPath
            os.system(command)

            print("Connected To Server")
        else:
            print("Could Not Find Server Path: Exp: 'hsamuelson/gitMessage'")


messageClient = True
prompt = "(" + REPOPATH + ")>"
os.chdir(REPOPATH.split("/")[1])
url = "https://api.github.com/repos/" + REPOPATH + "/contents/chat.txt"

while messageClient:
    print("chat file")
    
    # load chat file
    #print(client.get(chatPath).text)
    a  = requests.get(url).json()
    b = base64.b64decode(a['content'])
    c = bytes(str(b), "utf-8").decode("unicode_escape")
    os.system("cls")
    print(c)
    msg = str(input(prompt))
    if msg != "":
        # save message to chat file
        with open("chat.txt", "a") as myfile:
            myfile.write(str(msg +  " \n"))

        #commit message to git
        

        os.system("git pull ")
        os.system("git commit * -m 'msg' ")
        os.system("git push")

    else:
        os.system("git pull")
