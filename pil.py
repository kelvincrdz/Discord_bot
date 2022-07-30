import numpy as np
from PIL import Image, ImageDraw
import requests
from io import BytesIO

avatar_url = "https://i.pinimg.com/originals/e8/00/cb/e800cb2b0afd3f13c78d83850823ec05.jpg"
url = avatar_url
r = requests.get(url, allow_redirects=True)

avatar = Image.open(BytesIO(r.content)).convert("RGB")
img = avatar
npImage=np.array(img)
h,w=img.size
# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,h,w],0,360,fill=255)
npAlpha=np.array(alpha)
npImage=np.dstack((npImage,npAlpha))
Image.fromarray(npImage).save('result.png')
img2 =Image.fromarray(npImage)
img2.show()
