import os, shutil, glob
from os import path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

root_window = Tk()
root_window.title("File Manager")
root_window.geometry("500x430")
list_box = Listbox(root_window, selectmode=SINGLE, font=('arial', 15), width=25)
list_box.insert(END, "There is No File Selected")

toput = "None"


def for_opening_file():
    global list_box, toput
    s = filedialog.askopenfile(initialdir="C:\\Users", title="Choose ur File ", filetype=(
("All files", "*.*"), ("PDF Format", "*.pdf"), ("Executabled Format", "*.exe")))
    if s != None:

        list_box.destroy()
        list_box2 = Listbox(root_window, selectmode=SINGLE, font=('arial', 15), width=25)

        if os.path.isfile(s.name):
            toput = path.basename(s.name)
        else:
            toput = path.dirname(s.name)
        list_box2.insert(END, toput)
        list_box2.grid(row=2, column=0, pady=5)
        toput = s


def for_copying_file():
    global toput, list_box
    if toput != "None":
        try:
            toput = path.abspath(toput.name)
        except:
            print(Exception)
        else:
            to_ = filedialog.askdirectory(initialdir="c:\\", title="Choose A pLace Where u Want TO Copy Ur File")
            try:
                shutil.copy(toput, to_)
            except:
                messagebox.showerror(title="SAME NAMED FILE EXISTS", message="File ALready Existed In Destination PATH")
            else:
                messagebox.showinfo(title="Copied", message="File Copied to " + path.dirname(to_))


def for_moving_file():
    global toput, list_box
    if toput != "None":
        try:
            toput = path.abspath(toput.name)
        except:
            print(Exception)
        else:
            to_ = filedialog.askdirectory(initialdir="c:\\", title="Choose A place Where you want tO move your file")
            try:
                shutil.move(toput, to_)
            except:
                messagebox.showerror(title="FILE EXISTS", message="File already existed in destination PATH")
            else:
                messagebox.showinfo(title="Moved!", message="File Moved to " + path.dirname(to_))


def for_delete_file():
    global toput, list_box
    if toput != "None":
        try:
            toput = path.abspath(toput.name)
        except:
            print(Exception)
        else:
            try:
                os.remove(toput)
            except:
                messagebox.showerror(title="Error ", message="File Already deleted from the path")
            else:
                messagebox.showinfo(title="Deleted!", message="File Deleted Successfully ")


def for_renaming_file():
    global toput
    if toput != "None":
        try:
            extension = path.splitext(toput.name)[1]
        except BaseException as sc:
            pass
        else:
            pass


def for_deleting_folder():
    global toput
    if toput != " None":
        file_folder_location = filedialog.askdirectory()
        try:
            shutil.rmtree(file_folder_location)
        except BaseException as s:
            messagebox.showerror(title="Error!", message="You Have No Permission To Delete This File")
        else:
            messagebox.showinfo(title="Deleted!", message="You Have Deleted  The Folder Successfully")


def for_creating_folder():
    file = filedialog.askdirectory()
    folder_name = simpledialog.askstring("Name For Folder", "Enter The Folder NaME ?")
    joined = path.join(file, folder_name)
    try:
        os.mkdir(joined)
    except:
        messagebox.showerror(title="Error!", message="You Have No Permission To Create Folder")
    else:
        messagebox.showinfo(title="Created!", message="You Have Successfully Created Folder in "+file)


def for_listing_files_in_directory():
    global list_box,toput
    file_location = filedialog.askdirectory()
    list_of_files = os.listdir(file_location)
    list_box.destroy()
    list_box2 = Listbox(root_window, selectmode=SINGLE, font=('arial', 15), width=25)
    if  list_of_files.__len__() > 0:
        for i in list_of_files:
            list_box2.insert(END,i)
            list_box2.grid(row=2, column=0, pady=5)

    toput = file_location





def for_interface_part():
    Name_and_Logo = Label(root_window, text="   Simple File Manager System   ", font=("Elephant", 25, "bold"), justify="left" ,bg='gray')
    Name_and_Logo.grid(row=0, column=0, sticky="w", pady=10)
    list_box = Listbox(root_window, selectmode=SINGLE, font=('arial', 15), width=30, height=5,bg='gray')
    list_box.insert(END, "No file selected")
    list_box.grid(row=1, column=0, pady=5)

    open = Button(root_window, text="Open", command=for_opening_file, width=46, bg='green')
    open.grid(row=3, column=0, pady=5)

    frame = Frame(root_window)
    frame.grid(row=4, column=0,padx=100)

    copy = Button(frame, text="Copy", command=for_copying_file, bg='green',width=10)
    copy.grid(row=0, column=0)

    move = Button(frame, text="Move", command=for_moving_file, bg='green',width=10)
    move.grid(row=0, column=2)
    delete = Button(frame, text="Delete", command=for_delete_file, bg='green',width=11)
    delete.grid(row=0, column=4)
    rename = Button(frame, text="Rename", command=for_renaming_file, bg='green',width=11)
    rename.grid(row=0, column=6)

    create_fle = Button(frame, text="Create Folder", command=for_creating_folder, bg='green',width=10)
    create_fle.grid(row=2, column=0)
    create_folder = Button(frame, text="Delete Folder", command=for_deleting_folder, bg='green', width=10)
    create_folder.grid(row=2, column=2)
    list_files = Button(frame, text="List all Files", command=for_listing_files_in_directory, bg='green',width=10)
    list_files.grid(row=2, column=4)



for_interface_part()
mainloop()
