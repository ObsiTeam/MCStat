from PIL import Image
from lib import fore, back, color, reset,cls
from requests import get
import sys
import io
cls()
try:
	justtrying = sys.argv[1]
except:
	fore(244,44,10,"\nSorry, You need to run the script with python "+sys.argv[0]+" <name>\n")
	sys.exit()

fd = get("https://mc-heads.net/avatar/"+str(sys.argv[1])+"/1.png")
im = Image.open(io.BytesIO(fd.content))
pix = im.load()
width, height = im.size
px = list(im.getdata())
print ("\n")
color("0f")
mixes = [(0,1,2),(0,2,1),(2,1,0),(1,2,0),(1,0,2),(2,0,1)]
for mx in mixes:
	print ()
	print ()
	back(0,0,0,"")
	for i in range(0,8):sys.stdout.write(back(px[i][mx[0]],px[i][mx[1]],px[i][mx[2]],"  ").go+back(0,0,0,"").go)
	print ()
	for i in range(0,8):sys.stdout.write(back(px[i+8][mx[0]],px[i+8][mx[1]],px[i+8][mx[2]],"  ").go+back(0,0,0,"").go)
	print ()
	for i in range(0,8):sys.stdout.write(back(px[i+16][mx[0]],px[i+16][mx[1]],px[i+16][mx[2]],"  ").go+back(0,0,0,"").go)
	print ()
	for i in range(0,8):sys.stdout.write(back(px[i+24][mx[0]],px[i+24][mx[1]],px[i+24][mx[2]],"  ").go+back(0,0,0,"").go)
	print ()
	for i in range(0,8):sys.stdout.write(back(px[i+32][mx[0]],px[i+32][mx[1]],px[i+32][mx[2]],"  ").go+back(0,0,0,"").go)
	print ()
	for i in range(0,8):sys.stdout.write(back(px[i+40][mx[0]],px[i+40][mx[1]],px[i+40][mx[2]],"  ").go+back(0,0,0,"").go)
	print ()
	for i in range(0,8):sys.stdout.write(back(px[i+48][mx[0]],px[i+48][mx[1]],px[i+48][mx[2]],"  ").go+back(0,0,0,"").go)
	print ()
	for i in range(0,8):sys.stdout.write(back(px[i+56][mx[0]],px[i+56][mx[1]],px[i+56][mx[2]],"  ").go+back(0,0,0,"").go)
	print (back(0,0,0,"").go+"")
	print()
