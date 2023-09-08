# Importing Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
import os
import threading

url = ''
destination = ''

# Creating close menu
def onclosing():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

# Creating Loading Screen
def show_loading_screen():
    loading_screen = Toplevel(root)
    
    # Take the position of main root
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    
    # Adjust the loaing screen to center of the main root
    loading_width = 215
    loading_height = 35
    loading_x = root_x + (root_width - loading_width)
    loading_y = root_y + (root_height - loading_height)

    # Loading screen geometry xd
    loading_screen.geometry(f"{root_x}x{loading_height}+{loading_x}+{loading_y}")
    loading_screen.resizable(False, False)
    loading_screen.title("Loading")

    # Loading Text
    loading_label = Label(loading_screen, text="Converting...")
    loading_label.pack(pady=5)

    return loading_screen

# Creating main converting funtion and thread
def Convert():
    def convert_thread():
        try:
            loading_screen = show_loading_screen()

            url = url_entry.get()
            video = YouTube(url)
            stream = video.streams.filter(only_audio=True).first()

            out_file = stream.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            loading_screen.after(100, loading_screen.destroy)
            messagebox.showinfo("Success", "Video Successfully Downloaded")

        except Exception as e:
            loading_screen.destroy()
            messagebox.showerror("ERROR", 'An error occurred: {}'.format(str(e)))

    thread = threading.Thread(target=convert_thread)
    thread.start()

# Adjusting main root Size etc.
root = Tk()
root.geometry("215x95")
root.resizable(False, False)
root.title("MP3 CO")

url_label = ttk.Label(root, text="Video Link :")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

url_entry = ttk.Entry(root, width=33)
url_entry.grid(padx=6, pady=5)

convert_btn = ttk.Button(root, text="Convert", command=Convert)
convert_btn.grid()

# Closing Screen
def EXECUTE(event):
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()
root.bind("<Escape>", EXECUTE)

root.protocol("WM_DELETE_WINDOW", onclosing)
root.mainloop()
