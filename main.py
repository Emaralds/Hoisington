import time
import sys
import os
import random
from termcolor import colored, cprint
from getkey import getkey,keys
from mazes import *
# defineses delay print which prints charitors one at a time
def delay_print(s,speed=0.05 , color="white"):
	if speedrun and speed==0.05:speed=0
	for c in s:
		sys.stdout.write(colored(c,color))
		sys.stdout.flush()
		time.sleep(speed)
def clear():
	os.system("clear")
#defines many diffrent vairables
money=0
story=0
roomx=0
roomy=3
xpos=2
ypos=2
xblit=0
yblit=0
max_health=3
health=3
runery=10
style=96
oil=0
bombs=0
cp=[0,3,2,2]
darkness=False
doubleCost=False
debug=False
maze=master_maze[roomy][roomx]
room=maze[0].get_maze()
# definces the diffnt responces to naming yourself diffent things
name_responses={
	"Slick":["That's a pretty slick name you got there son","\nI have a friend who likes to call himself that"],
	"Evan":["I have a good friend who goes by that name, son","\nhe likes to call himself slick"],
	"Robert":["That is going to be a bad choice, son"],
	"Lincoln":["Wow you could have put in a better name, son","\nhow about Richard?"],
	"Richard":["Genshin impact sucks"],
	"Alexander":["I know you you","\nyour'e the one that made me"],
	"Hoisington":["THATS ME!","\nIt can't be!","\nNot again!"],
	"Bryan":["Nice!"],
	"Joshua":["Oh him, he owes me quite a bit of homework"],
	"Ethan":["You suck"],
	"Julia":["You're his sister arent you?"],
	"Debug":["I'm not gonna let you in that easy","\nyou're gonna need a passcode"],
	"Bug":["debug mode activated"],
	"Dark":["Very Spooky!"],
	"Sus":["SUS"],
	"James":["smol boi"],
	"Lion":["ROAR"]
}
speednames=["Speed","Speedrun","A","Zoom"]
speedrun=False
runner_start=0
inventory=[]
state="talking"
cursor_pos=0
past_rooms=[]
# hadles what happens if an error accurs
def on_error():
	global roomx,roomy,xpos,ypos,cp
	print("An error accured, SUS")
	if speedrun:print(time.time() -start)
	roomx=cp[0]
	roomy=cp[1]
	xpos=cp[2]
	ypos=cp[3]
	pass
# controls the actions the your key preses cause while in the maze
def on_press(key):
	global xblit,yblit,state
	if key in [keys.UP,"w"]:yblit-=1
	elif key in [keys.DOWN,"s"]:yblit+=1
	elif key in [keys.LEFT,"a"]:xblit-=1
	elif key in [keys.RIGHT,"d"]:xblit+=1
	if key == keys.ENTER:
		state="menu"
		print(menu())
	else:movement()
# controls the shop
def run_shop(shop,key):
	global money,inventory,oil,cursor_pos,bombs
	if key == keys.ESC:return draw_maze()
	if key == keys.ENTER:
		if cursor_pos==len(shop):
			cursor_pos=0
			return dr
		elif shop[cursor_pos][1]<=money and shop[cursor_pos][0] not in inventory:
			money -= shop[cursor_pos][1]
			if shop[cursor_pos][0]=="lamp oil":
				oil+=1
			elif shop[cursor_pos][0]=="3 bombs":
				bombs+=3
			else:inventory.append(shop[cursor_pos][0])
	clear()
	message="  $"+str(money)+"\n"
	for x in range(len(shop)):
		if x == cursor_pos:message+="\u279E "
		else:message+="  "
		if shop[x][0] not in inventory:message += shop[x][0].capitalize() +"   $"+str(shop[x][1])+"\n"
		else:message+="--Sold Out--\n"
	if cursor_pos==len(shop):message+="\u279E "
	else:message+="  "
	message+="Exit"
	return message
