from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import PIL.Image
from tkinter import messagebox
import socket
import threading
from threading import Thread

root = Tk()
root.geometry("900x640")
root.configure(bg='black')

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
#big blue box
bgb = PIL.Image.open(r'bluesquare.png')
bgb = bgb.resize((1155,700), Image.Resampling.LANCZOS)
bgb = ImageTk.PhotoImage(bgb)
#mcbg
mcbg = PIL.Image.open(r'mcbg.jpg')
mcbg = mcbg.resize((900,640), Image.Resampling.LANCZOS)
mcbg = ImageTk.PhotoImage(mcbg)
#smol button
btn = PIL.Image.open(r'button.png')
btn = btn.resize((300,210), Image.Resampling.LANCZOS)
btn = ImageTk.PhotoImage(btn)
#big button
bigbtn = PIL.Image.open(r'bigbutt.png')
bigbtn = bigbtn.resize((330,240), Image.Resampling.LANCZOS)
bigbtn = ImageTk.PhotoImage(bigbtn)
#gamescreen bg
gcbg = PIL.Image.open(r'gcbg.png')
gcbg = gcbg.resize((900,640), Image.Resampling.LANCZOS)
gcbg = ImageTk.PhotoImage(gcbg)


#creating mainscreen
mainscreen = Canvas(root,bg='black',width=900,height=640,highlightthickness=0)
mainscreen.pack()
hi = mainscreen.create_image(0,0,anchor='nw',image=mcbg,tags='lmao')

#creating gamescreen
game_screen = Canvas(root, width=900, height=640,highlightthickness=0)
game_screen.create_image(0,0,anchor='nw',image=gcbg)
running = False

