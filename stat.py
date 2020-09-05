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
try:
	uuid = "   UUiD: "+get("https://api.mojang.com/users/profiles/minecraft/"+sys.argv[1]).text.split('"id":"')[1].replace('"}',"")+"                       "
except:
	fore(244,44,10,"\n[!] "+sys.argv[1]+" is an offline name [!]\n")
	sys.exit()
fd = get("https://mc-heads.net/avatar/"+str(sys.argv[1])+"/1.png")
im = Image.open(io.BytesIO(fd.content))
pix = im.load()
width, height = im.size
px = list(im.getdata())
print ("\n")
color("a0")
print ()
back(255,255,255,"")
fore(255,50,255,"\n ╔═══════════════════════════════════════════════════════════╗\n")
fore(255,50,255," ║ ")
for i in range(0,8):sys.stdout.write(back(px[i][0],px[i][1],px[i][2],"  ").go+back(0,0,0,"").go)
back(255,255,255,"")
fore(255,50,255,"   MCStat By: ").go+fore(242, 117, 0,"@Masonrapa                 ").go+fore(255,50,255," ║").go
print ()
fore(255,50,255," ║ ")
for i in range(0,8):sys.stdout.write(back(px[i+8][0],px[i+8][1],px[i+8][2],"  ").go+back(0,0,0,"").go)
back(255,255,255,"")
fore(255,50,255,"                                          ║")
print ()
fore(255,50,255," ║ ")
for i in range(0,8):sys.stdout.write(back(px[i+16][0],px[i+16][1],px[i+16][2],"  ").go+back(0,0,0,"").go)
back(255,255,255,"")
variable = "   Name: "+sys.argv[1]+"                                     "
variable = variable[:42]+"║"
fore(255,50,255,variable)
print ()
fore(255,50,255," ║ ")
for i in range(0,8):sys.stdout.write(back(px[i+24][0],px[i+24][1],px[i+24][2],"  ").go+back(0,0,0,"").go)
back(255,255,255,"")
variable = uuid[:42]+"║"
fore(255,50,255,variable)
print ()
fore(255,50,255," ║ ")
for i in range(0,8):sys.stdout.write(back(px[i+32][0],px[i+32][1],px[i+32][2],"  ").go+back(0,0,0,"").go)
back(255,255,255,"")
rek = get("https://api.ashcon.app/mojang/v2/user/"+sys.argv[1]).text.split('"custom":')[1].split(",")[0].replace(" ","")
if rek == "true": variable = "   Skin: Yes (Custom)                       "
if rek == "false": variable = "   Skin: No (Steve)                        "
variable = variable[:42]+"║"
fore(255,50,255,variable)
print ()
fore(255,50,255," ║ ")
for i in range(0,8):sys.stdout.write(back(px[i+40][0],px[i+40][1],px[i+40][2],"  ").go+back(0,0,0,"").go)
back(255,255,255,"")
variable = "   Name Changes: "+str(len(get("https://api.mojang.com/user/profiles/"+get("https://api.mojang.com/users/profiles/minecraft/"+sys.argv[1]).text.split('"id":"')[1].replace('"}',"")+"/names").text.split("},{")))+"                               "
variable = variable[:42]+"║"
fore(255,50,255,variable)
print ()
fore(255,50,255," ║ ")
for i in range(0,8):sys.stdout.write(back(px[i+48][0],px[i+48][1],px[i+48][2],"  ").go+back(0,0,0,"").go)
back(255,255,255,"")
variable = "   Original Name: "+get("https://api.mojang.com/user/profiles/"+get("https://api.mojang.com/users/profiles/minecraft/"+sys.argv[1]).text.split('"id":"')[1].replace('"}',"")+"/names").text.split('"name":"')[1].split('"}')[0]+"                               "
variable = variable[:42]+"║"
fore(255,50,255,variable)
print ()
fore(255,50,255," ║ ")
for i in range(0,8):sys.stdout.write(back(px[i+56][0],px[i+56][1],px[i+56][2],"  ").go+back(0,0,0,"").go)
back(255,255,255,"")
rek = get("https://api.ashcon.app/mojang/v2/user/"+sys.argv[1]).text
if '"changed_at": "2020-' in rek:
	rek = rek.split('"changed_at": "2020-')[1].split('.000Z"')[0].replace("T"," ")
	variable = "   Active Acc: Yes (2020-"+rek+")                     "
else: variable = "   Active Acc: No                       "
variable = variable[:42]+"║"
fore(255,50,255,variable)
print (back(255,255,255,"\n ╚═══════════════════════════════════════════════════════════╝").go+"")
print()
