import tkinter as tk
import random 
import ctypes

score=0
lost=False
bt=[0]*25

def make_grid():
    global grid
    grid=[]
    for i in range(0,25):
        grid.append(random.randrange(-5,5,1))
    mark=False  
    for i in range(0,25):
        if grid[i]==0:
            mark=True
    if mark==False:
        i=random.randrange(0,26)
        grid[i]=0

def savegame():
    def save():
        name=et.get()
        data=name + ',' + str(score) + ','
        with open('savegame.csv','a') as f: 
            f.write(data)
        a.destroy()
    
    a=tk.Tk()  
    a.title('บันทึกแต้มบุญที่นี่')
    a.geometry('250x70')
    a.resizable(0,0)
    lbl = tk.Label(a,text="ชื่่อเจ้าของแต้มบุญ")
    lbl.grid(row=0,column=0)
    et=tk.Entry(a,width=20)
    et.grid(row=0,column=1)
    bt = tk.Button(a,text='SAVE',command=save)
    bt.grid(row=1,column=0,columnspan=2)
    tk.mainloop()
      
def button_click(button_num):
    global grid
    global score
    global lost
    color="white"
    if grid[button_num]==0:  
        end_text="END"
        color="red"
        lost=True
    else:
        end_text=str(grid[button_num])
        score=score+grid[button_num]
        lb_ss.config(text=str(score))
        bt[button_num].config(state='disabled')
        
    bt[button_num].config(text=end_text,bg=color)
    
    if lost==True:
        for i in range(0,25):
            bt[i].config(state = 'disabled')
        aa='แต้มบุญ = ' + str(score)
        ctypes.windll.user32.MessageBoxW(0,aa,'GAME OVER',0)
        savegame()
        quit()

def high_score():
    def close():
        a.destroy()
        
    with open('savegame.csv','r') as f: 
            data=f.readlines()
    x=data[0].split(',') 
    x.pop() 
    hs={} 
    for i in range(0,len(x),2): 
        hs[x[i]]=int(x[i+1])
    hs_score=sorted(hs.values()) 
    hs_name=sorted(hs, key=hs.get)
    hs_text=[]
    for i in range(0,(10-len(hs_name))):
        hs_text.append(" -- ")
    j=0
    for i in range(len(hs_text),10): 
        if j<=len(hs_name):
            hs_text.append(hs_name[j] + " " + str(hs_score[j]))
        j+=1
        
    a=tk.Tk()  
    a.title('LOAD')
    a.geometry('250x270')
    a.config(bg="purple")
    a.resizable(0,0)
    
    for i in range(0,10):
        num=str(i+1) + ". " + hs_text[9-i] 
        lbl = tk.Label(a,text=num,bg="purple",fg='white',font=(12))
        lbl.grid(row=i,column=0,sticky='W')
    bt = tk.Button(a,text='Exit',command=close)
    bt.grid(row=11,column=0,columnspan=2)
    tk.mainloop()

def new_game():
    global score
    make_grid()
    score=0
    lb_ss.config(text="0")
    for i in range(0,25):
        bt[i].config(bg='SystemButtonFace',text="",state = 'normal')

def help_img_file():
    def clicked():
       root.destroy()
    root=tk.Toplevel(a)
    root.geometry("900x520")  
    root.title("How to play")
    root.resizable(0,0)
    widget = tk.Label(root, compound='top')
    widget.howtoplay_image_png = tk.PhotoImage(file="Capture.png")
    widget['image'] = widget.howtoplay_image_png
    widget.pack()
    btn = tk.Button(root, text='close', command=clicked)
    btn.pack()
    root.mainloop()
    

make_grid() 
a=tk.Tk()  
a.title('คลิ๊กช่องเก็บแต้มบุญ')
a.geometry('370x410')
a.resizable(0,0)
a.config(bg='purple')

for r in range(0,5):
    for c in range(0,5):
        bt[r*5+c] = tk.Button(a,width=6,height=3,command=lambda button_num=r*5+c: button_click(button_num))
        bt[r*5+c].grid(row=r,column=c,padx=10,pady=10)

lb_s=tk.Label(a,text="Score=",bg="purple",fg="white",font=(18)) 
lb_s.grid(row=5,column=0)
lb_ss=tk.Label(a,text="0",bg="purple",fg="white",font=(18))
lb_ss.grid(row=5,column=1,sticky="W")
bt_hs=tk.Button(a,text="LOAD",command=high_score)
bt_hs.grid(row=5,column=2)
bt_help=tk.Button(a,text="How to play",command=help_img_file)
bt_help.grid(row=5,column=3)
bt_new=tk.Button(a,text="New Game",command=new_game)
bt_new.grid(row=5, column=4)

tk.mainloop()
