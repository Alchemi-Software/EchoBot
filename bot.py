import discord
from discord.ext import commands
import asyncio
import requests
import os
from datetime import datetime
from getpass import getpass
from gmail import *

# Gmail address to send email from.
outaddress = "John doe <heck@gmail.com>"
outpassword = getpass("Alert email pwd: ")

# Any address to send to
toemail = "me@mydomain.com"

bot = commands.Bot(command_prefix='*', description="Echos user input to Webhooks")

def alert(ad,pwd,sad):
    e = GMail(ad,pwd)
    m = Message("Relay Doggo",to=sad,text="Seems the bot is shutting down.")
    e.send(m)

def get_urls():
    if not os.path.exists("hooks.txt"):
        return "None configured"
    else:
        f = open("hooks.txt")
        t = f.read()
        f.close()
        return t.split("\n")

def gettoken():
    if os.path.exists("token.txt"):
        f = open("token.txt")
        token = f.read()
        f.close()
        return token
    else:
        return "NONE"

def strstamp():
    return str(datetime.now())

def log(message):
    f = open("log.txt","a+")
    f.write("\n"+strstamp() +" : " + message)
    f.close()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("https://discordapp.com/oauth2/authorize?client_id=509832116050067457&scope=bot")
    print("------")
    log("Started")

@bot.command(description="Send to webhooks",pass_ctx=True)
async def echo(*,text:str):
    """Echo to list of webhooks"""
    urls = get_urls()
    answer = ""
    c = 0
    text = str(text)
    for url in urls:
        if url != "" and url != "\n" and url != " ":
            r = requests.post(url, data={"username":"Relay Doggo","avatar_url":"https://i.ytimg.com/vi/4PDQ1gziLL8/maxresdefault.jpg","content":text})
            answer += "\n" + r.text
            c += 1
    log("MSG: " + text)
    await bot.say("I sent `" + text + "` to " + str(c) + " url(s).")
    print("Sent `" + text + "` to " + str(c) + " url(s).")

@bot.command()
async def kys():
    log("Closing")
    alert(outaddress,outpassword,toemail)
    quit()

t = gettoken()
if t != "NONE":
    bot.run(t)
else:
    print("Token file not found.")
