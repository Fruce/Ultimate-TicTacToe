from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import PIL.Image
from tkinter import messagebox
from customtkinter import *
import socket
import threading

import time
root = Tk()
root.geometry("1060x640")
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
mcbg = mcbg.resize((1060,640), Image.Resampling.LANCZOS)
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
gcbg = gcbg.resize((1060,640), Image.Resampling.LANCZOS)
gcbg = ImageTk.PhotoImage(gcbg)
#turns
OUT = PIL.Image.open(r'OUT.png')
OUT = OUT.resize((200,100), Image.Resampling.LANCZOS)
OUT_P = ImageTk.PhotoImage(OUT)
XOT = PIL.Image.open(r'XOT.png')
XOT = XOT.resize((250,150), Image.Resampling.LANCZOS)
XOT_P = ImageTk.PhotoImage(XOT)
XUT = PIL.Image.open(r'XUT.png')
XUT = XUT.resize((200,100), Image.Resampling.LANCZOS)
XUT_P = ImageTk.PhotoImage(XUT)
OOT = PIL.Image.open(r'OOT.png')
OOT = OOT.resize((250,150), Image.Resampling.LANCZOS)
OOT_P = ImageTk.PhotoImage(OOT)

#creating mainscreen
mainscreen1 = Canvas(root,bg='black',width=1060,height=640,highlightthickness=0)
mainscreen1.pack()
mainscreen1.create_image(0,0,anchor='nw',image=mcbg)

#creating gamescreen
game_screen = Canvas(root, width=1060, height=640,highlightthickness=6,highlightbackground='#080c11',relief='sunken')
game_screen.create_image(0,0,anchor='nw',image=gcbg)
running = False

def multiplayer():

    game_screen.pack()
    global count,game_panel,k,last_move,bigbluebox,bigpinkbox,running,rebind,disabled,increaser,size

    running = True

    c = socket.socket()
    def connect():
        try:
            c.connect(("localhost", 9999))
            print("Connected")
        except:
            connect()

    print("Waiting for connections...")
    connect()

    # making and gridding the canvas
    game_panel = Canvas(game_screen,bg="#F7E1A1", height=460, width=460,highlightthickness=0)
    game_screen.create_line(265,18,735,18,fill="#210101",width=6)
    game_screen.create_line(265, 18, 265, 492, fill="#210101", width=6)
    game_screen.create_line(265, 492, 735, 492, fill="#210101", width=6)
    game_screen.create_line(735, 18, 735, 492, fill="#210101", width=6)
    game_screen.create_window(500,255,anchor='center',window=game_panel)
    #O's side
    O_UT = game_screen.create_image(130,250,anchor='center',image=OUT_P,state='hidden')
    X_OT = game_screen.create_image(130, 250, anchor='center', image=XOT_P,state='hidden')
    #X's side
    X_UT = game_screen.create_image(130,250,anchor='center',image=XUT_P,state='hidden')
    O_OT = game_screen.create_image(130,250,anchor='center',image=OOT_P,state='hidden')
    #bigboxes
    bigpinkbox = game_panel.create_image(-300, -85, anchor="nw", image=bbb, state='hidden')
    bigbluebox = game_panel.create_image(-300, -85, anchor="nw", image=bgb, state='hidden')
    lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1, 10)]) for x in range(1, 10)]).split(",")

