from tkinter import messagebox
import subprocess
import os
import tkinter as tk
import webbrowser

def main():
    
    global window
    
    window = tk.Tk()
    window.title('Tiktok Botting')
    window.geometry("250x200")  # Adjusted window size
    window.resizable(False, False)
    
    
    window.configure(bg='#121212')
    
    
    font_style = ("Courier New", 12, 'bold')  # Adjusted font size


    label = tk.Label(window, text="Please choose an option", font=font_style, bg='#121212', fg='#00FF00')
    label.place(relx=0.5, rely=0.1, anchor='center')
    
    
    views_button = tk.Button(window, text="Views", command=run_views, width=20, bg='#1E1E1E', fg='#00FF00', font=font_style, relief="flat", bd=0)
    views_button.place(relx=0.5, rely=0.3, anchor='center')


    favorites_button = tk.Button(window, text="Favorites", command=run_favorites, width=20, bg='#1E1E1E', fg='#FF9900', font=font_style, relief="flat", bd=0)
    favorites_button.place(relx=0.5, rely=0.5, anchor='center')


    likes_button = tk.Button(window, text="Likes", command=run_likes, width=20, bg='#1E1E1E', fg='#FF007F', font=font_style, relief="flat", bd=0)
    likes_button.place(relx=0.5, rely=0.7, anchor='center')
    
    
    made_by_label = tk.Label(window, text="Made by Froxxy", font=("Courier New", 10), bg='#121212', fg='lime')  # Adjusted font size
    made_by_label.place(relx=0.5, rely=0.85, anchor='center')
    made_by_label.bind("<Button-1>", open_github)
    
    
    change_color(made_by_label)


def change_color(label):
    colors = ['lime', 'cyan', 'yellow', 'magenta', 'red', 'green', 'blue', 'white']
    current_color = 0


    def animate_color():
        nonlocal current_color
        label.config(fg=colors[current_color])
        current_color = (current_color + 1) % len(colors)
        label.after(250, animate_color)


    animate_color()


def open_github(event):
    webbrowser.open("https://github.com/Froxxy1011") 


def Login():
    

    global PasswordLabel
    global Password
    global Passwordbutton
    global logwindow


    try:
        
        webbrowser.open("https://github.com/Froxxy1011") 
        
        
        logwindow = tk.Tk()
        logwindow.title('Log in')
        logwindow.geometry("250x200")  
        logwindow.resizable(False, False)
        logwindow.configure(bg='#121212')


        PasswordLabel = tk.Label(logwindow, text="Enter the password", font=("Courier New", 12), bg='#121212', fg='lime')
        PasswordLabel.place(relx=0.5, rely=0.2, anchor='center')


        Password = tk.Entry(logwindow, font=("Courier New", 12), width=20, bd=0, relief="flat", show="*")
        Password.place(relx=0.5, rely=0.4, anchor='center')


        Passwordbutton = tk.Button(logwindow, text="Enter", command=checkpassword, font=("Courier New", 12), bg='#00FF00', fg='#121212', relief="flat", bd=0)
        Passwordbutton.place(relx=0.5, rely=0.6, anchor='center')


    except:
        messagebox.showerror("Error", "Something went wrong, Try again...")


def checkpassword():
    Gettext = Password.get()
    if Gettext == "Froxxy1011" or Gettext == "froxxy1011":
        logwindow.destroy()
        main()
        
        
    else:
        messagebox.showerror("Wrong Password", "Incorrect password. Try again...")
        logwindow.destroy()
        Login()


def run_views():
    subprocess.Popen(['python', 'modules/views.py'])


def run_favorites():
    subprocess.Popen(['python', 'modules/favorites.py'])


def run_likes():
    subprocess.Popen(['python', 'modules/hearts.py'])


Login()


os.system("cls && title Zefoy Tool / github:Froxxy1011 && mode con: cols=80 lines=40")

logwindow.mainloop()
