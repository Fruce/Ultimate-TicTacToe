from telnetlib import WONT
from tkinter import *
import socket
import threading
from tkinter import  messagebox
lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1, 10)]) for x in range(1, 10)]).split(",")

c = socket.socket()
c.connect(('localhost', 9999))

def disable(x, y="#7ec7e6"):
    z = list(x)[-1]
    for i in lbutt:
        if "button" + z in i:
            exec(i + f"[\"bg\"] = \'{y}\'")
            exec(i + f"[\"activebackground\"] = \'{y}\'")
        if "button" + z in i and i not in disabled:
            exec(i + "[\"state\"] = ACTIVE")

        elif "button" + z not in i:
            exec(i + "[\"state\"] = DISABLED")
            exec(i + "[\"bg\"] = \"#ffe6ff\"")
            exec(i + "[\"activebackground\"] = \"#ffe6ff\"")

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

    print(l_wins)
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
        global temp
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
root = Tk()
root.configure(bg="black")


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
    c.send(bytes(x, "utf-8"))
    disable(x, "#e6b3ff")
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



for i in range(1, 10):
    for j in range(1, 10):
        exec(
            f"button{i}{j} = Button(root,text=\" \",font=\"Helvatica 15 bold\",padx=18,pady=8,width = 1,bg=\"#ffe6ff\",bd=0,command=lambda :change(\"button{i}{j}\"),state = NORMAL)")
count = 0
for i in range(0, 10, 4):
    for j in range(0, 10, 4):
        make_grid(i, j)
for i in [(0, 3), (3, 0), (0, 7), (7, 0)]:
    exec(f"l{i[0] + i[1]} = Label(text=\"\",font = \'Helvatica 1\',bg=\"black\",)")
    eval(f"l{i[0] + i[1]}.grid(row=i[0],column=i[1],pady=0)")

# canvas1 = Canvas(width=10,height=520,bg="red")
# canvas1.grid(row=0,column=4,columnspan=11)
root.mainloop()
print(dic)