def multiplayer():

    game_screen.pack()
    global count,game_panel,k,last_move,bigbluebox,bigpinkbox,running,hello
    #global change
    running = True

    c = socket.socket()
    c.connect(('localhost', 9999))

    # making and gridding the canvas
    game_panel = Canvas(game_screen,bg="#A18F80", height=460, width=460,highlightthickness=0)
    game_screen.create_line(215,18,685,18,fill="#210101",width=6)
    game_screen.create_line(215, 18, 214, 492, fill="#210101", width=6)
    game_screen.create_line(215, 492, 685, 492, fill="#210101", width=6)
    game_screen.create_line(685, 18, 685, 492, fill="#210101", width=6)
    game_screen.create_window(450,255,anchor='center',window=game_panel)

    bigpinkbox = game_panel.create_image(-300, -85, anchor="nw", image=bbb, state='hidden')
    bigbluebox = game_panel.create_image(-300, -85, anchor="nw", image=bgb, state='hidden')
    lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1, 10)]) for x in range(1, 10)]).split(",")

    # making the shapes which shows up when local box is won and square highlights
    count = 1

    def shapes(x, y, shape):
        global count
        exec(f"{shape}{count} = game_panel.create_image({x},{y},anchor=\"nw\",image={shape},state=\'hidden\')",
             globals())
        count += 1
        if count - 1 == 9:
            count = 1

    for i in range(-26, 384, 158):
        for j in range(-91, 226, 158):
            shapes(j, i, 'bluesquare')
    for i in range(-26, 394, 158):
        for j in range(-91, 226, 158):
            shapes(j, i, 'pinksquare')
    game_panel.create_image(-30, -30, anchor='nw', image=grid)
    for i in range(0, 311, 155):
        for j in range(0, 311, 155):
            shapes(j, i, 'O')
    for i in range(0, 311, 155):
        for j in range(0, 311, 155):
            shapes(j, i, 'X')




    # disable / enable buttons function
    def disable(x, y="bluesquare", c="#7ec7e6"):
        #j = 0
        z = list(x)[-1]
        for i in lbutt:
            if "button" + z in i:
                exec(i + f"[\"bg\"] = \'{c}\'")
                #exec(i + f"[\"activebackground\"] = \'{c}\'")
                exec(f'game_panel.itemconfig({y}' + z + ',state=\'normal\')')

            if "button" + z in i and i not in disabled:
                calling(i,z) #check line 345
                # exec(i + f".bind('<Button-1>',lambda change(\'button{z}{j}\')))")
                # j += 1
                # if j == 10:
                #     j = 1

            elif "button" + z not in i:
                exec(i + ".unbind(\'<Button-1>\')")
                exec(i + "[\"bg\"] = \"#A18F80\"")
                #exec(i + "[\"activebackground\"] = \"#A18F80\"")

    def checkifdisabled(p, y='bigbluebox', c="#7ec7e6"):
        try:
            if all(elem in disabled for elem in [f"button{p}{q}" for q in range(1, 10)]):
                for i in lbutt:
                    if i not in disabled:
                        exec(f"{i}[\"state\"] = ACTIVE")
                c
                for i in lbutt:
                    exec(i + f"[\"bg\"] = \'{c}\'")
                    exec(i + f"[\"activebackground\"] = \'{c}\'")
                    exec(f'game_panel.itemconfig(pinksquare' + i[-2] + ',state=\'hidden\')')
                    exec(f'game_panel.itemconfig(bluesquare' + i[-2] + ',state=\'hidden\')')

                exec(f'game_panel.itemconfig({y},state=\'normal\')')
        except:
            pass

    def local_win(x, y, z):
        lmove = y
        for i in range(1, 8, 3):
            winrow = True
            for j in range(i, i + 3):
                if dic["button" + x + str(j)] != y:
                    winrow = False
                    break
            if winrow:
                break
        for i in range(1, 4):
            wincol = True
            for j in range(i, i + 7, 3):
                if dic["button" + x + str(j)] != y:
                    wincol = False
                    break
            if wincol:
                break
        windiag1 = True
        for i in range(1, 10, 4):
            if dic["button" + x + str(i)] != y:
                windiag1 = False
                break
        windiag2 = True
        for i in range(3, 8, 2):
            if dic["button" + x + str(i)] != y:
                windiag2 = False
                break
        if winrow or wincol or windiag1 or windiag2 == True:
            l_wins[int(x)] = lmove
            print(l_wins)
            exec(f'game_panel.itemconfig({z}{x},state=\'normal\')')
            exec(f'game_panel.delete(\'win{x}\')')
            for i in lbutt:
                if "button" + x in i:
                    exec(i + "[\'state\'] =  DISABLED")
                    if i not in disabled:
                        disabled.append(i)

    def global_win():
        winrow = False
        wincol = False
        windiag1 = False
        windiag2 = False
        for i in range(1, 10, 3):
            if l_wins[i] == l_wins[i + 1] == l_wins[i + 2] != "":
                winrow = True
                break
        for i in range(1, 4):
            if l_wins[i] == l_wins[i + 3] == l_wins[i + 6] != "":
                wincol = True
                break
        if l_wins[1] == l_wins[5] == l_wins[9] != "":
            windiag1 = True
        if l_wins[3] == l_wins[5] == l_wins[7] != "":
            windiag2 = True
        if winrow or wincol or windiag1 or windiag2 is True:
            c.send(bytes('lost', "utf-8"))
        return winrow or wincol or windiag1 or windiag2

    def hideboxes(box, x):
        print('hidebox: ', x)
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
                hideboxes('pink', msg[-2])
                disable(msg)
                if last_move == "O":
                    exec(msg + ".configure(text=\"X\",fg=\"Red\")")
                    exec(msg + ".unbind(\'<Button-1>\')")
                    disabled.append(msg)
                    dic[msg] = "X"
                elif last_move == "X":
                    exec(msg + ".configure(text=\"O\",fg=\"Blue\")")
                    exec(msg + ".unbind(\'<Button-1>\')")
                    disabled.append(msg)
                    dic[msg] = "O"
                local_win(msg[-2], moves[moves.index(last_move) - 1], moves[moves.index(last_move) - 1])
                checkifdisabled(msg[-1])

            elif "lost" in msg:
                disableall()
                hideboxes('blue', temp[-1])
                messagebox.showinfo("GAME OVER", "YOU LOST!!! YOU DUMB BASTARD\nLLLLLLL")

    def disableall():
        for i in lbutt:
            exec(i + '.unbind(\'<Button-1>\')')

    t = threading.Thread(target=listen)
    t.start()
    last_move = "O"
    dic = dict(map(lambda e: (e, " "), lbutt))
    disabled = []
    l_wins = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    moves = ["X", "O"]
    
    # defining change
    def change(x):
        global last_move
        c.send(bytes(x, "utf-8"))
        disable(x, "pinksquare", '#c354f7')
        hideboxes('blue', x[-2])
        if last_move == "O":
            exec(x+".configure(text=\"X\",fg=\"red\")")
            exec(x + ".unbind(\'<Button-1>\')")
            disabled.append(x)
            dic[x] = "X"
            last_move = "X"
            c.send(bytes("X", "utf-8"))
        else:
            exec(x + ".configure(text=\"O\",fg=\"Blue\")")
            exec(x + ".unbind(\'<Button-1>\')")
            disabled.append(x)
            dic[x] = "O"
            last_move = "O"
            c.send(bytes("O", "utf-8"))
        local_win(x[-2], last_move, last_move)
        checkifdisabled(x[-1], 'bigpinkbox', '#c354f7')
        disableall()
        if global_win():
            disableall()
            print('global win: ', x)
            hideboxes('pink', x[-1])
            messagebox.showinfo("GAME OVER", "YOU WON")

    #making the buttons
    f1 = Font(family="Lithos Pro Light",size=20,weight='bold')
    for i in range(1, 10):
        for j in range(1, 10):
            exec(
                f"button{i}{j} = Label(text=\"  \",font=f1,padx=6,pady=0,bg='#A18F80',fg=\"green\")"
                f"\nbutton{i}{j}.bind(\'<Button-1>\',lambda event:change(\"button{i}{j}\"))",locals(),globals())

    # screening buttons
    count = 1
    k = 1

    def make_grid(x, y):
        global count, k
        exec(f"win{k}{count} = game_panel.create_window({x},{y},anchor=\"nw\",window=button{k}{count},tags=\'win{k}\')",locals(),globals())
        count += 1
        if count - 1 == 9:
            count = 1
            k += 1

    for i in range(13, 100, 43):
        for j in range(15, 100, 42):
            make_grid(j, i)
    for i in range(13, 100, 43):
        for j in range(170, 255, 42):
            make_grid(j, i)
    for i in range(13, 100, 43):
        for j in range(325, 429, 42):
            make_grid(j, i)
    for i in range(170, 257, 43):
        for j in range(15, 100, 42):
            make_grid(j, i)
    for i in range(170, 257, 43):
        for j in range(170, 255, 42):
            make_grid(j, i)
    for i in range(170, 257, 43):
        for j in range(325, 429, 42):
            make_grid(j, i)
    for i in range(325, 414, 43):
        for j in range(15, 100, 42):
            make_grid(j, i)
    for i in range(325, 414, 43):
        for j in range(170, 255, 42):
            make_grid(j, i)
    for i in range(325, 414, 43):
        for j in range(325, 429, 42):
            make_grid(j, i)



