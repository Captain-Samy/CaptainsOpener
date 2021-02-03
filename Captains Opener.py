import tkinter as tk
import webbrowser
import pickle
import atexit

root = tk.Tk()

root.title("Captains Opener")

#canvas (How big the app is)
canvas = tk.Canvas(root, width=800,  height=800)
canvas.grid(columnspan=3)


#function for the button to add urls to dictionary
def add_to_dict():
    url_to_add = url_insert.get()
    primary_key = key_insert.get()
    opener_dict[primary_key] = url_to_add


#Listbox of all website's keys
listbox = tk.Listbox(root)
listbox.place(relx=0.5, rely=0.65, anchor="center", relwidth=0.3, height=300)


#create first dictionary
opener_dict = {}


#try to load dictionary
try:
    with open("save_dict.txt", "rb") as myFile:
        opener_dict = pickle.load(myFile)
except:
    with open("save_dict.txt", "wb") as myFile:
        pickle.dump(opener_dict, myFile)

#safe dictionary as txt when closing the application
def save():
    with open("save_dict.txt", "wb") as myFile:
        pickle.dump(opener_dict, myFile)

atexit.register(save)

#show all saved keys in listbox
def display():
    listbox.delete(0,"end")
    for urls in opener_dict:
        listbox.insert("end", urls)

#delete from dictionary
def delete():
    key_to_delete = del_insert.get()
    del opener_dict[key_to_delete]

#Open all urls in the dictionary
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def opener():
    webbrowser.get(chrome_path).open("google.com")
    for key, values in opener_dict.items():
        webbrowser.get(chrome_path).open_new_tab(values)


#instructions
instructions = tk.Label(root, text ="CAPTAIN'S OPENER", font=("Courier",30))
instructions.place(relx=0.5, rely=0.05, anchor="center")

#url insertion
url_insert = tk.Entry(root)
url_insert.place(relx=0.5,rely=0.2, anchor="center", relwidth=0.5, height=20)
url_insert_label = tk.Label(root, text="Insert URL:", font="courier")
url_insert_label.place(relx=0.1, rely=0.185)

#Key insertion
key_insert = tk.Entry(root)
key_insert.place(relx=0.505,rely=0.25, anchor="center", relwidth=0.2, height=20)
key_insert_label = tk.Label(root, text="Insert key/website name:", font="courier")
key_insert_label.place(relx=0.1, rely=0.2345)

#delete insertion
del_insert = tk.Entry(root)
del_insert.place(relx=0.505,rely=0.87, anchor="center", relwidth=0.2, height=20)
del_insert_label = tk.Label(root, text="Insert key to delete:", font="courier")
del_insert_label.place(relx=0.1, rely=0.856)

#button insert to dictionary
insert_button = tk.Button(root, text="Add to opener", command=add_to_dict, font=("Courier",11))
insert_button.place(relx=0.5, rely=0.32, anchor ="center", width=200, height=50)

#button to display all primary keys/websites
display_button = tk.Button(root, text="Display all websites", command=display, font=("Courier",11))
display_button.place(relx=0.5, rely=0.4, anchor ="center", width=200, height=50)

#butto delete
delete_button = tk.Button(root, text="Delete URLS", command=delete, font=("Courier",11))
delete_button.place(relx=0.5, rely=0.91, anchor ="center", width=200, height=25)

#button open
open_button = tk.Button(root, text="OPEN ALL URLS", command=opener, font=("Courier",11))
open_button.place(relx=0.5, rely=0.12, anchor ="center", width=180, height=50)







root.mainloop()