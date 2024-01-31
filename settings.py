import tkinter as tk
import customtkinter as ctk

def start_slider_event(value):
    print(value)
    val_for_start.set(value)
    string_start.set(f"{int(value)}%")
    
def game_slider_event(value):
    print(value)
    val_for_game.set(value)
    string_game.set(f"{int(value)}%")

def Write_to_file():
    with open("volume.txt", "w") as file:
        file.write(f"G: {val_for_game.get()}\nS: {val_for_start.get()}")
    main.destroy()

def start(gamevolume, startvolume):
    global val_for_start, main, val_for_game, string_start, string_game
    main = tk.Tk()
    main.geometry("400x300")
    main.title("Settings")
    
    font = ctk.CTkFont(family="Arial",size=15)
    
    val_for_start = tk.IntVar()
    start_slider = ctk.CTkSlider(main, number_of_steps=10, from_=0, to=100, command = start_slider_event, variable=val_for_start)
    start_slider.set(startvolume)
    start_slider.pack(pady=30)
    
    string_start = tk.StringVar()
    start_label = tk.Label(textvariable = string_start,master = main, font = font)
    start_label.place(x=185,y=5)
    
    val_for_game = tk.IntVar()
    game_slider = ctk.CTkSlider(main, number_of_steps= 10, from_=0, to=100, command=game_slider_event, variable = val_for_game)
    game_slider.set(gamevolume)
    game_slider.pack()
    
    string_game = tk.StringVar()
    game_Label = tk.Label(main, textvariable=string_game, font=font)
    game_Label.place(x=185,y=50)
    
    gamesound = tk.Label(master= main, text= "Game Volume", font="Silom 13 bold")
    gamesound.place(x=4,y=73)
    
    startsound = tk.Label(master= main, text= "Menu Volume", font="Silom 13 bold")
    startsound.place(x=4,y=25)
    
    
    apply = ctk.CTkButton(main, text="apply and close", font = font, command= Write_to_file)
    apply.pack(pady=10)
    
    
    main.mainloop()
def begin():
    with open("volume.txt", "r") as volume:
        times = str(volume.read())
        time = times.split()
        print(time)
    start(int(time[1]),int(time[3]))
if __name__ == "__main__":
    begin()