def gamescreen(event=None):

    mainscreen.pack_forget()
    game_screen.pack()
    multiplayer()

    #exec(open("multiplayer.py").read())

def calling(m,n):
    if running == True:
        #global change
        print('multiplayer is runing')
        def activate(i,z):
            for j in range(1,10):
                eval(i+f".bind(\'<Button-1>\',lambda event: change(\'button{z}{j}\'))")
        activate(m,n)

#creating the button shapes
compshape = mainscreen.create_image(450,340,anchor='center',image=btn)
multshape = mainscreen.create_image(450,415,anchor='center',image=btn)
settshape = mainscreen.create_image(450,490,anchor='center',image=btn)
quitshape = mainscreen.create_image(450,565,anchor='center',image=btn)


def buttenter(win,shape,y,label,ly):
    exec("mainscreen.delete("+win+")")
    exec(win +"= mainscreen.create_window(450,"+ly+", anchor='center', window="+label+")",globals())
    exec(label+".configure(fg='#d7bd1e',font=('Ink Free',20,\"bold\"))")
    exec('mainscreen.delete('+shape+')')
    exec(shape+"= mainscreen.create_image(450,"+y+",anchor=\'center\',image=bigbtn)",globals())

def buttleave(win,shape,y,label,ly):
    exec(win +"= mainscreen.create_window(450,"+ly+", anchor='center', window="+label+")")
    exec(label+".configure(fg='white',font=('Ink Free',18,\"bold\"))")
    exec('mainscreen.delete('+shape+')')
    exec(shape+"= mainscreen.create_image(450,"+y+",anchor='center',image=btn)",globals())

#the button texts
f = Font(family = 'Ink Free',size=18,weight="bold")
Computer = Label(text='Computer',font=f,bg='black',padx=0,pady=0,fg='white',width=7)
Multiplayer = Label(text='Multiplayer',font=f,bg='black',padx=0,pady=0,fg='white',width=9)
Settings = Label(text='Settings',font=f,bg='black',padx=0,pady=0,fg='white',width=9)
Quit = Label(text='Quit',font=f,bg='black',padx=0,pady=0,fg='white',width=9)
#button windows
comp = mainscreen.create_window(450,325,anchor='center',window=Computer)
mult = mainscreen.create_window(450,400,anchor='center',window=Multiplayer)
sett = mainscreen.create_window(450,475,anchor='center',window=Settings)
quit = mainscreen.create_window(450,550,anchor='center',window=Quit)
#activites when interacted with the buttons
Computer.bind('<Enter>',lambda event: buttenter('comp','compshape','340','Computer','323'))
Computer.bind('<Leave>',lambda event: buttleave('comp','compshape','340','Computer','325'))
Multiplayer.bind('<Enter>',lambda event: buttenter('mult','multshape','415','Multiplayer','398'))
Multiplayer.bind('<Leave>',lambda event: buttleave('mult','multshape','415','Multiplayer','400'))
Settings.bind('<Enter>',lambda event: buttenter('sett','settshape','490','Settings','473'))
Settings.bind('<Leave>',lambda event: buttleave('sett','settshape','490','Settings','475'))
Quit.bind('<Enter>',lambda event: buttenter('quit','quitshape','565','Quit','548'))
Quit.bind('<Leave>',lambda event: buttleave('quit','quitshape','565','Quit','550'))

Multiplayer.bind('<Button-1>',gamescreen)
root.mainloop()
