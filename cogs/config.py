import discord
import pyrebase
from nextcord.ext import commands
import random

fb = {
  "apiKey": "AIzaSyDagXCuaZL0WzQL6CaN6pYS7OQo0yakRrE",
  "authDomain": "loop-cd5b8.firebaseapp.com",
  "databaseURL": "https://loop-cd5b8-default-rtdb.firebaseio.com",
  "storageBucket": "loop-cd5b8.appspot.com",
    "serviceAccount": "sa.json"

}
firebase = pyrebase.initialize_app(fb)
db = firebase.database()

class config(commands.Cog):
    def __init__(self, bot):
       self.bot = bot

    @commands.command()
    async def cor(self, ctx):
        message = str(ctx.message.content)
        com, cor = message.split("#")
        message = ("#"+cor)
        db.child("Usuarios").child(ctx.author.id).child("cor").set(message)
        await ctx.send("sua cor foi alterada para "+message)
        
    def frase(self):
        frases_n = db.child("NewMwmber").get().val()
        frases_n.remove(None)
        t = random.randint(1, len(frases_n))
        res = db.child("LvUp").child(t).get().val()
        print(res)
        a , b = res.split("*")
        print(a, b)
        return (a, b)
    
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            a, b = frase()
            to_send = f"a {member.mention} b!"
            await guild.system_channel.send(to_send)
            

        
def setup(bot):
    bot.add_cog(config(bot))
