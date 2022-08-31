from tkinter import *
import socket
import threading
from tkinter import messagebox
from customtkinter import *
from time import *
root = CTk()
set_appearance_mode("dark")
root.geometry("940x520")
root.resizable(False, False)
root.configure(bg="black")
root.title("Ultimate TicTacToe")
lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1, 10)]) for x in range(1, 10)]).split(",")
# link = input("Enter the join link: ")
# port = int(input("Enter the port number: "))
username = "Helo"
c = socket.socket()
def connect():
    try:
        c.connect(("localhost", 9999))
        print("Connected")
    except:
        connect()
print("Waiting for connections...")
connect()


def disable(x, y="#7ec7e6"):
    z = list(x)[-1]
    for i in lbutt:
        if i[-2] not in [str(x) for x in l_wins.keys() if l_wins[x] != ""]:
            if "button" + z in i:
                exec(i + f"[\"bg\"] = \'{y}\'")
                exec(i + f"[\"activebackground\"] = \'{y}\'")
            if "button" + z in i and i not in disabled:
                exec(i + "[\"state\"] = ACTIVE")

            elif "button" + z not in i:
                exec(i + "[\"state\"] = DISABLED")
                exec(i + "[\"bg\"] = \"#ffe6ff\"")
                exec(i + "[\"activebackground\"] = \"#ffe6ff\"")
def FrameWidth(event):
    canvas_width = event.width
    mycanvas.itemconfig(test,width = canvas_width)
def OnFrameConfigure(event):
    mycanvas.configure(scrollregion=mycanvas.bbox("all"))
canvas1 = Canvas(root,bg="#212325",highlightbackground="black",width=420)
f = CTkFrame(canvas1,highlightbackground="#212325",bg_color="#212325",fg_color="#212325")
canvas1.grid(row=0,column=11,rowspan=11,sticky="ns")
canvas1.create_window((15,10),window=f,anchor="nw")
main_frame = CTkFrame(f,height=300,width=400,bg_color="#212325",fg_color="#212325")
entry_frame = CTkFrame(f,height=100,width=400,fg_color="#212325") #fg_color="#212325"
mycanvas = Canvas(main_frame,bg="#212325",highlightbackground="#212325")
mycanvas.pack(side=LEFT,fill="both")
yscrollbar = Scrollbar(main_frame,command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill="y")
mycanvas.configure(yscrollcommand=yscrollbar.set)
canvas_frame = CTkFrame(mycanvas,bg_color="#212325",fg_color="#212325")
canvas_frame.bind("<Configure>", OnFrameConfigure)
mycanvas.bind("<Configure>",FrameWidth)
test = mycanvas.create_window((0,0),window=canvas_frame,anchor="nw")
main_frame.pack(side=TOP,pady=20)
random_label = CTkLabel(f,text="")
random_label_again = CTkLabel(f,text="")
entry_frame.pack(side=BOTTOM,pady=20)
random_label.pack(side=BOTTOM)
random_label_again.pack(side=BOTTOM)
fake_entrybox = CTkEntry(entry_frame,width=295,height=95,state=DISABLED)
entry_box = Text(entry_frame,width=35,height=5,bd=0,bg="#343638",fg="white",insertbackground="white")
send_button = CTkButton(entry_frame,text="Send",width=12,command=lambda:send(True,entry_box.get(1.0,"end-1c")))
send_button.pack(side=RIGHT)
def enter_to_send(e):
    send(True,entry_box.get(1.0,"end-1c"))
    return "break"
entry_box.bind("<Return>",enter_to_send)
entry_box.bind("<Shift-Return>",lambda e: entry_box.insert(END,""))
fake_entrybox.pack(side=RIGHT,padx=20)
entry_box.place(x=25,y=5)
def send(x,y):
    if x and y != "":
        entry_box.delete(1.0,"end-1c")
        c.send(bytes("\0<p>"+y+"<p>\0",'utf-8'))
        frame = CTkFrame(canvas_frame,corner_radius=8)
        frame.pack(side=TOP,anchor="e",padx=20,pady=3)
        CTkLabel(frame,text=y,wraplength=300,corner_radius=8).pack(side=RIGHT,pady=5)
        mycanvas.update_idletasks()
        mycanvas.yview_moveto(1)
    elif y != "":
        frame = CTkFrame(canvas_frame,corner_radius=8)
        yview_coords = mycanvas.yview()[1]
        frame.pack(side=TOP,anchor="w",padx=20,pady=3)
        CTkLabel(frame,text=y,wraplength=300,corner_radius=8).pack(side=LEFT,pady=5)
        if yview_coords == 1:
            mycanvas.yview_moveto(1)
