from nextcord.ext import commands
from translate import Translator
import requests

import random

api_key = "973aNDUzMToxNTQyOkx6OE83Vm1NYTY1dk1RaHA"
template_id = "fb877b2b228783e4"


class Frases(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meajuda(self, ctx):
        response = requests.request("GET", "https://api.adviceslip.com/advice")
        img_url = response.json()
        translator = Translator(to_lang="pt-br")
        translation = translator.translate(img_url["slip"]["advice"])
        await ctx.send(translation)

    @commands.command()
    async def ship(self, ctx):
        msg = str(ctx.message.content)
        txt = msg.replace(".ship ", "")
        txt2=[]
        txt2 = txt.split("e")
        porc = random.randint(0,100)
        await ctx.send(f"{txt2[0]} e {txt2[1]} são *{porc}%* compativeis em")

        @commands.command()
        async def toxico(self, ctx):
            message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            #await ctx.send(message.content)
            await ctx.send(f"{txt2[0]} e {txt2[1]} são *{porc}%* compativeis em")

def setup(bot):
    bot.add_cog(Frases(bot))


