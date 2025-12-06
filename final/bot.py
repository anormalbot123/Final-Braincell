import discord
from settings import *
from discord.ext import commands
from random import randint
import random
from logic import * 


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

    num_right = ans_list.index(rihgt_ans) + 1

    await ctx.send(quest)
    await ctx.send("Aqui las posibles respuestas:")

    message_list = ""

    for i in range(len(ans_list)):
        message_list += f"{i}) " + ans_list[i] + "\n"

    await ctx.send(message_list)


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel


    try:
        await ctx.send("listo para recibir tu respuesta")
        mssg = await bot.wait_for("message", timeout=30, check=check)

    except:
        await ctx.send("Se te acabo el tiempo")
        return
    

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
    choosen_one = random.choice(meme_list)

    with open(f'memes/{choosen_one}', 'rb') as f:

        # es File pq es una clase FFFFF

        picture = discord.File(f)
    
    await ctx.send(file=picture)


@bot.command()
async def facto(ctx):
    await ctx.send(random.choice(fact_list))




bot.run(settings["token"])