def checkifdisabled(p,r,q = "#7ec7e6"):
    try:
        if len(disabled) == 81:
            messagebox.info("It's a draw!!")
        elif all(elem in disabled for elem in [f"button{p}{q}" for q in range(1,10)]):
            if r:
                for i in lbutt:
                    if i not in disabled:
                        exec(f"{i}[\"state\"] = ACTIVE")
            for j in lbutt:
                if j[-2] not in [str(x) for x in l_wins.keys() if l_wins[x] != ""]:
                    exec(j + f"[\"bg\"] = \"{q}\"")
                    exec(j + f"[\"activebackground\"] = \"{q}\"")
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
            return winrow

    for i in range(1,4):
        wincol = True
        for j in range(i,i+7,3):
            if dic["button"+x+str(j)] != y:
                wincol = False
                break
        if wincol:
            return wincol
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
    return windiag1 or windiag2

def global_win():

    print(l_wins)
    for i in range(1,10,3):
        if l_wins[i] == l_wins[i+1] == l_wins[i+2] != "":
            return True
    for i in range(1,4):
        if l_wins[i] == l_wins[i+3] == l_wins[i+6] != "":
            return True
    if l_wins[1] == l_wins[5] == l_wins[9] != "":
        return True
    if l_wins[3] == l_wins[5] == l_wins[7] != "":
        return True

def listen():
    loc = []
    global last_move
    while True:
        if len(loc) == 0:
            loc.extend(c.recv(2048).decode().split('\0'))
        print(loc)
        msg = loc.pop(0)
        print(msg)
        if msg == "X":
            last_move = "X"
        elif msg == "O":
            last_move = "O"
        elif "button" in msg and msg[0] != "<":
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
            if local_win(msg[-2],moves[moves.index(last_move)-1]):
                for i in lbutt:
                    if "button"+msg[-2] in i:
                        exec(i + "[\"bg\"] = \"#eb6e8b\"")
                        exec(i + "[\"activebackground\"] = \"#eb6e8b\"")
                        exec(i+"[\'state\'] =  DISABLED")
                        if i not in disabled:
                            disabled.append(i)
                l_wins[int(msg[-2])] = moves[moves.index(last_move)-1]
            checkifdisabled(msg[-1],True)
        elif msg == 'lost':
            disableall()
            messagebox.showinfo("GAME OVER","YOU LOST!!!")
            root.destroy()
        else:
            msg = msg[3:-3]
            send(False,msg)

def disableall():
    for i in lbutt:
        exec(f"{i}[\"state\"] = DISABLED")


t = threading.Thread(target=listen)
t.start()
last_move = "O"


def make_grid(r, c):
    global count
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            eval(f"{lbutt[count]}.grid(row={i},column={j},padx=2,pady=2)")
            count += 1


dic = dict(map(lambda e: (e, " "), lbutt))
disabled = []
l_wins={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
moves = ["X","O"]

def change(x):
    global last_move
    c.send(bytes('\0'+x+'\0', "utf-8"))
    disable(x, "#e6b3ff")
    checkifdisabled(x[-1],False,"#e6b3ff")
    if last_move == "O":
        exec(x + "[\"text\"] = \"X\"")
        exec(x + "[\"state\"] = DISABLED")
        disabled.append(x)
        dic[x] = "X"
        last_move = "X"
        c.send(bytes("\0X\0", "utf-8"))
    else:
        exec(x + "[\"text\"] = \"O\"")
        exec(x + "[\"state\"] = DISABLED")
        disabled.append(x)
        dic[x] = "O"
        last_move = "O"
        c.send(bytes("\0O\0", "utf-8"))
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
        if global_win() is True:
            disableall()
            c.send(bytes('\0lost\0', "utf-8"))
            messagebox.showinfo("GAME OVER","YOU WON")
            root.destroy()
for i in range(1, 10):
    for j in range(1, 10):
        exec(f"button{i}{j} = Button(root,text=\" \",font=\"Helvatica 15 bold\",padx=18,pady=8,width = 1,bg=\"#ffe6ff\",bd=0,command=lambda :change(\"button{i}{j}\"),state = NORMAL)")
count = 0
for i in range(0, 10, 4):
    for j in range(0, 10, 4):
        make_grid(i, j)
for i in [(0, 3), (3, 0), (0, 7), (7, 0)]:
    exec(f"l{i[0] + i[1]} = Label(text=\"\",font = \'Helvatica 1\',bg=\"black\",)")
    eval(f"l{i[0] + i[1]}.grid(row=i[0],column=i[1],pady=0)")
root.mainloop()
print(dic)
print(l_wins)
print(disabled)
