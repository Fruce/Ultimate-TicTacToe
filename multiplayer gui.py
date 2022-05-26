from tkinter import *
from PIL import ImageTk, Image
import PIL.Image
from tkinter import messagebox
import socket
import threading

root = Tk()
c = socket.socket()
c.connect(('localhost', 9999))

#grid image
grid = PIL.Image.open(r"ttt.png")
grid = grid.resize((520,520), Image.Resampling.LANCZOS)
grid = ImageTk.PhotoImage(grid)
#circle image
circle = PIL.Image.open(r'circle.png')
circle = circle.resize((150,150), Image.Resampling.LANCZOS)
circle = ImageTk.PhotoImage(circle)
#cross image
cross = PIL.Image.open(r'cross.png')
cross = cross.resize((150,150), Image.Resampling.LANCZOS)
cross = ImageTk.PhotoImage(cross)

# making and gridding the canvas
game_panel = Canvas(root,bg="#ffe6ff",height=520,width=520)
game_panel.pack()
#grid
game_panel.create_image(0,0,anchor='nw',image=grid)
#defining lbutt
lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1, 10)]) for x in range(1, 10)]).split(",")
#making the shapes which shows up when local box is won
count=1
def shapes(x,y,shape):
    global count
    exec(f"{shape}{count} = game_panel.create_image({x},{y},anchor=\"nw\",image={shape},state=\'hidden\')",globals())
    count += 1
    if count - 1 == 9:
        count = 1
for i in range(30,341,155):
    for j in range(30,341,155):
        shapes(j,i,'circle')
for i in range(30, 341, 155):
    for j in range(30, 341, 155):
        shapes(j, i, 'cross')


#disable / enable buttons function
def disable(x):
    z = list(x)[-1]
    for i in lbutt:
        if "button" + z in i:
            exec('game_panel.itemconfig(cross'+z+',state=\'normal\')')
        if "button" + z in i and i not in disabled:
            exec(i + "[\"state\"] = ACTIVE")

        elif "button" + z not in i:
            exec(i + "[\"state\"] = DISABLED")
            exec(i + "[\"bg\"] = \"white\"")
            exec(i + "[\"activebackground\"] = \"white\"")
            

def checkifdisabled(p):
    try:
        if all(elem in disabled for elem in [f"button{p}{q}" for q in range(1,10)]):
            for i in lbutt:
                if i not in disabled:
                    exec(f"{i}[\"state\"] = ACTIVE")
            for j in lbutt:
                exec(j + "[\"bg\"] = \"#7ec7e6\"")
                exec(j + "[\"activebackground\"] = \"#7ec7e6\"")
    except:
        pass

def local_win(x,y):
    for i in range(1,8,3):
        winrow = True
        for j in range(i,i+3):
            if dic["button"+x+str(j)] != y:
                winrow = False
                break
        if winrow:
            break

    for i in range(1,4):
        wincol = True
        for j in range(i,i+7,3):
            if dic["button"+x+str(j)] != y:
                wincol = False
                break
        if wincol:
            break
    windiag1 = True
    for i in range(1,10,4):
        if dic["button"+x+str(i)] != y:
            windiag1 = False
            break
    windiag2 = True
    for i in range(3,8,2):
        if dic["button"+x+str(i)] != y:
            windiag2 = False
            break
    return winrow or wincol or windiag1 or windiag2

def global_win():
    winrow = False
    wincol = False
    windiag1 = False
    windiag2 = False
    for i in range(1,10,3):
        if l_wins[i] == l_wins[i+1] == l_wins[i+2] != "":
            winrow = True
            break
    for i in range(1,4):
        if l_wins[i] == l_wins[i+3] == l_wins[i+6] != "":
            wincol = True
            break
    if l_wins[1] == l_wins[5] == l_wins[9] != "":
        windiag1 = True
    if l_wins[3] == l_wins[5] == l_wins[7] != "":
        windiag2 = True
    if winrow or wincol or windiag1 or windiag2 is True:
        c.send(bytes('lost', "utf-8"))
    return winrow or wincol or windiag1 or windiag2

