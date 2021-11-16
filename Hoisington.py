import time
import sys
import keyboard
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
money=0
place="start"
roomx=0
roomy=1
xpos=2
ypos=2
class maze:
    def __init__(self,layout):
        self.layout=layout
    def get_maze(self):
        return self.layout
start=maze([
    [1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1],
    [1,1,0,0,0,1,1],
    [1,1,0,0,0,1,1],
    [1,1,0,0,0,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1]])
maze1=maze([
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,0,0,0,1,1],
    [1,1,0,0,0,0,0],
    [1,1,0,0,0,1,1],
    [1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1]])
maze2=maze([
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]])
list=[]
for x in range(10):
    list.append([0,0,0,0,0,0,0,0,0,0])
print(list)
master_maze=[
    [maze1],
    [start]]
def display_maze(roomx,roomy,xpos,ypos):
    maze[roomy][roomx][ypos][xpos]

delay_print("\nHello I am Mr. Hoisington")
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
	delay_print("THATS ME!")
	time.sleep(0.5)
	delay_print("\nIt can't be!")
	time.sleep(0.5)
	delay_print("\nNot again!")
	time.sleep(0.5)
else:
  delay_print("Hmm "+name+" that is an interesting name you got there son")
  time.sleep(0.5)
  delay_print("\nI used to have an old friend with that name")
time.sleep(0.5)
delay_print("\nbut that is a story for another time.")
time.sleep(0.5)
delay_print("\nAnyway let's play a game son")
time.sleep(0.5)
delay_print("it is a simple maze")
while True:
    print(sys.stdin)