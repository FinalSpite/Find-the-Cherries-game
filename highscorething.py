import tkinter as tk
import customtkinter as ctk

def get_highscores():
    with open("saveFile.txt", "r") as highscores:
        string = highscores.read()
        split = string.split(" ")
        reversed = split[::-1]
        print(reversed)
        return reversed
        
def highscores_enter():
    with open("saveFile.txt", "a") as highscores:
        highscores.write

def start():
    highscores = get_highscores()
    main = tk.Tk()
    main.geometry("300x200")
    main.title("Highscores")
    main.resizable(False, False)

    frame = tk.Frame(master = main)
    frame.pack(pady=30) 

    label = tk.Label(master = frame, text = f"The highscore is {highscores[1]} \n set by {highscores[0]}!", font= "Arial 25")
    label.pack()
    
    close = ctk.CTkButton(main, text="Close", command=main.destroy)
    close.pack()
    
    main.mainloop()
if __name__ == "__main__":
    start()