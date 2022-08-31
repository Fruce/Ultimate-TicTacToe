from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageSequence
from tkinter.font import Font
import PIL.Image
from tkinter import messagebox
from customtkinter import *
import socket
import threading
import subprocess
from os import chdir
from urllib.request import urlopen
chdir("assets")
def give_link():
    while True:
        try:
            url = urlopen("http://127.0.0.1:4040/api/tunnels").read().rstrip().decode().replace("false","False")
            exec("global url_dict ; url_dict = " + url)
            print(url_dict["tunnels"][0]["public_url"][6::])
            break
        except:
            continue
def start_ngrok(event):
    subprocess.Popen("python server.py")
    connect("localhost",9999)
    subprocess.Popen("ngrok.exe tcp 9999",creationflags=subprocess.CREATE_NEW_CONSOLE)
    th = threading.Thread(target=give_link)
    th.start()

root = CTk()
w = root.winfo_screenwidth() /2 - 530
h = root.winfo_screenwidth() /2 - 640
root.geometry(f"1060x640+{int(w)}+{int(h)}")
root.configure(bg='black')

root.set_appearance_mode('dark')

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
#button
btn = PIL.Image.open(r'button.png')
btn = btn.resize((300,210), Image.Resampling.LANCZOS)
btn = ImageTk.PhotoImage(btn)
#rematchbuttons
accept = PIL.Image.open(r'accept.png')
accept = accept.resize((65,63), Image.Resampling.LANCZOS)
accept = ImageTk.PhotoImage(accept)

deny = PIL.Image.open(r'deny.png')
deny = deny.resize((57,55), Image.Resampling.LANCZOS)
deny = ImageTk.PhotoImage(deny)
#entry
entry = PIL.Image.open(r'entry.png')
entry = entry.resize((900,470), Image.Resampling.LANCZOS)
entry = ImageTk.PhotoImage(entry)
#btn2
btn2 = PIL.Image.open(r'button.png')
btn2 = btn2.resize((250,210), Image.Resampling.LANCZOS)
btn2 = ImageTk.PhotoImage(btn2)
#bbtn2
bigbtn2 = PIL.Image.open(r'bigbutt.png')
bigbtn2 = bigbtn2.resize((270,240), Image.Resampling.LANCZOS) #330 240
bigbtn2 = ImageTk.PhotoImage(bigbtn2)
#big button
bigbtn = PIL.Image.open(r'bigbutt.png')
bigbtn = bigbtn.resize((330,240), Image.Resampling.LANCZOS)
bigbtn = ImageTk.PhotoImage(bigbtn)
#gamescreen bg
gcbg = PIL.Image.open(r'gcbg.png')
gcbg = gcbg.resize((1070,650), Image.Resampling.LANCZOS)
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
bob = mainscreen1.create_image(0,0,anchor='nw')
def playgif():
    global mcbg,mainscreen1
    mcbg = PIL.Image.open(r'mcbg.gif')

    for mcbg in ImageSequence.Iterator(mcbg):
        mcbg = ImageTk.PhotoImage(mcbg)
        mainscreen1.itemconfig(bob,image=mcbg)
        root.update()
playgif()

#creating gamescreen
game_screen = Canvas(root, width=1060, height=640,highlightthickness=6,highlightbackground='#080c11',relief='sunken')
game_screen.create_image(0,0,anchor='nw',image=gcbg)
running = False

def connect(HOST,PORT):
    global c
    c = socket.socket()
    try:
        c.connect((HOST, PORT))
        print("Connected")
        multiplayer()
    except Exception as e:
        print(e)


