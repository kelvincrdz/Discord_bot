import pyrebase
import random
from nextcord.ext import commands
import nextcord
from operator import itemgetter
import os
from translate import Translator
from PIL import Image, ImageDraw, ImageFont
import json
import foaas

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)

#banco de dados
fb = {
  "apiKey": "AIzaSyDagXCuaZL0WzQL6CaN6pYS7OQo0yakRrE",
  "authDomain": "loop-cd5b8.firebaseapp.com",
  "databaseURL": "https://loop-cd5b8-default-rtdb.firebaseio.com",
  "storageBucket": "loop-cd5b8.appspot.com",
    "serviceAccount": "sa.json"

}

#token
token = "ODcxODM1MTg0NTQxMDczNDA4.GpffV7.x1QvoMpmywP9xuBe84Rkl45wTONn1Jm7_xU40o"


firebase = pyrebase.initialize_app(fb)
db = firebase.database()


#On Ready Event.
@bot.listen()
async def on_ready():
  print("Bot Ready.")
  print("Logged In As:  {0.user}".format(bot))
  print('BOT ONLINE - Olá Mundo!')
  print(bot.user.name)
  print(bot.user.id)

def criar_user(id,xp,lv):
    db.child("Usuarios").child(id).child("xp").set(xp)
    db.child("Usuarios").child(id).child("lv").set(lv)

def update_xp(message, id, xp):
    xp_old = int(db.child("Usuarios").child(id).child("xp").shallow().get().val())
    lv_old = int(db.child("Usuarios").child(id).child("lv").shallow().get().val())

    if (lv_old<5):
        if ((lv_old*100)>=xp_old):
            xp_n = int(xp_old+xp)
            db.child("Usuarios").child(id).child("xp").set(xp_n)
            return (False)
        else:
            db.child("Usuarios").child(id).child("xp").set((xp_old + xp))
            db.child("Usuarios").child(id).child("lv").set((lv_old + 1))
            return (True)
    else:
        if ((lv_old*100)*2>xp_old):
            db.child("Usuarios").child(id).child("xp").set((xp_old+xp))
            return (False)
        else:
            db.child("Usuarios").child(id).child("xp").set((xp_old + xp))
            db.child("Usuarios").child(id).child("lv").set((lv_old + 1))
            return (True)

def msg_lvup():
    lvs = db.child("LvUp").get().val()
    lvs.remove(None)
    t = random.randint(1, len(lvs))
    res = db.child("LvUp").child(t).get().val()
    return res

@bot.event
async def on_message(message):
    if message.author.bot == False:
        if not db.child("Usuarios").child(message.author.id).shallow().get().val():
            xp= random.randint(1, 10)
            criar_user(message.author.id,xp, 1)
        else:
            xp = random.randint(1, 10)
            lv = update_xp(message, message.author.id, xp)
            if (lv == True):
                lv= db.child("Usuarios").child(message.author.id).child("lv").shallow().get().val()
                msg = str(msg_lvup())
                print(msg)
                msg = msg.replace('#', str(lv))
                a, b = msg.split("*")
                print(msg)
                await message.channel.send(a + f' {message.author.mention} '+b)
    await bot.process_commands(message)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send("Loaded cog!")

for fn in os.listdir("./cogs"):
       if fn.endswith(".py"):
           bot.load_extension(f"cogs.{fn[:-3]}")

bot.run(token)