#handles the menu
def menu(key=None):
	global inventory,cursor_pos,past_rooms,roomx,roomy,xpos,ypos,style,oil,song,darkness,bombs,doubleCost,room,maze,health,max_health
	if oil>0 and "lantern" not in inventory:inventory.append("lantern")
	if bombs>0 and "bombs" not in inventory:inventory.append("bombs")
	if key == keys.ESC: return draw_maze()
	if key==keys.UP and cursor_pos>0:cursor_pos-=1
	elif key==keys.DOWN and cursor_pos<len(inventory):cursor_pos+=1
	elif key==keys.ENTER:
		if cursor_pos>=len(inventory):return draw_maze()
		elif inventory[cursor_pos]=="heart":
			max_health+=1
			health=max_health
		elif inventory[cursor_pos]=="dark":darkness=not darkness
		elif inventory[cursor_pos]=="double cost":doubleCost=not doubleCost
		elif inventory[cursor_pos]=="up":
			roomy-=1
		elif inventory[cursor_pos]=="right":roomx+=1
		elif inventory[cursor_pos]=="down":roomy+=1
		elif inventory[cursor_pos]=="left":roomx-=1
		elif inventory[cursor_pos]=="rope" and len(past_rooms)>0:
			loading_room=past_rooms.pop()
			roomx=loading_room[0]
			roomy=loading_room[1]
			xpos=loading_room[2]
			ypos=loading_room[3]
		elif inventory[cursor_pos]=="bombs":
			bombs-=1
			room=master_maze[roomy][roomx][0].get_maze()
			for x in range(xpos-1,xpos+2):
				if x>=0 and x<len(room[0]):
					for y in range(ypos-1,ypos+2):
						if (y>=0 and y<len(room)) and (room[y][x]==7 or room[y][x]==2):
							room[y][x]=0
			if bombs==1: maze.remove("bombs")
			return draw_maze("BOOM!")
				
		elif inventory[cursor_pos]=="nuke":
			room=master_maze[roomy][roomx][0].get_maze()
			for x in range(xpos-2,xpos+3):
				if x>=1 and x<len(room[0])-1:
					for y in range(ypos-2,ypos+3):
						if (y>=1 and y<len(room)-1) or ((y>=0 and y<len(room)-1) and (room[y][x]==7 or room[y][x]==2)):room[y][x]=0
			return draw_maze("BOOM!")
		elif "lantern" in inventory[cursor_pos]:
			if oil>0:	
				maze=master_maze[roomy][roomx]
				if "dark" in maze:maze.remove("dark")
				else:
					maze =maze[0].get_maze()
					for y in range(len(maze)):
						for x in range(len(maze[0])):
							if maze[y][x]==2:maze[y][x]=0
				oil-=1
			else:
				inventory.remove("lantern")
				return draw_maze("You don't have enough oil!")
		elif inventory[cursor_pos]=="shades":
			time.sleep(0.5)
			if style<=5:delay_print("You feel very slick in these")
			elif style<15:delay_print("You feel as if this joke is going to old soon")
			elif style==15:delay_print("You know what your gonna have to earn this")
			elif style==16:delay_print("You know what how about 100 points")
			elif style==17:delay_print("Then we will see who has the most syle")
			elif style==18:delay_print("You know what I'll even through in a little gift to help you")
			elif style==19:delay_print("It's a style point counter")
			elif style==20:delay_print("Do you like it?")
			elif style==21:delay_print("All right I'll leave you alone")
			elif style==90:delay_print("You're almost there!")
			elif style==91:delay_print("Took you long enough")
			elif style==92:delay_print("But I'm gonna have to have to stop you")
			elif style==93:delay_print("You can't have what lies ahead")
			elif style==94:delay_print("It if far too powerful for the likes of you")
			elif style==97:delay_print("I have to stop you")
			elif style==98:delay_print("STOP",2)
			elif style==99:
				# prints the wiki artical
				f=open("style.txt")
				delay_print(f.read(),0.008)
				f.close()
			elif style==100:
				delay_print("Wow I can't belive that you actually did it wow!")
				time.sleep(0.5)
				delay_print("\nwell I supose you deserve this")
				time.sleep(0.5)
				delay_print("\nyou got the nuke")
				style+=1
				# gives the nuke to the player
				inventory.append("nuke")
				return draw_maze()
			time.sleep(0.5)
			delay_print("\nYou got 1 style point!")
			style+=1
			time.sleep(1)
		return draw_maze()
	clear()
	# adds the bigginging of he menu including health,money,and style
	message="money: "+str(money)+"\nhealth:"+"❤️ "*health+"\n"
	if style >=20 and style!=101:message+="style: "+str(style)+"\n"
	
	n=0
	i=globals()
	if debug:
		for x in i:
			message+=str(x)+"     "+str(i[x])+"\n"
	for x in inventory:
		if n==cursor_pos:message+="\u279E "
		else:message+="  "
		message+= x.capitalize()
		if x=="lantern":message+="   "+str(oil)
		elif x=="bombs":message+="   "+str(bombs)
		message+="\n"
		n+=1
	if cursor_pos==len(inventory):message+="\u279E Exit"
	else:message+="  Exit"
	return message
