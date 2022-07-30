from operator import itemgetter
import discord
import pyrebase
from nextcord.ext import commands
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
from io import BytesIO
import numpy as np


fb = {
  "apiKey": "AIzaSyDagXCuaZL0WzQL6CaN6pYS7OQo0yakRrE",
  "authDomain": "loop-cd5b8.firebaseapp.com",
  "databaseURL": "https://loop-cd5b8-default-rtdb.firebaseio.com",
  "storageBucket": "loop-cd5b8.appspot.com",
    "serviceAccount": "sa.json"

}
firebase = pyrebase.initialize_app(fb)
db = firebase.database()


#ctx.author.id = ID_CTX
ID_CTX="502592316092186644"

rank = []
all_users = db.child("Usuarios").get()
for user in all_users.each():
    rank.append([user.key(), db.child("Usuarios").child(user.key()).child("xp").shallow().get().val()])

rank_r = sorted(rank, key=itemgetter(1), reverse=True)
aux = 1

for number in rank_r:
    db.child("Rank").child(number[0]).child("rk").set(aux)
    aux = aux + 1

if not db.child("Usuarios").child(ID_CTX).child("cor").shallow().get().val():
    db.child("Usuarios").child(ID_CTX).child("cor").set("#11998e")
    cor = "#11998e"
else:
    cor = db.child("Usuarios").child(ID_CTX).child("cor").shallow().get().val()
cor_b = "#fcfcfc"

#avatar_url = ctx.author.avatar.url
avatar_url = "https://i.pinimg.com/originals/e8/00/cb/e800cb2b0afd3f13c78d83850823ec05.jpg"
##################################################################################################

lv = db.child("Usuarios").child(ID_CTX).child("lv").shallow().get().val()
xp = db.child("Usuarios").child(ID_CTX).child("xp").shallow().get().val()
if (lv < 5):
    p_xp = (lv * 100)
else:
    p_xp = (lv * 100) * 2
c_0 = (360 * xp) / p_xp
rank = db.child("Rank").child(ID_CTX).child("rk").shallow().get().val()
##################################################################################################
#nome_ok = ctx.author.name
nome_ok = "KELVIN"

##################################################################################################

# criando o card
im = Image.new(mode="RGB", size=(1900, 702))

# desenha a barra lateral
w, h = 50, 702
shape = [(0, 0), (w, h)]
img1 = ImageDraw.Draw(im)
img1.rectangle(shape, fill=cor)

# salva o avatar em uma variavel pil
r = requests.get(avatar_url, allow_redirects=True)


avatar = Image.open(BytesIO(r.content)).convert("RGB")
img = avatar
npImage=np.array(img)
h1,w1=img.size
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,h1,w1],0,360,fill=255)
npAlpha=np.array(alpha)
npImage=np.dstack((npImage,npAlpha))
img2 =Image.fromarray(npImage)
img2.show()

# cria o fundo do avatar
img1.ellipse((110, 130, 550, 572), fill=cor)
img1.pieslice((110, 130, 550, 572), start=c_0, end=360, fill=cor_b)
im.paste(img2, (122, 145), mask=img2)



# cria texto com nome do user
font = ImageFont.truetype("Roboto-Medium.ttf", size=110)
img1.text((615, 230), nome_ok, font=font, fill=(255, 255, 255))

fontlv = ImageFont.FreeTypeFont("Roboto-Italic.ttf", size=60)
img1.text((1337, 37), "Level ", font=fontlv, fill=cor)
img1.text((1502, 37), str(lv), font=fontlv, fill=cor)

img1.text((1639, 37), "Rank ", font=fontlv, fill=cor)
img1.text((1788, 37), str(rank), font=fontlv, fill=cor)

img1.text((615, 360), "XP", font=fontlv, fill=cor_b)
img1.text((711, 360), (str(xp) + " / " + str(p_xp)), font=fontlv, fill=cor_b)

im.show()
with BytesIO() as image_binary:
    im.save(image_binary, 'PNG')
    image_binary.seek(0)
    #await ctx.send(file=discord.File(fp=image_binary, filename="card.png"))

