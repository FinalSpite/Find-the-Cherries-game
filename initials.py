import tkinter as tk
import customtkinter as ctk 

final = "UNKNOWN"
returned = 1

def submit():
    global final, input_text, returned, main
    final = input_text.get()
    returned = 0
    main.destroy()

def start():
    global final, input_text, returned, main
    main = tk.Tk()
    main.title("HIGHSCORES")
    main.geometry("300x150")
    main.resizable(False, False)
    
    font = ctk.CTkFont(family="Arial", size=20)
    
    label1 = tk.Label(main, text="You got a new HIGHSCORE", font=font)
    label2 = tk.Label(main, text="Input your intials: ", font= font)
    label1.place(x=0, y=0)
    label2.place(x=0, y=50)
    
    input_text = tk.StringVar() 
    input = ctk.CTkEntry(main, width=100, textvariable=input_text)
    input.place(x=0, y=100)
    
    button = ctk.CTkButton(main, text="Submit", command = submit)
    button.place(x=125, y=100)
    
    main.bind('<Return>', lambda event: submit())
    
    main.mainloop()
    print(final)
    return final

if __name__ == "__main__":
    start()
    