import game
import tkinter as tk 
import ttkbootstrap as ttk #noqa
from PIL import ImageTk, Image  #noqa
import customtkinter as ctk
import highscorething
import credits
import pygame
import settings
import quitpython

def get_volume():
    with open("volume.txt", "r") as volume:
        read = volume.readlines(20)
        split = read[1].removeprefix("S: ")
        return float(split)/100

def StartGame():
    global root
    pygame.quit()
    root.destroy()#noqa \
    game.things()
    
def highscores():
    highscorething.start()

def reload():
    root.destroy()
    volume = get_volume()
    main(volume)
    
def Credits():
    credits.start()
    
def Settings():
    settings.begin()

SCREENWIDTH = 800
SCREENHEIGHT = 600
def main(volume):
    global root, SCREENHEIGHT, SCREENWIDTH
    reloadimage = ctk.CTkImage(Image.open("restart-icon.png"))
    root = tk.Tk() #noqa
    pygame.mixer.init()
    music = pygame.mixer.music
    music.load('startmusic.mp3')
    music.set_volume(volume) 
    music.play(-1)
   
    
    screenw = root.winfo_screenwidth()
    screenh = root.winfo_screenheight()

    x =(screenw/2) - (SCREENWIDTH/2)
    y = (screenh/2) - (SCREENHEIGHT/2)

    root.title("Start Screen")
    root.geometry(f"{SCREENWIDTH}x{SCREENHEIGHT}+{int(x)}+{int(y)}")
    root.resizable(False, False)
    root.bind('<Return>', lambda event: StartGame()) #noqa

    font2 = ctk.CTkFont(family='Silom', size=50)
    font3 = ctk.CTkFont(family='Silom', size=25)

    bg = tk.PhotoImage(file = 'start.png') #noqa

    bgimage = tk.Label(master=root, image=bg) #noqa
    bgimage.place(x=0,y=0, relheight=1, relwidth=1) #noqa

    button1 = ctk.CTkButton(master=root, command=StartGame, height=99, width=228, fg_color="transparent", bg_color="#85b964", text = "START", font = font2) 
    button1.place(x = 285, y = 443) 
    button2 = ctk.CTkButton(master=root, command=highscores, height=74, width=171, fg_color="transparent", text = "Highscores",bg_color="#85b964", font = font3) 
    button2.place(x = 93, y = 452)
    button3 = ctk.CTkButton(master=root, command=Credits, height=73, width=171, fg_color="transparent", text = "Credits",bg_color="#85b964", font = font3) 
    button3.place(x = 540, y = 453)
    exit = ctk.CTkButton(master=root, command=root.destroy, height=74, width=171, fg_color="transparent", text = "Exit",bg_color="#85b964", font = font3)
    exit.place(x = 10, y = 295)
    settings = ctk.CTkButton(master=root, command=Settings, height=74, width=171,text="Settings", font=font3,fg_color="transparent",bg_color="#85b964")
    settings.place(y=295,x=620)
    reloadbtn = ctk.CTkButton(master = root, command=reload, height=30, width=30, image=reloadimage, text="", bg_color="#85b964", fg_color="transparent")
    reloadbtn.place(x=765, y=0)

    root.mainloop()
    pygame.quit()
    quitpython.quit()
def begin():
    global volume
    volume = get_volume()
    main(volume)
if __name__ == "__main__":
    begin()
