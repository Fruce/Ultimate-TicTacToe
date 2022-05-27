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
O = PIL.Image.open(r'circle.png')
O = O.resize((150,150), Image.Resampling.LANCZOS)
O = ImageTk.PhotoImage(O)
#cross image
X = PIL.Image.open(r'cross.png')
X = X.resize((150,150), Image.Resampling.LANCZOS)
X = ImageTk.PhotoImage(X)
#square image
pinksquare = PIL.Image.open(r'pinksquare.png')
pinksquare = pinksquare.resize((335,200), Image.Resampling.LANCZOS)
pinksquare = ImageTk.PhotoImage(pinksquare)
#green square
bluesquare = PIL.Image.open(r'bluesquare.png')
bluesquare = bluesquare.resize((335,200), Image.Resampling.LANCZOS)
bluesquare = ImageTk.PhotoImage(bluesquare)
#big pink box
bbb = PIL.Image.open(r'pinksquare.png')
bbb = bbb.resize((1155,700), Image.Resampling.LANCZOS)
bbb = ImageTk.PhotoImage(bbb)
#big green box
bgb = PIL.Image.open(r'bluesquare.png')
bgb = bgb.resize((1155,700), Image.Resampling.LANCZOS)
bgb = ImageTk.PhotoImage(bgb)

# making and gridding the canvas
game_panel = Canvas(root,bg="#ffe6ff",height=460,width=460)
game_panel.pack()
#bigboxes
bigpinkbox = game_panel.create_image(-300,-85,anchor="nw",image=bbb,state='hidden')
bigbluebox = game_panel.create_image(-300,-85,anchor="nw",image=bgb,state='hidden')
#defining lbutt
lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1, 10)]) for x in range(1, 10)]).split(",")
#making the shapes which shows up when local box is won and square highlights
count=1
def shapes(x,y,shape):
    global count
    exec(f"{shape}{count} = game_panel.create_image({x},{y},anchor=\"nw\",image={shape},state=\'hidden\')",globals())
    count += 1
    if count - 1 == 9:
        count = 1
for i in range(-26,384,158):
    for j in range(-91, 226, 158):
        shapes(j,i,'bluesquare')
for i in range(-26,394,158):
    for j in range(-91, 226, 158):
        shapes(j,i,'pinksquare')
game_panel.create_image(-30,-30,anchor='nw',image=grid)
for i in range(0,311,155):
    for j in range(0,311,155):
        shapes(j,i,'O')
for i in range(0, 311, 155):
    for j in range(0, 311, 155):
        shapes(j, i, 'X')

#disable / enable buttons function
def disable(x,y = "bluesquare",c="#7ec7e6"):
    z = list(x)[-1]
    for i in lbutt:
        if "button" + z in i:
            exec(i + f"[\"bg\"] = \'{c}\'")
            exec(i + f"[\"activebackground\"] = \'{c}\'")
            exec(f'game_panel.itemconfig({y}' + z + ',state=\'normal\')')

        if "button" + z in i and i not in disabled:
            exec(i + "[\"state\"] = ACTIVE")

        elif "button" + z not in i:
            exec(i + "[\"state\"] = DISABLED")
            exec(i + "[\"bg\"] = \"#ffe6ff\"")
            exec(i + "[\"activebackground\"] = \"#ffe6ff\"")

def checkifdisabled(p,z='square',y='bigbluebox',c="#7ec7e6"):
    try:
        if all(elem in disabled for elem in [f"button{p}{q}" for q in range(1,10)]):
            for i in lbutt:
                if i not in disabled:
                    exec(f"{i}[\"state\"] = ACTIVE")
            c
            for i in lbutt:
                exec(i + f"[\"bg\"] = \'{c}\'")
                exec(i + f"[\"activebackground\"] = \'{c}\'")
                exec(f'game_panel.itemconfig({z}' + i[-2] + ',state=\'hidden\')')

            exec(f'game_panel.itemconfig({y},state=\'normal\')')
    except:
        pass

def local_win(x,y,z):
    global last_move
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
    if winrow or wincol or windiag1 or windiag2 == True:
        l_wins[int(x)] = last_move
        exec(f'game_panel.itemconfig({z}{x},state=\'normal\')')
        exec(f'game_panel.delete(\'win{x}\')')
        for i in lbutt:
            if "button"+x in i:
                exec(i+"[\'state\'] =  DISABLED")
                if i not in disabled:
                    disabled.append(i)

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

def hideboxes(box,x):
    print('hidebox: ',x)
    if box == 'blue':
        exec(f'game_panel.itemconfig(bluesquare{x},state=\'hidden\')')
        exec(f'game_panel.itemconfig(bigbluebox,state=\'hidden\')')
    else:
        exec(f'game_panel.itemconfig(pinksquare{x},state=\'hidden\')')
        exec(f'game_panel.itemconfig(bigpinkbox,state=\'hidden\')')

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
            temp = msg
            hideboxes('pink',msg[-2])
            disable(msg)
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
            local_win(msg[-2],moves[moves.index(last_move)-1],moves[moves.index(last_move)-1])
            checkifdisabled(msg[-1], "pinksquare")

        elif "lost" in msg:
            disableall()
            hideboxes('blue',temp[-1])
            messagebox.showinfo("GAME OVER","YOU LOST!!! YOU DUMB BASTARD\nLLLLLLL")

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
    disable(x, "pinksquare",'#c354f7')
    hideboxes('blue',x[-2])
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
    local_win(x[-2],last_move,last_move)
    checkifdisabled(x[-1], 'pinksquare', 'bigpinkbox','#c354f7')
    disableall()
    if global_win():
        disableall()
        print('global win: ',x)
        hideboxes('pink',x[-1])
        messagebox.showinfo("GAME OVER","YOU WON")

#making the buttons
for i in range(1, 10):
    for j in range(1, 10):
        exec(
     f"button{i}{j} = Button(text=\" \",font=\"Helvatica 14 bold\",padx=10,pady=2,width = 1,bg=\"#ffe6ff\",bd=0,"
        f"command=lambda :change(\"button{i}{j}\"),state = NORMAL)")

#screening buttons
count = 1
k=1
def make_grid(x, y):
    global count, k
    exec(f"win{k}{count} = game_panel.create_window({x},{y},anchor=\"nw\",window=button{k}{count},tags=\'win{k}\')")
    count += 1
    if count - 1 == 9:
        count = 1
        k += 1

for i in range(13,100,43):
    for j in range(15,100,42):
        make_grid(j,i)
for i in range(13,100,43):
    for j in range(170,255,42):
        make_grid(j,i)
for i in range(13,100,43):
    for j in range(325,429,42):
        make_grid(j,i)
for i in range(170,257,43):
    for j in range(15,100,42):
        make_grid(j,i)
for i in range(170,257,43):
    for j in range(170,255,42):
        make_grid(j,i)
for i in range(170,257,43):
    for j in range(325,429,42):
        make_grid(j,i)
for i in range(325,414,43):
    for j in range(15,100,42):
        make_grid(j,i)
for i in range(325,414,43):
    for j in range(170,255,42):
        make_grid(j,i)
for i in range(325,414,43):
    for j in range(325,429,42):
        make_grid(j,i)

root.mainloop()