def listen():
    global last_move
    while True:
        msg = c.recv(2048).decode()
        print(msg)
        if msg == "X":
            last_move = "X"
        elif msg == "O":
            last_move = "O"
        elif "button" in msg:
            disable(msg)
            checkifdisabled(msg[-1])
            if last_move == "O":
                exec(msg + "[\"text\"] = \"X\"")
                exec(msg + "[\"state\"] = DISABLED")
                disabled.append(msg)
                dic[msg] = "X"
            elif last_move == "X":
                exec(msg + "[\"text\"] = \"O\"")
                exec(msg + "[\"state\"] = DISABLED")
                disabled.append(msg)
                dic[msg] = "O"
            if local_win(msg[-2],moves[moves.index(last_move)-1]):
                for i in lbutt:
                    if "button"+msg[-2] in i:
                        exec(i + "[\"bg\"] = \"#eb6e8b\"")
                        exec(i + "[\"activebackground\"] = \"#eb6e8b\"")
                        exec(i+"[\'state\'] =  DISABLED")
                        if i not in disabled:
                            disabled.append(i)
        elif "lost" in msg:
            disableall()
            messagebox.info("GAME OVER","YOU LOST!!! YOU DUMB BASTARD\nLLLLLLL")

def disableall():
    for i in lbutt:
        exec(f"{i}[\"state\"] = DISABLED")

t = threading.Thread(target=listen)
t.start()
last_move = "O"
dic = dict(map(lambda e: (e, " "), lbutt))
disabled = []
l_wins={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
moves = ["X","O"]
#defining change
def change(x):
    global last_move
    c.send(bytes(x, "utf-8"))
    disable(x)
    if last_move == "O":
        exec(x + "[\"text\"] = \"X\"")
        exec(x + "[\"state\"] = DISABLED")
        disabled.append(x)
        dic[x] = "X"
        last_move = "X"
        c.send(bytes("X", "utf-8"))
    else:
        exec(x + "[\"text\"] = \"O\"")
        exec(x + "[\"state\"] = DISABLED")
        disabled.append(x)
        dic[x] = "O"
        last_move = "O"
        c.send(bytes("O", "utf-8"))
    disableall()
    if local_win(x[-2],last_move):
        for i in lbutt:
            if "button"+x[-2] in i:
                exec(i + "[\"bg\"] = \"#6bff81\"")
                exec(i + "[\"activebackground\"] = \"#6bff81\"")
                exec(i+"[\'state\'] =  DISABLED")
                if i not in disabled:
                    disabled.append(i)
        l_wins[int(x[-2])] = last_move
        if global_win():
            disableall()
            messagebox.showinfo("GAME OVER","YOU WON")

#making the buttons
for i in range(1, 10):
    for j in range(1, 10):
        exec(
     f"button{i}{j} = Button(text=\" \",font=\"Helvatica 14 bold\",padx=10,pady=2,width = 1,bg=\"white\",bd=1,"
        f"command=lambda :change(\"button{i}{j}\"),state = NORMAL)")

#screening buttons
count = 1
k=1
def make_grid(x, y):
    global count, k
    exec(f"win{str(count)} = game_panel.create_window({x},{y},anchor=\"nw\",window=button{k}{count})")
    count += 1
    if count - 1 == 9:
        count = 1
        k += 1

for i in range(43,130,43):
    for j in range(40,131,45):
        make_grid(j,i)
    for j in range(195,286,45):
        make_grid(j,i)
    for j in range(350,441,45):
        make_grid(j,i)

for i in range(200,287,43):
    for j in range(40,131,45):
        make_grid(j,i)
    for j in range(195,286,45):
        make_grid(j,i)
    for j in range(350,441,45):
        make_grid(j,i)

for i in range(355,444,43):
    for j in range(40,131,45):
        make_grid(j,i)
    for j in range(195,286,45):
        make_grid(j,i)
    for j in range(350,441,45):
        make_grid(j,i)


root.mainloop()
