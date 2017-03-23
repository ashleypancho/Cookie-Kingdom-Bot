# -*- coding: utf-8 -*-
from random import randint

import discord
from discord.ext.commands import Bot

import urllib.request

playing = "Just Chatting | //help"
botgame = discord.Game(name=playing)

ckQuotes = ["cheesewoof: i'll sleep after this episode" ,
            "cheesewoof: Help me rachi wan kenobi you're my only hope",
            "hbic: darn one corn short of a clam chowder. isn't that the way life goes",
            "Forever_Banned: I've grown attached to the idea of having a siamese twin",
            "DawnofAshes: Gonna get DNA banned.",
            "nathanielsp3: Im saying the one thing id say i say. nathanielsp3: I said it.",
            "IAmTheCandyman: No T-Swizz? Have we no standards?",
            "hbic: there is a new skin treatment called donkey milk. it looks gross and facsinating",
            "Jiante: Rachi does have a nice ass, not gonna lie, it likes carrots",
            "Rachiface: I want my epitaph to say this. \"Not appreciating my puns was a grave mistake.\"",
            "cheesewolf: Tell me how my ass tastes, bobby flay"
            ]

mulaneyQuotes = ["Here’s how easy it was to get away with bank robbery back in the ‘30s… as long as you weren’t still there when the police arrived, you had a 99% change of getting away with it.",
                 "I bet whenever Trump has to make a decision, he asks himself, \"What would a cartoon rich person do?\"",
                 "Donald Trump is not just a rich man, he’s what a hobo imagines a rich man to be.",
                 "In terms of instant relief, canceling plans is like heroin.",
                 "It's 100% easier not to do things than to do them.",
                 "I have a lot of stories about being a kid because it was the last time I was interesting.",
                 "Excuse me, I'm homeless, I'm gay, I have AIDS, and I'm new in town.",
                 "Eat ass, suck a dick, and sell drugs."
                 ]

randQuotes = ["Friendship is like peeing your pants, everyone can see it but only you can feel the warmth.",
              "Love is like a fart. If you have to force it, it's probably shit.",
              "I'm a lot like JFK, once the car gets sticky, ladies tend to run with reckless abandon."
             ]


my_bot = Bot(command_prefix="//")
@my_bot.event
async def on_read():
    print("Client logged in")

# @my_bot.change_status(game=botgame)
# async def nothing()

@my_bot.command()
async def hello(*args):
    return await my_bot.say("Hello, world!")

@my_bot.command()
async def info(*args):
    help = "List of commands: " \
           "\nck: Returns a random quote from a Cookie Kingdom regular" \
           "\nfmk name1 name2 name3: Fuck, marry, kill" \
           "\nmulaney: Returns a random John Mulaney quote" \
           "\nrandom: Returns a random quote" \
           "\nxkcd [number]: Returns a random xkcd comic unless a number is specified."

    return await my_bot.say(help) #add this

@my_bot.command()
async def mulaney(*args):
    x = randint(0,len(mulaneyQuotes)-1)
    return await my_bot.say(mulaneyQuotes[x])

@my_bot.command()
async def random(*args):
    x = randint(0,len(randQuotes)-1)
    return await my_bot.say(randQuotes[x])

@my_bot.command()
async def fmk(*args):
    arr = []
    for x in args:
        arr.append(x)
    result = "";

    x = randint(0,2)
    result += "Fuck: " + arr[x]
    arr.remove(arr[x])

    x = randint(0,1)
    result += "\nMarry: " + arr[x]
    arr.remove(arr[x])

    result += "\nKill: " + arr[0]
    return await my_bot.say(result)

@my_bot.command()
async def ck(*args):
    x = randint(0,len(ckQuotes)-1)
    return await my_bot.say(ckQuotes[x])

@my_bot.command()
async def xkcd(*args):
    if len(args) != 0:
        url = "https://xkcd.com/" + args[0] + "/"
        html = urllib.request.urlopen(url)
        result = html.read()
    else:
        x = randint(0,1800)
        result = "https://xkcd.com/" + str(x) + "/"
    return await my_bot.say(result);

my_bot.run("MjcwNjE1MzMyNjY4ODMzODAy.C3aTbw.kN3EJGs3Vdw-EVdI825fICcc5Zw")


# Link to add to servers:
# https://discordapp.com/oauth2/authorize?client_id=270615332668833802&scope=bot&permissions=0
