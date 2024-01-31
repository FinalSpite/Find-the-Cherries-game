import tkinter as tk
import customtkinter as ctk

def start():
    window = tk.Tk()
    window.title('Credits')
    window.geometry("300x200")
    window.resizable(False, False)
    
    frame = ctk.CTkFrame(window)
    frame.pack(pady=30)
    
    label = tk.Label(frame, text="Game made by Nolan Wolff", font=("Arial Bold", 20))
    label.pack()
    
    close = ctk.CTkButton(window, text="Close", command=window.destroy)
    close.pack(pady=10)
    
    window.mainloop()

if __name__ == '__main__': 
    start()