# -----------------------------------------------------------------------------------------------------------------

    def FrameWidth(event):
        canvas_width = event.width
        mycanvas.itemconfig(test, width=canvas_width)

    def OnFrameConfigure(event):
        mycanvas.configure(scrollregion=mycanvas.bbox("all"))

    # canvas1 = Canvas(root,bg="#212325",highlightbackground="white",width=300,height=470)
    # canvas1_win = game_screen.create_window(750,20,anchor='nw',window=canvas1)
    f = CTkFrame(root, highlightbackground="#171717",width=300,height=480)
    f.pack_propagate(0)# fg_color="green")
    f_win = game_screen.create_window(750,17, anchor='nw', window=f)
    f_label = Label(f,image=gcbg)
    f_label.pack()
    # canvas1.grid(row=0,column=11,rowspan=11,sticky="ns")
    #canvas1.create_window((5,5),window=f,anchor="nw")
    main_frame = CTkFrame(f_label, height=300, width=200, bg_color="#0c0c10", fg_color="#0c0c10")
    entry_frame = CTkFrame(f_label, height=100, width=280,fg_color='#0c0c10',bg_color='#0c0c10')

    mycanvas = Canvas(main_frame, bg="#0c0c10", highlightbackground="#0c0c10", width=250, height=375)

    # canvas1.create_image(0,0,anchor='nw',image=gcbg)

    mycanvas.pack(side=LEFT, fill="both")
    yscrollbar = Scrollbar(main_frame, command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    canvas_frame = CTkFrame(mycanvas, bg_color="#0c0c10", fg_color="#0c0c10")
    canvas_frame.bind("<Configure>", OnFrameConfigure)
    mycanvas.bind("<Configure>", FrameWidth)
    test = mycanvas.create_window((0, 0), window=canvas_frame, anchor="nw")
    main_frame.pack(side=TOP, pady=10)
    random_label = CTkLabel(f_label, text="")
    random_label_again = CTkLabel(f_label, text="")
    entry_frame.pack(side=BOTTOM, pady=17)
    random_label.pack(side=BOTTOM)
    random_label_again.pack(side=BOTTOM)
    fake_entrybox = CTkEntry(entry_frame, width=237, height=45, state=DISABLED)
    entry_box = Text(entry_frame, width=28, height=2, bd=0, bg="#28241c", fg="white", insertbackground="white")
    send_button = CTkButton(entry_frame, text="Send", width=12,
                            command=lambda: send(True, entry_box.get(1.0, "end-1c")))
    send_button.pack(side=RIGHT)

    def enter_to_send(e):
        send(True, entry_box.get(1.0, "end-1c"))
        return "break"

    entry_box.bind("<Return>", enter_to_send)
    entry_box.bind("<Shift-Return>", lambda e: entry_box.insert(END, ""))
    fake_entrybox.pack(side=RIGHT, padx=5)
    entry_box.place(x=10, y=5)

    def send(x, y):
        if x and y != "":
            entry_box.delete(1.0, "end-1c")
            c.send(bytes("\0<p>" + y + "<p>\0", 'utf-8'))
            frame = CTkFrame(canvas_frame, corner_radius=8)
            frame.pack(side=TOP, anchor="e", padx=20, pady=3)
            CTkLabel(frame, text=y, wraplength=300, corner_radius=8).pack(side=RIGHT, pady=5)
            mycanvas.update_idletasks()
            mycanvas.yview_moveto(1)
        elif y != "":
            frame = CTkFrame(canvas_frame, corner_radius=8)
            yview_coords = mycanvas.yview()[1]
            frame.pack(side=TOP, anchor="w", padx=20, pady=3)
            CTkLabel(frame, text=y, wraplength=300, corner_radius=8).pack(side=LEFT, pady=5)
            if yview_coords == 1:
                mycanvas.yview_moveto(1)

    # --------------------------------------------------------------------------------------------------------

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
    def disable(x, y="bluesquare", c="#5fffb1"):
        j = 0
        z = list(x)[-1]
        for i in lbutt:
            if "button" + z in i:
                exec(i + f"[\"bg\"] = \'{c}\'")
                exec(f'game_panel.itemconfig({y}' + z + ',state=\'normal\')')
                binder(i)
            elif "button" + z not in i:
                exec(i + ".unbind(\'<Button-1>\')")
                exec(i + "[\"bg\"] = \"#F7E1A1\"")

    def checkifdisabled(p, y='bigbluebox', c="#5fffb1"):
        try:
            if all(elem in disabled for elem in [f"button{p}{q}" for q in range(1, 10)]):
                for i in lbutt:
                    binder(i)

                for i in lbutt:
                    exec(i + f"[\"bg\"] = \'{c}\'")
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
                    exec(i + f".unbind(\'<Button-1>\')")
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

        if box == 'blue':
            exec(f'game_panel.itemconfig(bluesquare{x},state=\'hidden\')')
            exec(f'game_panel.itemconfig(bigbluebox,state=\'hidden\')')
        else:
            exec(f'game_panel.itemconfig(pinksquare{x},state=\'hidden\')')
            exec(f'game_panel.itemconfig(bigpinkbox,state=\'hidden\')')

    def listen():
        loc = []
        global last_move
        while True:
            if len(loc) == 0:
                loc.extend([x for x in c.recv(2048).decode().split('\0') if x != '' or '\0'])
            print(loc)
            msg = loc.pop(0)
            print(msg)
            if msg == "X":
                last_move = "X"
            elif msg == "O":
                last_move = "O"
            elif "button" in msg and msg[0] != "<":
                temp = msg
                hideboxes('pink', msg[-2])
                disable(msg)
                if last_move == "O":
                    exec(msg + ".configure(text=\"X\",fg=\"#ed151d\")")
                    exec(msg + ".unbind(\'<Button-1>\')")
                    turnshower2('O')
                    disabled.append(msg)
                    dic[msg] = "X"
                elif last_move == "X":
                    exec(msg + ".configure(text=\"O\",fg=\"blue\")")
                    exec(msg + ".unbind(\'<Button-1>\')")
                    turnshower2('X')
                    disabled.append(msg)
                    dic[msg] = "O"
                local_win(msg[-2], moves[moves.index(last_move) - 1], moves[moves.index(last_move) - 1])
                checkifdisabled(msg[-1])
            elif "lost" in msg:
                disableall()
                for i in lbutt:
                    exec(i + f"[\"bg\"] = \'#F7E1A1\'")
                hideboxes('blue', temp[-1])
                hideturns()
                messagebox.showinfo("GAME OVER", "YOU LOST!!! YOU DUMB BASTARD\nLLLLLLL")
            else:
                msg = msg[3:-3]
                send(False, msg)
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

    def turnshower(move):
        if move == 'X':
            game_screen.itemconfig(X_UT, state='hidden')
            game_screen.itemconfig(O_OT, state='normal')
        if move == "O":
            game_screen.itemconfig(O_UT, state='hidden')
            game_screen.itemconfig(X_OT, state='normal')

    def turnshower2(move):
        if move == 'X':
            game_screen.itemconfig(O_OT, state='hidden')
            game_screen.itemconfig(X_UT, state='normal')
        if move == 'O':
            game_screen.itemconfig(X_OT, state='hidden')
            game_screen.itemconfig(O_UT, state='normal')


    def rebind(x):
        print('hello is run',x)
        global last_move
        c.send(bytes(x, "utf-8"))
        disable(x, "pinksquare", '#f1aaf1')
        hideboxes('blue', x[-2])
        if last_move == "O":
            exec(x+".configure(text=\"X\",fg=\"#ed151d\")")
            exec(x + ".unbind(\'<Button-1>\')")
            turnshower('X')
            disabled.append(x)
            dic[x] = "X"
            last_move = "X"
            c.send(bytes("X", "utf-8"))
        else:
            exec(x + ".configure(text=\"O\",fg=\"blue\")")
            exec(x + ".unbind(\'<Button-1>\')")
            turnshower('O')
            disabled.append(x)
            dic[x] = "O"
            last_move = "O"
            c.send(bytes("O", "utf-8"))
        local_win(x[-2], last_move, last_move)
        checkifdisabled(x[-1],'bigpinkbox', '#f1aaf1')
        disableall()
        if global_win():
            disableall()
            hideturns()
            print('global win: ', x)
            exec(i + f"[\"bg\"] = \'#F7E1A1\'")
            hideboxes('pink', x[-1])
            messagebox.showinfo("GAME OVER", "YOU WON")
    def hideturns():
        game_panel.itemconfig(X_UT, state='hidden')
        game_panel.itemconfig(X_OT, state='hidden')
        game_panel.itemconfig(O_UT, state='hidden')
        game_panel.itemconfig(O_OT, state='hidden')
    # defining change
    def change(x):
        print('change is run',x)
        global last_move
        c.send(bytes(x, "utf-8"))
        disable(x, "pinksquare", '#f1aaf1')
        hideboxes('blue', x[-2])
        if last_move == "O":
            exec(x+".configure(text=\"X\",fg=\"#ed151d\")")
            exec(x + ".unbind(\'<Button-1>\')")
            turnshower('X')
            disabled.append(x)
            dic[x] = "X"
            last_move = "X"
            c.send(bytes("X", "utf-8"))
        else:
            exec(x + ".configure(text=\"O\",fg=\"blue\")")
            exec(x + ".unbind(\'<Button-1>\')")
            turnshower('O')
            disabled.append(x)
            dic[x] = "O"
            last_move = "O"
            c.send(bytes("O", "utf-8"))
        local_win(x[-2], last_move, last_move)
        checkifdisabled(x[-1],'bigpinkbox', '#f1aaf1')
        disableall()
        if global_win():
            disableall()
            hideturns()
            print('global win: ', x)
            exec(i + f"[\"bg\"] = \'#F7E1A1\'")
            hideboxes('pink', x[-1])
            messagebox.showinfo("GAME OVER", "YOU WON")

    #making the buttons
    f1 = Font(family="Lithos Pro Light",size=20,weight='bold')
    for i in range(1, 10):
        for j in range(1, 10):
            exec(
                f"button{i}{j} = Label(text=\"  \",font=f1,padx=5,pady=0,bg='#F7E1A1')"
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

    mainscreen3.pack_forget()
    game_screen.pack()
    multiplayer()

def binder(m):
    if running == True:
        def activate(i):
            eval(i+f".bind(\'<Button-1>\',lambda event: rebind(\'button{i[-2]}{i[-1]}\'))")
            if i in disabled:
                eval(i+f".unbind(\'<Button-1>\')")
        activate(m)

def server(event=None):
    global client
    exec(open("server.py").read())
    gamescreen()


#creating the button shapes
compshape = mainscreen1.create_image(530,340,anchor='center',image=btn)
multshape = mainscreen1.create_image(530,415,anchor='center',image=btn)
settshape = mainscreen1.create_image(530,490,anchor='center',image=btn)
quitshape = mainscreen1.create_image(530,565,anchor='center',image=btn)

def buttenter(win,shape,y,label,ly,no='1'):
    exec(f"mainscreen{no}.delete("+win+")")
    exec(win +f"= mainscreen{no}.create_window(530,"+ly+", anchor='center', window="+label+")",globals())
    exec(label+".configure(fg='#d7bd1e',font=('Ink Free',20,\"bold\"))")
    exec(f'mainscreen{no}.delete('+shape+')')
    exec(shape+f"= mainscreen{no}.create_image(530,"+y+",anchor=\'center\',image=bigbtn)",globals())

def buttleave(win,shape,y,label,ly,no='1'):
    exec(win +f"= mainscreen{no}.create_window(530,"+ly+", anchor='center', window="+label+")")
    exec(label+".configure(fg='white',font=('Ink Free',18,\"bold\"))")
    exec(f'mainscreen{no}.delete('+shape+')')
    exec(shape+f"= mainscreen{no}.create_image(530,"+y+",anchor='center',image=btn)",globals())

#the button texts
f = Font(family = 'Ink Free',size=18,weight="bold")
Computer = Label(text='Computer',font=f,bg='black',padx=0,pady=0,fg='white',width=7)
Multiplayer = Label(text='Multiplayer',font=f,bg='black',padx=0,pady=0,fg='white',width=9)
Settings = Label(text='Settings',font=f,bg='black',padx=0,pady=0,fg='white',width=9)
Quit = Label(text='Quit',font=f,bg='black',padx=0,pady=0,fg='white',width=9)
#button windows
comp = mainscreen1.create_window(530,325,anchor='center',window=Computer)
mult = mainscreen1.create_window(530,400,anchor='center',window=Multiplayer)
sett = mainscreen1.create_window(530,475,anchor='center',window=Settings)
quit = mainscreen1.create_window(530,550,anchor='center',window=Quit)
#activites when interacted with the buttons
Computer.bind('<Enter>',lambda event: buttenter('comp','compshape','340','Computer','323'))
Computer.bind('<Leave>',lambda event: buttleave('comp','compshape','340','Computer','325'))
Multiplayer.bind('<Enter>',lambda event: buttenter('mult','multshape','415','Multiplayer','398'))
Multiplayer.bind('<Leave>',lambda event: buttleave('mult','multshape','415','Multiplayer','400'))
Settings.bind('<Enter>',lambda event: buttenter('sett','settshape','490','Settings','473'))
Settings.bind('<Leave>',lambda event: buttleave('sett','settshape','490','Settings','475'))
Quit.bind('<Enter>',lambda event: buttenter('quit','quitshape','565','Quit','548'))
Quit.bind('<Leave>',lambda event: buttleave('quit','quitshape','565','Quit','550'))

def lcl_func(event=None):
    global f, mainscreen3, host, join, hostshape, joinshape, host_win, join_win
    mainscreen2.pack_forget()
    mainscreen3 = Canvas(root, bg='black', width=1060, height=640, highlightthickness=0)
    mainscreen3.pack()
    mainscreen3.create_image(0, 0, anchor='nw', image=mcbg)
    host = Label(text='Host', font=f, bg='black', padx=0, pady=0, fg='white', width=9)
    join = Label(text='Join', font=f, bg='black', padx=0, pady=0, fg='white', width=9)
    host_win = mainscreen3.create_window(530, 325, anchor='center', window=host)
    join_win = mainscreen3.create_window(530, 400, anchor='center', window=join)
    hostshape = mainscreen3.create_image(530, 340, anchor='center', image=btn)
    joinshape = mainscreen3.create_image(530, 415, anchor='center', image=btn)
    host.bind('<Enter>', lambda event: buttenter('host_win', 'hostshape', '340', 'host', '323','3'))
    host.bind('<Leave>', lambda event: buttleave('host_win', 'hostshape', '340', 'host', '325','3'))
    join.bind('<Enter>', lambda event: buttenter('join_win', 'joinshape', '415', 'join', '398', '3'))
    join.bind('<Leave>', lambda event: buttleave('join_win', 'joinshape', '415', 'join', '400', '3'))

    join.bind('<Button-1>',gamescreen)
    host.bind('<Button-1>',server,add="+")
    glbl.bind('<Button-1>', gamescreen, add="+")
def multbutt(event=None):
    global f,mainscreen2,lcl,glbl,lclshape,glblshape,lcl_win,glbl_win
    mainscreen1.pack_forget()
    mainscreen2 = Canvas(root, bg='black', width=1060, height=640, highlightthickness=0)
    mainscreen2.pack()
    mainscreen2.create_image(0, 0, anchor='nw', image=mcbg)
    lcl = Label(text='Local', font=f, bg='black', padx=0, pady=0, fg='white', width=9)
    glbl = Label(text='Global', font=f, bg='black', padx=0, pady=0, fg='white', width=9)
    lcl_win = mainscreen2.create_window(530, 325, anchor='center', window=lcl)
    glbl_win = mainscreen2.create_window(530, 400, anchor='center', window=glbl)
    lclshape = mainscreen2.create_image(530, 340, anchor='center', image=btn)
    glblshape = mainscreen2.create_image(530, 415, anchor='center', image=btn)
    lcl.bind('<Enter>', lambda event: buttenter('lcl_win', 'lclshape', '340', 'lcl', '323','2'))
    lcl.bind('<Leave>', lambda event: buttleave('lcl_win', 'lclshape', '340', 'lcl', '325','2'))
    glbl.bind('<Enter>', lambda event: buttenter('glbl_win', 'glblshape', '415', 'glbl', '398', '2'))
    glbl.bind('<Leave>', lambda event: buttleave('glbl_win', 'glblshape', '415', 'glbl', '400', '2'))
    lcl.bind('<Button-1>', lcl_func)

Multiplayer.bind('<Button-1>',multbutt)
root.mainloop()
