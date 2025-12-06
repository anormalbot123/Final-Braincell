import discord
from settings import *
from discord.ext import commands
from random import randint
import random
from logic import * 
import os


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings["prefix"], intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command()
async def quiz(ctx):
    max = len(list_questions) - 1
    ind = randint(0, max)

    quest = get_question(ind)
    ans_list = get_answers(ind)
    rihgt_ans = get_right_ans(ind)

    num_right = ans_list.index(rihgt_ans)

    await ctx.send(quest)
    await ctx.send("Aqui las posibles respuestas:")

    for i in range(len(ans_list)):
        await ctx.send(f"{i + 1}) {ans_list[i]}")

    # mssg es un objecto, para el contenido seria 
    # mssg.content

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        await ctx.send("listo para recibir tu respuesta")
        mssg = await bot.wait_for("message", timeout=30, check=check)

    except:
        await ctx.send("Se te acabo el tiempo")
        return
    

    #verificar respuesta
    try: 
        user_ans = int(mssg.content)

    except:
        await ctx.send("hubo un error")
        return


    if user_ans == num_right:
        await ctx.send("asi es!")
        
    else:
        await ctx.send("mejor suerte para la proxima")

    return


@bot.command()
async def meme(ctx):
    with open(f'memes/{random.choice(meme_list)}', 'rb') as f:
        picture = discord.file(f)
    
    await ctx.send(file=picture)


bot.run(settings["token"])