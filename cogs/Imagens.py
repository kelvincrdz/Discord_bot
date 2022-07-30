from nextcord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests
import discord

api_key = "973aNDUzMToxNTQyOkx6OE83Vm1NYTY1dk1RaHA"
template_id = "fb877b2b228783e4"

class Imagens(commands.Cog):
    def __init__(self, bot):
       self.bot = bot

    @commands.command()
    async def chicob(self, ctx):
        BG = Image.new(mode="RGB", size=(500, 602))
        img_url = ctx.message.attachments[0].url
        url = img_url
        r = requests.get(url, allow_redirects=True)
        meme = Image.open(BytesIO(r.content))
        meme_ok = meme.resize((154, 208), Image.ANTIALIAS)
        meme_ok2 = meme.resize((46, 60), Image.ANTIALIAS)
        Image.Image.paste(BG, meme_ok, (40, 51))
        Image.Image.paste(BG, meme_ok2, (32, 472))
        meme_l1 = "https://i.imgur.com/4kJBi7q.png"
        meme_r = requests.get(meme_l1, allow_redirects=True)
        l1 = Image.open(BytesIO(meme_r.content))
        bi = BG.convert("RGBA")
        fi = l1.convert("RGBA")
        bi.paste(fi, (0, 0), fi)
        with BytesIO() as image_binary:
            bi.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename="lixo.png"))

    @commands.command()
    async def monica(self, ctx):
        # Captura texto ou frase ".monica"

        if ctx.message.attachments:
            img_url = ctx.message.attachments[0].url
            txt=img_url
        else:
            txt1 = str(ctx.message.content)
            txt = txt1.replace(".monica", "")

        print(txt)
        # (<>width, ^height)
        BG = Image.new(mode="RGB", size=(601, 680))
        font = font = ImageFont.truetype("arial.ttf", size=35)
        if txt.find("http") != -1:
            url = txt
            r = requests.get(url, allow_redirects=True)
            meme = Image.open(BytesIO(r.content))
            meme_ok = meme.resize((381, 392), Image.ANTIALIAS)
            Image.Image.paste(BG, meme_ok, (220, 0))
        else:
            frase = ""
            cont = 1
            for i in txt:
                if i != " ":
                    frase = frase + i
                elif (cont < 3 and i == " "):
                    frase = frase + i
                    cont = cont + 1
                elif (cont == 3 and i == " "):
                    frase = frase + "\n"
                    cont = 1
            draw = ImageDraw.Draw(BG)
            draw.rectangle([(680, 392), (220, 0)], outline="white", fill="white")
            draw.text((430, 40), frase, fill="black", anchor="ms", font=font)
            # BG.show()
        meme_l1 = "https://i.imgur.com/FmJOA3J.png"  # MASCARA MEME
        meme_r = requests.get(meme_l1, allow_redirects=True)
        l1 = Image.open(BytesIO(meme_r.content))
        bi = BG.convert("RGBA")
        fi = l1.convert("RGBA")
        bi.paste(fi, (0, 0), fi)
        with BytesIO() as image_binary:
            bi.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename="monica.png"))

    @commands.command()
    async def catinho(self, ctx):
        url = "https://api.thecatapi.com/v1/images/search?format=json&limit=10"
        payload={}
        headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'fb1acec9-5448-4370-b0a2-40c368080534',

        }
        params = {
            'limit':'1',
            'size':'full'
            
        }
        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        img_url = response.json()
        print(img_url)
        respotas = img_url[0]
        await ctx.send(respotas['url'])


def setup(bot):
    bot.add_cog(Imagens(bot))