# takes in the current maze and renders it
def draw_maze(message=""):
	global state
	state="maze"
	ylen=len(room)
	xlen=len(room[0])
	clear()
	display=""
	box=False
	for y in room:
		for x in y:
			if x in [-2,-4]:box=True
	dark="dark" in maze or darkness
	for y in range(ylen):
		for x in range(xlen):
			if (xpos==x and ypos==y) and (name=="Evan" or name == "Slick" or "shades"in inventory):display+="\U0001F60E"
			elif xpos==x and ypos==y:display+="\U0001F642"
			elif runery==y and x==2 and maze[0]==evan_room and "shades" not in inventory:display+="🏃"
			elif not dark or ((x<=xpos+1 and x>=xpos-1)and(y<=ypos+1 and y>=ypos-1)):
				# need to fix this part
				if room[y][x] == 3 and "money" in  master_maze[roomy][roomx]:display+="💰"
				elif room[y][x] == 4: display+="\u25B2\u25B2"
				elif room[y][x] == 5 and "cp" in master_maze[roomy][roomx]:display+="❤️ "
				elif room[y][x] == 6:display+='🤑'
				elif room[y][x] == 7 and "bombs" in inventory:display+='\u2593\u2593'
				elif room[y][x] == 8 and not windows:display+="🪙 "
				elif room[y][x] == 8:display+="💵"
				elif room[y][x] in [1,2,7]:display+="\u2588\u2588"
				elif room[y][x] in [-2,9]:display+="📦"
				elif room[y][x] ==10:display+="🔘"
				elif room[y][x]==-4:display+="✅"
				elif room[y][x]==11:display+="✉️ "
				else:display+="  "
			elif dark:display+="  "
		display+="\n"
	display+= message
	return display
