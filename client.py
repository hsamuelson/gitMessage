#
# Henry Samuelson 
# 
# June 2 2019 
#
# This is the main client for git message 

import requests
import os
from bs4 import BeautifulSoup

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
            command = "git clone" + ServerPath
            os.system(command)

            print("Connected To Server")
        else:
            print("Could Not Find Server Path: Exp: 'hsamuelson/gitMessage'")


messageClient = True
prompt = "(" + REPOPATH + ")>"
chatPath = str(ServerPath + "chat.txt")


while messageClient:
    client.get(chatPath)
    msg = str(input(prompt))

    # save message to chat file
    with open("chat.txt", "a") as myfile:
        myfile.write(msg)

    #commit message to git
    os.system("git pull")
    os.system("git commit *")
    os.system("git push")


