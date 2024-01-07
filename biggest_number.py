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
root.geometry("300x300")


# ask the user to input 3 numbers
messagebox.showinfo(title="Random Number", message="Welcome! Kindly click 'OK' to proceed.")

first_num = int(input("Kindly input your first random number: "))
second_num = int(input("Kindly input your second random number: "))
third_num = int(input("Kindly input your third random number: "))

# check and find the biggest number
if first_num > second_num and first_num > third_num:
    print (first_num,"is the largest number")

elif second_num > first_num and second_num > third_num:
    print (second_num,"is the largest number")

else:
    third_num 
    print (third_num,"is the largest number")

# print the biggest number
    
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

button = customtkinter.CTkButton(master=frame, text="Find the Largest between the inputs")
button.pack(pady=20,padx=20)

root.mainloop()