# handeles play movmnt including colision and interactions with blocks
def movement():
	global xblit,yblit,xpos,ypos,roomy,roomx,runery,story,inventory,health,state,past_rooms,cp,money,room,maze,cursor_pos
	xtest=xpos
	ytest=ypos
	maze=master_maze[roomy][roomx]
	room=maze[0].get_maze()
	ylen=len(room)
	xlen=len(room[0])
	xtest+=xblit
	ytest+=yblit
	# moves the player between rooms
	if ytest<0 or ytest>ylen-1 or xtest<0 or xtest>xlen-1:
		past_rooms.append([roomx,roomy,xpos,ypos])
		dir = [ytest>ylen-1,xtest<0,ytest<0,xtest>xlen-1].index(True)
		runery=15
		if dir==2:roomy-=1
		elif dir==3:roomx+=1
		elif dir==0:roomy+=1
		elif dir==1:roomx-=1
		maze=master_maze[roomy][roomx]
		if not maze[0]:
			if dir==0:roomy-=1
			elif dir==1:roomx+=1
			elif dir==2:roomy+=1
			elif dir==3:roomx-=1
			maze=master_maze[roomy][roomx]
		room=maze[0].get_maze()
		exits=maze[0].get_exits()
		if dir in (0,2):
			xtest=exits[dir]
			ytest=(len(room)-1)*(dir//2)
		else:
			ytest=exits[dir]
			if dir == 1:xtest=len(room[0])-1
			else:xtest=0
		complete=True
		for y in room:
			for x in y:
				if x ==10:complete=False
		for y in range(len(room)):
			for x in range(len(room[0])):
				if room[y][x]==-1:room[y][x]=4
				elif room[y][x]==-2:room[y][x]=0
				elif room[y][x]==-3 and not complete:room[y][x]=9
				elif room[y][x]==-4 and not complete:room[y][x]=10
		xpos=xtest
		ypos=ytest
		if maze==evan_room:
			runner_start=time.perf_counter()
			runery=15
		print(draw_maze())
	elif room[ytest][xtest]==3 and "money" in master_maze[roomy][roomx]:
		money+=5
		xpos=xtest
		ypos=ytest
		print(draw_maze("You got 5 coins"))
		master_maze[roomy][roomx].remove("money")
	elif room[ytest][xtest]==4:
		health-=1
		if health<=0:
			#death
			time.sleep(1)
			delay_print("Oof that's gotta hurt")
			time.sleep(0.5)
			roomx=cp[0]
			roomy=cp[1]
			xpos=cp[2]
			ypos=cp[3]
			health=3
			maze=master_maze[roomy][roomx]
			room=maze[0].get_room()
			print(draw_maze("RIP"))
			time.sleep(1)
		else:
			#hurt
			xpos=xtest
			ypos=ytest
			room[ytest][xtest]=-1
			print(draw_maze("Ouch"))
	elif room[ytest][xtest]==5 and "cp" in master_maze[roomy][roomx]:
		health=max_health
		xpos=xtest
		ypos=ytest
		cp=[roomx,roomy,xpos,ypos]
		print(draw_maze(),"Health refilled")
	elif room[ytest][xtest]==6:
		global shop
		state="shop"
		shop=master_maze[roomy][roomx][1]
		if doubleCost:
			for x in shop:
				x[1]*=2
		cursor_pos=0
		delay_print("Lamp oil, rope, bombs you want it, it's your's my friend as long as you have enough coins",0.03)
		print(run_shop(shop,None))
	elif room[ytest][xtest]==8:
		money+=1
		xpos=xtest
		ypos=ytest
		print(draw_maze("You got a coin"))
		room[ytest][xtest]=0
	elif room[ytest][xtest] in [-2,9] and ytest+yblit>0 and ytest+yblit<len(room)-1 and xtest+xblit>0 and xtest+xblit<len(room[0])-1 and room[ytest+yblit][xtest+xblit] in[0,10,-3]:
		# handles BOX
		if room[ytest][xtest]==9:room[ytest][xtest]=-3
		else:
			room[ytest][xtest]=0
		if room[ytest+yblit][xtest+xblit] == 0:room[ytest+yblit][xtest+xblit]=-2
		elif room[ytest+yblit][xtest+xblit] == -3:room[ytest+yblit][xtest+xblit]=9
		else:
			room[ytest+yblit][xtest+xblit]=-3
			complete=True
			for y in room:
				for x in y:
					if x ==10:complete=False
			for y in range(len(room)):   
				for x in range(len(room[0])):
					if room[y][x] in (4,-1) and complete:
						room[y][x]=0
		xpos=xtest
		ypos=ytest
		print(draw_maze())
	elif room[ytest][xtest]==11:
		if(type(maze[1]))==list:message=maze[2]
		else:message=maze[1]
		delay_print(message,0.03)
	elif any(x==room[ytest][xtest] for x in (1,7,9,-2,10)):
		pass
	elif ytest<=runery and evan_room in maze and "shades" not in inventory:
		time.sleep(1)
		delay_print("Wow you caught up to me")
		time.sleep(0.5)
		delay_print("\nYou are very fast")
		time.sleep(0.5)
		delay_print("\nhere take these")
		time.sleep(0.5)
		delay_print("\nyou deserve them")
		time.sleep(1)
		story+=1
		inventory.append("shades")
		xpos=xtest
		ypos=ytest
		print(draw_maze(),"You got the slick shades")
	else:
		xpos=xtest
		ypos=ytest
		print(draw_maze())
	xblit=0
	yblit=0
# start of game
print("Do you see a coin?\n🪙\n(y/n)")
windows=True#input()
delay_print("\nHello I am Mr. Hoisington")
time.sleep(0.5)
delay_print('\nWelcome to my game')
time.sleep(0.5)
delay_print("\nWhat is your name? ")
name = input().capitalize()
time.sleep(0.5)
if name in name_responses.keys():
	for x in name_responses[name]:
		delay_print(x,0.05,"red")
		time.sleep(0.5)
	if name=="Sick":money+=10
	elif name=="Richard":money-=5
	elif name=="Dark":darkness=True
	elif name=="Bug":debug=True
	elif name=="Sus":
		f=open("NOTHING.txt")
		raise Exception("\n"+f.read())
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
delay_print("\nit is a simple maze")
time.sleep(0.5)
delay_print("\nwith many secrets in the walls to discover")
time.sleep(0.5)
delay_print("\nGood Luck")
time.sleep(1)
print(draw_maze())
if debug:
	money+=pow(2,64)
	bombs=pow(2,8)
	oil=pow(2,8)
	inventory.extend(["dark","double cost","up","right","down","left","heart"])
state="maze"
start=time.time()
# gameplay loop
while True:
	key = getkey()
	if state=="maze":
		try:
			on_press(key)
		except:
			on_error()
		i=0.1
		# moves the runner
		while runner_start+i<time.perf_counter():
			i+=0.25
			if runner_start+i>=time.perf_counter():
				runner_start=time.perf_counter()
			runery-=1
	elif state == "shop":
		# moves the cursor position in the shop
		if key == keys.UP and cursor_pos > 0:cursor_pos-=1
		elif key == keys.DOWN and cursor_pos < len(shop):cursor_pos+=1
		print_shop=run_shop(shop,key)
		if print_shop != None:print(print_shop)
	elif state == "menu":
		# sends key preses and calls run_shop
		print(menu(key))
