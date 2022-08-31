from tkinter import *
root = Tk()
root.configure(bg="black")
lbutt = ",".join([",".join([f"button{x}{y}" for y in range(1,10)]) for x in range(1,10)]).split(",")
def make_grid(r,c):
    global count
    for i in range(r,r+3):
        for j in range(c,c+3):
            eval(f"{lbutt[count]}.grid(row={i},column={j},padx=2,pady=2)")
            count+=1
dic = dict(map(lambda e: (e," "),lbutt))
last_move = "O"
disabled = []
def change(x):
    global last_move
    z = list(x)[-1]
    for i in lbutt:
        if "button"+z in i:
            exec(i+"[\"bg\"] = \'#e6b3ff'")
            exec(i+"[\"activebackground\"] = \'#e6b3ff'")
            
                       
        if "button"+ z in i and i not in disabled:
            exec(i+"[\"state\"] = ACTIVE")
        
        elif "button"+ z not in i:
            exec(i+"[\"state\"] = DISABLED")
            exec(i+"[\"bg\"] = \"#ffe6ff\"")
            exec(i+"[\"activebackground\"] = \"#ffe6ff\"")    
    if last_move == "O":
        exec(x+"[\"text\"] = \"X\"")
        exec(x+"[\"state\"] = DISABLED")
        disabled.append(x)
        dic["button"+x] = "X"
        last_move = "X"
    else:
        exec(x+"[\"text\"] = \"O\"")
        exec(x+"[\"state\"] = DISABLED")
        disabled.append(x)
        dic["button"+x] = "O"
        last_move = "O"

for i in range(1,10):
    for j in range(1,10):
        exec(f"button{i}{j} = Button(root,text=\" \",font=\"Helvatica 15 bold\",padx=18,pady=8,width = 1,bg=\"#ffe6ff\",bd=0,command=lambda :change(\"button{i}{j}\"),state = NORMAL)")
count = 0
for i in range(0,10,4):
    for j in range(0,10,4):
        make_grid(i,j)
for i in [(0,3),(3,0),(0,7),(7,0)]:
    exec(f"l{i[0]+i[1]} = Label(text=\"\",font = \'Helvatica 1\',bg=\"black\",)")
    eval(f"l{i[0]+i[1]}.grid(row=i[0],column=i[1],pady=0)")

#canvas1 = Canvas(width=10,height=520,bg="red")
#canvas1.grid(row=0,column=4,columnspan=11)  
root.mainloop()
