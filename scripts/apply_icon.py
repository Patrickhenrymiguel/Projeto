import os, sys
from PIL import Image

src, root = sys.argv[1], sys.argv[2]
img = Image.open(src).convert("RGBA")
targets = [
 ("mipmap-mdpi",48),("mipmap-hdpi",72),("mipmap-xhdpi",96),
 ("mipmap-xxhdpi",144),("mipmap-xxxhdpi",192)
]
for folder,size in targets:
    d=os.path.join(root,"res",folder)
    if not os.path.isdir(d): continue
    for name in ("ic_launcher.png","icon.png","launcher.png"):
        p=os.path.join(d,name)
        if os.path.exists(p):
            img.resize((size,size),Image.LANCZOS).save(p)