def multiplayer():
    mainscreen3.pack_forget()
    game_screen.pack(expand=True)
    global count,game_panel,k,last_move,bigbluebox,bigpinkbox,running,change,disabled,increaser,size

    running = True
    # making and gridding the canvas
    game_panel = Canvas(game_screen,bg="#F7E1A1", height=460, width=460,highlightthickness=0)
    game_screen.create_line(265,18,735,18,fill="#210101",width=6)
    game_screen.create_line(265, 18, 265, 492, fill="#210101", width=6)
    game_screen.create_line(265, 492, 735, 492, fill="#210101", width=6)
    game_screen.create_line(735, 18, 735, 492, fill="#210101", width=6)
    game_screen.create_window(500,255,anchor='center',window=game_panel)

    def rematch_create():
        global rematch
        def buttenter(e):
            exec(e+f".configure(bg='#1c1c1c')")
        def buttleave(e):
            exec(e+f".configure(bg='black')")
        def rematch_func(event=None):
            print('offer sent')
            c.send(bytes('rematch', "utf-8"))
            rematch.configure(text='Offer Sent',fg='#C0C0C0',bg='#0f0f0f')
            rematch.unbind('<Enter>')
            rematch.unbind('<Leave>')
            rematch.unbind('<Button-1>')

        f = Font(family='Ink Free', size=19, weight="bold")
        rematch = Label(text='Rematch', font=f,bg='black',fg='yellow',width=17,pady=5)
        rematch.bind('<Enter>', lambda e: buttenter('rematch'))
        rematch.bind('<Leave>', lambda e: buttleave('rematch'))
        rematch.bind('<Button-1>', rematch_func)

        game_screen.create_window(885, 515, anchor='center', window=rematch,tags='rematch')

    rematch_create()

    #O's side
    O_UT = game_screen.create_image(130,250,anchor='center',image=OUT_P,state='hidden',tags='turns')
    X_OT = game_screen.create_image(130, 250, anchor='center', image=XOT_P,state='hidden',tags='turns')
    #X's side
    X_UT = game_screen.create_image(130,250,anchor='center',image=XUT_P,state='hidden',tags='turns')
    O_OT = game_screen.create_image(130,250,anchor='center',image=OOT_P,state='hidden',tags='turns')
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

    f = CTkFrame(root,width=270,height=390)
    f.pack_propagate(0)
    game_screen.create_window(750,25, anchor='nw', window=f)

    f2 = CTkFrame(root, width=300, height=30)
    game_screen.create_window(750, 435, anchor='nw', window=f2)

    main_frame = CTkFrame(f, height=300, width=200, bg_color="#0c0c10", fg_color="#0c0c10")
    entry_frame = CTkFrame(f2, height=100, width=280,fg_color='#0c0c10',bg_color='#0c0c10')
    mycanvas = Canvas(main_frame, bg="#0c0c10", highlightbackground="#0c0c10", width=250, height=390)
    mycanvas.pack(side=LEFT, fill="both")

    # style = ttk.Style()
    # style.configure("Horizontal.TScrollbar", gripcount=0,
    #                 background="Green", darkcolor="DarkGreen", lightcolor="LightGreen",
    #                 troughcolor="gray", bordercolor="blue", arrowcolor="white")

    yscrollbar = Scrollbar(main_frame,orient='vertical',command=mycanvas.yview,bg='red',highlightbackground='red',highlightcolor='red',
                           troughcolor='yellow')
    yscrollbar.pack(side=RIGHT, fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    canvas_frame = CTkFrame(mycanvas, bg_color="#0c0c10", fg_color="#0c0c10")
    canvas_frame.bind("<Configure>", OnFrameConfigure)
    mycanvas.bind("<Configure>", FrameWidth)
    test = mycanvas.create_window((0, 0), window=canvas_frame, anchor="nw")
    main_frame.pack(side=TOP)
    entry_frame.pack(side=BOTTOM)

    fake_entrybox = CTkLabel(entry_frame,width=260,height=37,bg_color='#595959', state=DISABLED)
    entry_box = Text(entry_frame, width=32,height=2,bd=0,bg="#1a1712", fg="white", insertbackground="white")#28241c

    def enter_to_send(e):
        send(True, entry_box.get(1.0, "end-1c"))
        return "break"

    entry_box.bind("<Return>", enter_to_send)
    entry_box.bind("<Shift-Return>", lambda e: entry_box.insert(END, ""))
    fake_entrybox.pack()
    entry_box.place(x=1, y=1)

    def send(x, y):
        if x and y != "":
            entry_box.delete(1.0, "end-1c")
            c.send(bytes("\0<p>" + y + "<p>\0", 'utf-8'))
            frame = CTkFrame(canvas_frame, corner_radius=8)
            frame.pack(side=TOP, anchor="e", padx=5, pady=3)
            CTkLabel(frame, text=y, wraplength=120, corner_radius=15).pack(side=RIGHT, pady=5)
            mycanvas.update_idletasks()
            mycanvas.yview_moveto(1)
        elif y != "":
            frame = CTkFrame(canvas_frame, corner_radius=8)
            yview_coords = mycanvas.yview()[1]
            frame.pack(side=TOP, anchor="w", padx=5, pady=3)
            CTkLabel(frame, text=y, wraplength=120, corner_radius=8).pack(side=LEFT, pady=5)
            if yview_coords == 1:
                mycanvas.yview_moveto(1)

    # --------------------------------------------------------------------------------------------------------

    # making the shapes which shows up when local box is won and square highlights
    count = 1
    def shapes(x, y, shape):
        global count
        exec(f"{shape}{count} = game_panel.create_image({x},{y},anchor=\"nw\",image={shape},state=\'hidden\',tags=\'shapes\')",
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
            c.send(bytes('\0lost\0', "utf-8"))
        return winrow or wincol or windiag1 or windiag2

    def hideboxes(box, x):
        if box == 'blue':
            exec(f'game_panel.itemconfig(bluesquare{x},state=\'hidden\')')
            exec(f'game_panel.itemconfig(bigbluebox,state=\'hidden\')')
        else:
            exec(f'game_panel.itemconfig(pinksquare{x},state=\'hidden\')')
            exec(f'game_panel.itemconfig(bigpinkbox,state=\'hidden\')')

    def accept_func(e):
        c.send(bytes('accepted', "utf-8"))
        reset("FUCK")

    def deny_func(e):
        c.send(bytes('denied', "utf-8"))
        game_screen.delete('rmch')
        rematch_create()

    def listen():
        loc = []
        global last_move,rematch,albl,dlbl
        while True:
            if len(loc) == 0:
                loc.extend(x for x in c.recv(2048).decode().split('\0'))
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
                    turnshower2("O")
                    disabled.append(msg)
                    dic[msg] = "X"
                elif last_move == "X":
                    exec(msg + ".configure(text=\"O\",fg=\"blue\")")
                    exec(msg + ".unbind(\'<Button-1>\')")
                    turnshower2("X")
                    disabled.append(msg)
                    dic[msg] = "O"
                local_win(msg[-2], moves[moves.index(last_move) - 1], moves[moves.index(last_move) - 1])
                checkifdisabled(msg[-1])
            elif "lost" == msg:
                disableall()
                for i in lbutt:
                    exec(i + f"[\"bg\"] = \'#F7E1A1\'")
                hideboxes('blue', temp[-1])
                game_screen.delete('turns')
                messagebox.showinfo("GAME OVER", "YOU LOST!!! YOU DUMB BASTARD\nLLLLLLL")
            elif 'rematch' == msg:
                game_screen.delete('rematch')
                f = Font(family='Ink Free', size=17, weight="bold")
                albl = Label(bg='black', image=accept, borderwidth=0)
                dlbl = Label(bg='black', image=deny, borderwidth=0)
                rmch = Label(text='Rematch\nOffer', font=f, bg='black', fg='yellow', width=12)

                game_screen.create_window(767, 524, anchor='center', window=albl, tags='rmch')
                game_screen.create_window(1002, 524, anchor='center', window=dlbl, tags='rmch')
                game_screen.create_window(885, 525, anchor='center', window=rmch, tags='rmch')
                def buttenter(label):
                    exec(label + ".configure(bg='#1c1c1c')")
                def buttleave(label):
                    exec(label + ".configure(bg='black')")
                albl.bind('<Button-1>',accept_func)
                dlbl.bind('<Button-1>',deny_func)
                albl.bind('<Enter>', lambda e: buttenter('albl'))
                albl.bind('<Leave>', lambda e: buttleave('albl'))
                dlbl.bind('<Enter>', lambda e: buttenter('dlbl'))
                dlbl.bind('<Leave>', lambda e: buttleave('dlbl'))



            elif 'accepted' == msg:
                reset("FUCK")
            elif 'denied' == msg:
                game_screen.delete('rematch')
                rematch_create()
            else:
                msg = msg[3:-3]
                send(False, msg)


    def reset(move):
        global last_move,dic,disabled,l_wins,count,k
        game_screen.delete('rmch')
        if move == 'FUCK':
            game_screen.itemconfig(X_UT, state='hidden')
            game_screen.itemconfig(O_UT, state='hidden')
            game_screen.itemconfig(X_OT, state='hidden')
            game_screen.itemconfig(O_OT, state='hidden')

        for i in range(1,10):
            exec(f"game_panel.itemconfig(pinksquare{i}, state='hidden')")
            exec(f"game_panel.itemconfig(bluesquare{i}, state='hidden')")
            exec(f"game_panel.itemconfig(X{i}, state='hidden')")
            exec(f"game_panel.itemconfig(O{i}, state='hidden')")

        for i in lbutt:
            exec(i + "[\"bg\"] = \"#F7E1A1\"")

        for i in range(1,100):
            exec(f'game_panel.delete(\'win{i}\')')
        count = 1
        k = 1
        f1 = Font(family="Lithos Pro Light", size=20, weight='bold')
        for i in range(1, 10):
            for j in range(1, 10):
                exec(
                    f"button{i}{j} = Label(text=\"  \",font=f1,padx=5,pady=0,bg='#F7E1A1')"
                    f"\nbutton{i}{j}.bind(\'<Button-1>\',lambda event:change(\"button{i}{j}\"))", globals())
        gridder()
        last_move = "O"
        dic = {}
        dic = dict(map(lambda e: (e, " "), lbutt))
        print('dic: ',dic)
        disabled = []
        l_wins = {}
        l_wins = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        print(l_wins,'latest')

        for i in lbutt:
            binder(i)
        rematch_create()

    def disableall():
        for i in lbutt:
            exec(i + '.unbind(\'<Button-1>\')')

    if threading.active_count() != 2:
        t = threading.Thread(target=listen)
        t.start()
    last_move = "O"
    dic = {}
    dic = dict(map(lambda e: (e, " "), lbutt))
    disabled = []
    l_wins = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    moves = ["X", "O"]
    print(threading.active_count())

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

    # defining change
    def change(x):
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
            game_screen.delete('turns')
            print('global win: ', x)
            for i in lbutt:
                exec(i + f"[\"bg\"] = \'#F7E1A1\'")
            hideboxes('pink', x[-1])
            messagebox.showinfo("GAME OVER", "YOU WON")

    #making the buttons
    global f1

    f1 = Font(family="Lithos Pro Light",size=20,weight='bold')
    for i in range(1, 10):
        for j in range(1, 10):
            exec(
                f"button{i}{j} = Label(text=\"  \",font=f1,padx=5,pady=0,bg='#F7E1A1')"
                f"\nbutton{i}{j}.bind(\'<Button-1>\',lambda event:change(\"button{i}{j}\"))",globals())

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
    def gridder():
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
    gridder()
def gamescreen(e):
    subprocess.Popen(r'python server.py')
    connect('localhost',9999)

def binder(m):
    if running == True:
        def activate(i):
            exec(i+f".bind(\'<Button-1>\',lambda event: change(\'button{i[-2]}{i[-1]}\'))",globals())
            if i in disabled:
                eval(i+f".unbind(\'<Button-1>\')")
        activate(m)


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

def backenter(win, shape,  label, no):
    exec(f"mainscreen{no}.delete(" + win + ")")
    exec(win + f"= mainscreen{no}.create_window(220,503, anchor='center', window=" + label + ")", globals())
    exec(label + ".configure(fg='#d7bd1e',font=('Ink Free',20,\"bold\"))")
    exec(f'mainscreen{no}.delete(' + shape + ')')
    exec(shape + f"= mainscreen{no}.create_image(220,520,anchor=\'center\',image=bigbtn2)", globals())

def backleave(win, shape , label, no):
    exec(win + f"= mainscreen{no}.create_window(220,505, anchor='center', window=" + label + ")")
    exec(label + ".configure(fg='white',font=('Ink Free',17,\"bold\"))")
    exec(f'mainscreen{no}.delete(' + shape + ')')
    exec(shape + f"= mainscreen{no}.create_image(220,520 ,anchor='center',image=btn2)", globals())



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

def back_func(cno,bno):
    exec(f"mainscreen{cno}.pack_forget()")
    exec(f"mainscreen{bno}.pack()")

def lcl_func(event=None):
    global f, mainscreen3, host, join, hostshape, joinshape, host_win, join_win,back4,back_win4,backshape4
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
    host.bind('<Enter>', lambda event: buttenter('host_win', 'hostshape', '340', 'host', '322','3'))
    host.bind('<Leave>', lambda event: buttleave('host_win', 'hostshape', '340', 'host', '325','3'))
    join.bind('<Enter>', lambda event: buttenter('join_win', 'joinshape', '415', 'join', '397', '3'))
    join.bind('<Leave>', lambda event: buttleave('join_win', 'joinshape', '415', 'join', '400', '3'))
    host.bind("<Button-1>",gamescreen)
    join.bind('<Button-1>',lambda event: connect('localhost',9999))
    back4 = Label(text='Back', font=f, bg='black', padx=0, pady=0, fg='white', width=7)
    back_win4 = mainscreen3.create_window(220, 505, anchor='center', window=back4)
    backshape4 = mainscreen3.create_image(220, 520, anchor='center', image=btn2)
    back4.bind('<Enter>', lambda event: backenter('back_win4', 'backshape4', 'back4', '3'))
    back4.bind('<Leave>', lambda event: backleave('back_win4', 'backshape4', 'back4', '3'))
    back4.bind('<Button-1>', lambda event: back_func('3', '2'))

def glbl_func(e):
    global f, mainscreen3, host1, join1, hostshape1, joinshape1, host_win1, join_win1,back3,back_win3,backshape3
    mainscreen2.pack_forget()
    mainscreen3 = Canvas(root, bg='black', width=1060, height=640, highlightthickness=0)
    mainscreen3.pack()
    mainscreen3.create_image(0, 0, anchor='nw', image=mcbg)
    host1 = Label(text='Host', font=f, bg='black', padx=0, pady=0, fg='white', width=9)
    join1 = Label(text='Join', font=f, bg='black', padx=0, pady=0, fg='white', width=9)
    host_win1 = mainscreen3.create_window(530, 325, anchor='center', window=host1)
    join_win1= mainscreen3.create_window(530, 400, anchor='center', window=join1)
    hostshape1 = mainscreen3.create_image(530, 340, anchor='center', image=btn)
    joinshape1 = mainscreen3.create_image(530, 415, anchor='center', image=btn)
    host1.bind('<Enter>', lambda event: buttenter('host_win1', 'hostshape1', '340', 'host1', '322','3'))
    host1.bind('<Leave>', lambda event: buttleave('host_win1', 'hostshape1', '340', 'host1', '325','3'))
    host1.bind("<Button-1>",start_ngrok)
    join1.bind('<Enter>', lambda event: buttenter('join_win1', 'joinshape1', '415', 'join1', '397', '3'))
    join1.bind('<Leave>', lambda event: buttleave('join_win1', 'joinshape1', '415', 'join1', '400', '3'))

    #host.bind("<Button-1>",gamescreen)

    join1.bind('<Button-1>',join_func)
    back3 = Label(text='Back', font=f, bg='black', padx=0, pady=0, fg='white', width=7)
    back_win3 = mainscreen3.create_window(220, 505, anchor='center', window=back3)
    backshape3 = mainscreen3.create_image(220, 520, anchor='center', image=btn2)
    back3.bind('<Enter>', lambda event: backenter('back_win3', 'backshape3', 'back3', '3'))
    back3.bind('<Leave>', lambda event: backleave('back_win3', 'backshape3', 'back3', '3'))
    back3.bind('<Button-1>', lambda event: back_func('3', '2'))
def join_func(event=None):
    global join_win,joinshape,mainscreen4,join,back2,back_win2,backshape2
    f1 = Font(family = 'Child\'s Hand',size=18,weight="bold")
    f2 = Font(family='Child\'s Hand', size=17,slant='italic')
    f3 = Font(family='Child\'s Hand', size=27, weight='bold')
    mainscreen3.pack_forget()
    mainscreen4 = Canvas(root, bg='black', width=1060, height=640, highlightthickness=0)
    mainscreen4.pack()
    mainscreen4.create_image(0, 0, anchor='nw', image=mcbg)

    mainscreen4.create_text(550, 270, fill="#FFD700", font=f3,anchor='center',text="Enter Ip Address:- ")
    mainscreen4.create_line(380, 300,700,300 ,fill="#FFD700",width=4)

    def onclick(e):
        if addr_entry.get() =='Eg: 8.tcp.ngrok : 12515':
            addr_entry.delete(0,'end')
            addr_entry.config(fg='white',font=f1)
    def offclick(e):
        if addr_entry.get() == '':
            addr_entry.insert(0,'Eg: 8.tcp.ngrok : 12515')
            addr_entry.config(fg='grey',font=f2)

    lol = mainscreen4.create_image(602,430,anchor='center',image=entry)
    addr_entry = Entry(root,width=16,bd=0,bg='black',fg='grey',font=f2,insertbackground='white')
    addr_entry.insert(0,"Eg: 8.tcp.ngrok : 12515")
    addr_entry.bind("<FocusIn>",onclick)
    addr_entry.bind("<FocusOut>",offclick)
    mainscreen4.create_window(493,348,anchor='center',window=addr_entry)

    def joinenter(win, shape, y, label, ly, no='4'):
        exec(f"mainscreen{no}.delete(" + win + ")")
        exec(win + f"= mainscreen{no}.create_window(715," + ly + ", anchor='center', window=" + label + ")", globals())
        exec(label + ".configure(fg='#d7bd1e',font=('Ink Free',20,\"bold\"))")
        exec(f'mainscreen{no}.delete(' + shape + ')')
        exec(shape + f"= mainscreen{no}.create_image(715," + y + ",anchor=\'center\',image=bigbtn2)", globals())

    def joinleave(win, shape, y, label, ly, no='4'):
        exec(win + f"= mainscreen{no}.create_window(715," + ly + ", anchor='center', window=" + label + ")")
        exec(label + ".configure(fg='white',font=('Ink Free',17,\"bold\"))")
        exec(f'mainscreen{no}.delete(' + shape + ')')
        exec(shape + f"= mainscreen{no}.create_image(715," + y + ",anchor='center',image=btn2)", globals())


    join = Label(text='Join', font=f, bg='black', padx=0, pady=0, fg='white', width=7)
    join_win = mainscreen4.create_window(715, 350, anchor='center', window=join)
    joinshape = mainscreen4.create_image(715, 365, anchor='center', image=btn2)

    join.bind('<Enter>', lambda event: joinenter('join_win', 'joinshape', '365', 'join', '348'))
    join.bind('<Leave>', lambda event: joinleave('join_win', 'joinshape', '365', 'join', '350'))
    join.bind('<Button-1>', lambda event: addrextract(addr_entry.get()))
    addr_entry.bind('<Return>',lambda event: addrextract(addr_entry.get()))
    back2 = Label(text='Back', font=f, bg='black', padx=0, pady=0, fg='white', width=7)
    back_win2 = mainscreen4.create_window(220, 505, anchor='center', window=back2)
    backshape2 = mainscreen4.create_image(220, 520, anchor='center', image=btn2)
    back2.bind('<Enter>', lambda event: backenter('back_win2', 'backshape2', 'back2', '4'))
    back2.bind('<Leave>', lambda event: backleave('back_win2', 'backshape2', 'back2', '4'))
    back2.bind('<Button-1>', lambda event: back_func('4', '3'))

    def addrextract(addr):
        if addr == "Eg: 8.tcp.ngrok : 12515" or "":
            print('invalid entry')
        else:
            nigga = addr.split(':')
            connect(str(nigga[0]),int(nigga[1]))
def multbutt(event=None):
    global f,mainscreen2,lcl,glbl,lclshape,glblshape,lcl_win,glbl_win,back1,backshape1,back_win1
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
    glbl.bind('<Button-1>',glbl_func)

    back1 = Label(text='Back', font=f, bg='black', padx=0, pady=0, fg='white', width=7)
    back_win1 = mainscreen2.create_window(220, 505, anchor='center', window=back1)
    backshape1 = mainscreen2.create_image(220, 520, anchor='center', image=btn2)
    back1.bind('<Enter>', lambda event: backenter('back_win1', 'backshape1', 'back1', '2'))
    back1.bind('<Leave>', lambda event: backleave('back_win1', 'backshape1', 'back1', '2'))
    back1.bind('<Button-1>',lambda event: back_func('2','1'))
def destroy(e):
    root.destroy()
Multiplayer.bind('<Button-1>',multbutt)
Quit.bind('<Button-1>',destroy)

root.mainloop()
