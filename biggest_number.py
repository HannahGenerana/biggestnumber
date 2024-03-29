# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# pseudocode
import customtkinter
from tkinter import messagebox
import time
from colorama import Fore, Back, Style, init 
init(convert=True) 


# make a window that ask the user to input random numbers
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("350x380")

# funtions
def close():
    messagebox.showwarning(title="Random Number", message="Are you sure?")
    messagebox.showinfo(title="Random Number", message="Thank you for participating!")
    command = root.destroy()

  # ask the user to input 3 numbers
def inputs():
    first_number = int(entry_first.get())
    second_number = int(entry_second.get())
    third_number = int(entry_third.get())
    time.sleep(1.30)
    print (Fore.LIGHTYELLOW_EX + Style.NORMAL,"First number:",first_number, Fore.RESET)
    time.sleep(1.40)
    print (Fore.LIGHTBLUE_EX + Style.NORMAL,"Second number:",second_number, Fore.RESET)
    time.sleep(1.50)
    print (Fore.LIGHTGREEN_EX + Style.NORMAL,"Third number:",third_number, Fore.RESET)
    

  # check and find the biggest number then print the biggest number
    if first_number >= second_number and first_number >= third_number:
        time.sleep(1.30)
        print (Fore.MAGENTA + Style.BRIGHT,first_number, "is the largest number among all inputs") 
    elif second_number >= first_number and second_number >= third_number:
        time.sleep(1.30)
        print (Fore.MAGENTA + Style.BRIGHT,second_number,  "is the largest number among all inputs")
    else:
        time.sleep(1.30)
        print (Fore.MAGENTA + Style.BRIGHT,third_number,  "is the largest number among all inputs") 


  # close the window after showing the biggest number
    messagebox.showinfo(title="Random Number", message="Thank you for participating!")
    command = root.destroy()

# custom the window
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,fill="both", expand=True)

label_one= customtkinter.CTkLabel(master=frame, text="Welcome!", font=("Helvetica", 25, "bold"))
label_one.pack(pady=5,padx=5)

label_two= customtkinter.CTkLabel(master=frame, text="Kindly input 3 random numbers", font=("Helvetica",20, "italic"))
label_two.pack(pady=5,padx=5)

entry_first = customtkinter.CTkEntry(master=frame, placeholder_text="Enter any random number")
entry_first.pack(pady=10,padx=10)

entry_second = customtkinter.CTkEntry(master=frame, placeholder_text="Enter any random number")
entry_second.pack(pady=10,padx=10)

entry_third = customtkinter.CTkEntry(master=frame, placeholder_text="Enter any random number")
entry_third.pack(pady=10,padx=10)

button_continue = customtkinter.CTkButton(master=frame, text="Find the largest input number", command=inputs,)
button_continue.pack(pady=15,padx=15)

button_close= customtkinter.CTkButton(master=frame, text="Cancel", command=close,)
button_close.pack(pady=15,padx=15)

root.mainloop()