import discord
from settings import *
from discord.ext import commands
from random import randint
import random
from logic import * 
from googletrans import Translator


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings["prefix"], intents=intents, help_command=None)

translator = Translator()

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}\n-------------------')


@bot.command()
async def quiz(ctx):
    max = len(list_questions) - 1
    ind = randint(0, max)

    quest = get_question(ind)
    ans_list = get_answers(ind)
    rihgt_ans = get_right_ans(ind)

    num_right = ans_list.index(rihgt_ans) + 1

    await ctx.send(quest)

    message_list = ""

    for i in range(len(ans_list)):
        message_list += f"{i + 1}) " + ans_list[i] + "\n"

    await ctx.send(message_list)


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel


    try:
        await ctx.send("Listo para recibir tu respuesta, tienes 30 segundos para pensar")
        mssg = await bot.wait_for("message", timeout=30, check=check)

    except:
        await ctx.send("Se te acabo el tiempo")
        return
    

    try: 
        user_ans = int(mssg.content)

    except:
        await ctx.send("Por favor ingrese un numero dentre el 1 y el 4")
        return
    

    if user_ans == num_right:
        await ctx.send("Asi es!")
        
    else:
        await ctx.send("Mejor suerte para la proxima.")

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


@bot.command()
async def weather(ctx, city=None):
    if city == None:
        await ctx.send("Por favor indique una ciudad o lugar")
        return 

    url = f'https://wttr.in/{city}?format=%C+%t'
    ans = requests.get(url)
    str_ans = ""

    if ans.status_code == 200:
        str_ans = ans.text.strip()
        untranslated = str_ans
        
        try:
            tranlated_t = await translator.translate(str_ans, src='en', dest='es')
            str_ans = tranlated_t.text

        except:
            str_ans = ans.text.strip()

        await ctx.send(f"La temperatura actual de {city} es: {str_ans}")

    else:
        await ctx.send("Perdon pero hubo un error fuera de mis limites")
        return
    

    engine = pyttsx3.init()

    engine.save_to_file(untranslated, "mp3/weather.mp3")
    engine.runAndWait()
    engine.stop()


    with open("mp3/weather.mp3", "rb") as f:
        sound = discord.File(f)

    await ctx.send(file=sound)
    

@bot.command()
async def help(ctx):
    await ctx.send("Bienvenido! -------------\n" \
                    " - !quiz: el bot te lanza una pregunta y tienes que responder con la respuesta, tienes 30 segundos para responder\n" \
                    " - !facto: tira un dato curioso\n" \
                    " - !weather (cualquier lugar del mundo): te dira el clima del lugar indicado ademas que enviara un audio sobre dicho clima\n" \
                    " - !meme: enviara un meme aleatorio")

bot.run(settings["token"])  

