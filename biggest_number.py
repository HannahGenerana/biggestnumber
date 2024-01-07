# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# pseudocode
import customtkinter
from tkinter import messagebox
import time
from colorama import Fore, Back, Style, init 
init(convert=True) 


# make a window that ask the user to input random numbers
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("300x300")


  # ask the user to input 3 numbers
def inputs():
    first_number = int(entry_first.get())
    second_number = int(entry_second.get())
    third_number = int(entry_third.get())
    print (Fore.LIGHTYELLOW_EX + Style.NORMAL,"First number: ",first_number)
    print (Fore.LIGHTBLUE_EX + Style.NORMAL,"Second number: ",second_number)
    print (Fore.LIGHTGREEN_EX + Style.NORMAL,"Third number: ",third_number)
    


  # check and find the biggest number then print the biggest number
    if first_number >= second_number and first_number >= third_number:
         print (first_number,Fore.MAGENTA + Style.BRIGHT, "is the largest among all inputs") 
    elif second_number >= first_number and second_number >= third_number:
         print (second_number, Fore.MAGENTA + Style.BRIGHT, "is the largest among all inputs")
    else:
         print (third_number, Fore.MAGENTA + Style.BRIGHT, "is the largest among all inputs") 


  # close the window after showing the biggest number
    messagebox.showinfo(title="Random Number", message="Thank you for participating!")
    command = root.destroy()

# custom the window
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=15,padx=25,fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Input 3 random numbers")
label.pack(pady=10,padx=10)

entry_first = customtkinter.CTkEntry(master=frame, placeholder_text="First Number")
entry_first.pack(pady=10,padx=10)

entry_second = customtkinter.CTkEntry(master=frame, placeholder_text="Second Number")
entry_second.pack(pady=10,padx=10)

entry_third = customtkinter.CTkEntry(master=frame, placeholder_text="Third Number")
entry_third.pack(pady=10,padx=10)

button = customtkinter.CTkButton(master=frame, text="Find the largest input number", command=inputs,)
button.pack(pady=25,padx=25)

root.mainloop()