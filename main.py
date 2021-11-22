import time
import sys
from getkey import getkey,keys
from mazes import *
def delay_print(s,speed=0.05):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(speed)
money=0
place="start"
roomx=0
roomy=1
xpos=3
ypos=3
xblit=0
yblit=0
speednames=["Speed","Speedrun","A","Zoom"]
speedrun=False
def on_press(key):
	global xblit,yblit
	if key == "up":yblit-=1
	elif key =="down":yblit+=1
	elif key == "left":xblit-=1
	elif key == "right":xblit+=1
	movement()

def draw_maze(roomy,roomx,xpos,ypos):
	maze=master_maze[roomy][roomx]
	room=maze.get_maze()
	ylen=len(room)
	xlen=len(room[0])
	display="\n"*10
	for y in range(ylen):
		for x in range(xlen):
			if (xpos==x and ypos==y) and (name=="Evan" or name == "Slick"):display+="\U0001F60E"
			elif xpos==x and ypos==y:display+="\U0001F642"
			elif room[y][x] == 0:display+="  "
			elif room[y][x] == 1 or room[y][x] == 2:display+="\u2588\u2588"
		display+="\n"
	return display
def movement():
	global xblit,yblit,xpos,ypos,roomy,roomx
	xtest=xpos
	ytest=ypos
	room=master_maze[roomy][roomx].get_maze()
	ylen=len(room)
	xlen=len(room[0])
	xtest+=xblit
	ytest+=yblit
	xblit=0
	yblit=0
	if ytest<0:
		roomy-=1
		maze=master_maze[roomy][roomx]
		room=maze.get_maze()
		exits=maze.get_exits()
		new_ylen=len(room)
		new_xlen=len(room[0])
		ytest=new_ylen-1
		xtest=exits[2]
		print(draw_maze(roomy,roomx,xpos,ypos))
		xpos = xtest
		ypos=ytest
		print(draw_maze(roomy,roomx,xpos,ypos))
	elif ytest>ylen-1:
		roomy+=1
		room=master_maze[roomy][roomx].get_maze()
		new_ylen=len(room)
		new_xlen=len(room[0])
		ytest=0
		xtest=exits[0]
		xpos = xtest
		ypos=ytest
		print(draw_maze(roomy,roomx,xpos,ypos))
	elif xtest<0:
		roomx-=1
		room=master_maze[roomy][roomx].get_maze()
		new_ylen=len(room)
		new_xlen=len(room[0])
		ytest=exits[1]
		xtest=new_xlen-1
		xpos = xtest
		ypos=ytest
		print(draw_maze(roomy,roomx,xpos,ypos))
	elif xtest>xlen-1:
		roomx+=1
		room=master_maze[roomy][roomx].get_maze()
		new_ylen=len(room)
		new_xlen=len(room[0])
		ytest=exits[3]
		xtest=0
		xpos = xtest
		ypos=ytest
		print(draw_maze(roomy,roomx,xpos,ypos))
	elif room[ytest][xtest]==1:
		exit
	else:
		xpos = xtest
		ypos=ytest
		print(draw_maze(roomy,roomx,xpos,ypos))

delay_print("Hello I am Mr. Hoisington")
time.sleep(0.5)
delay_print('\nWelcome to my game')
time.sleep(0.5)
delay_print("\nWhat is your name? ")
name = input().capitalize()
time.sleep(0.5)
if name =="Slick":
    money+=10
    delay_print("That's a pretty slick name you got there son")
    time.sleep(0.5)
    delay_print("\nI have a friend who likes to call himself that")
elif name=="Evan":
	delay_print("I have a good friend who goes by that name, son")
	time.sleep(0.5)
	delay_print("\nhe likes to call himself slick")
elif name=="Robert":
	delay_print("That is going to be a bad choice, son")
elif name == "Lincoln":
	delay_print("Wow you could have put in a better name, son")
	time.sleep(0.5)
	delay_print("\nhow about Richard?")
elif name == "Richard":
	delay_print("Genshin impact sucks")
	print("\nYou lost 10 money")
	money-=10
	delay_print("You should try Lincoln")
elif name == "Alex" or name == "Alexander":
	delay_print("I know you.")
	time.sleep(0.5)
	delay_print("\nYou're the one that created me")
	time.sleep(0.5)
elif "Hoisington" in name:
	delay_print("THATS ME!",0.5)
	time.sleep(0.5)
	delay_print("\nIt can't be!",0.5)
	time.sleep(0.5)
	delay_print("\nNot again!",0.5)
	time.sleep(0.5)
elif name=="Bryan":
	delay_print("Nice!")
elif name=="Joshua":
	delay_print("Oh him, he owes he quite a few quizes")
elif name=="Ethan":
	delay_print("You suck")
elif name=="Josh":
	delay_print("It's spelled Joshua")
	name=="Joshua"
elif name=="Julia":
	delay_print("Your'e his sister are you, daughter")
elif name in speednames:
	print("speedrun acivated")
	speedrun=True
else:
  delay_print("Hmm "+name+" that is an interesting name you got there son")
  time.sleep(0.5)
  delay_print("\nI used to have an old friend with that name")
time.sleep(0.5)
delay_print("\nbut that is a story for another time.")
time.sleep(0.5)
delay_print("\nAnyway let's play a game son")
time.sleep(0.5)
delay_print("\nit is a simple maze\n")
time.sleep(2)
print(draw_maze(roomy,roomx,xpos,ypos))
while True:
	key = getkey()
	if key == keys.UP:on_press("up")
	elif key == keys.DOWN:on_press("down")
	elif key == keys.RIGHT:on_press("right")
	elif key == keys.LEFT:on_press("left")