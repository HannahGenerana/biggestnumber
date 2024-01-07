# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# pseudocode
from tkinter import messagebox
from tkinter import*

# ask the user to input 3 numbers
messagebox.showinfo(title="Random Number", message="Welcome! Kindly click 'OK' to proceed.")

first_num = int(input("Kindly input your first random number: "))
second_num = int(input("Kindly input your second random number: "))
third_num = int(input("Kindly input your third random number: "))

# check what is the biggest number
if first_num > second_num and first_num > third_num:
    print (first_num,"is the largest number")

elif second_num > first_num and second_num > third_num:
    print (second_num,"is the largest number")

else:
    third_num 
    print (third_num,"is the largest number")

# print the biggest number
