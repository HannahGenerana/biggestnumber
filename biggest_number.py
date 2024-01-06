# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# pseudocode
from tkinter import messagebox
from tkinter import*

# ask the user to input 3 numbers
window=Tk()
window.title("Random Number")
window.geometry("600x200")

l1=Label(window, text="Kindly input some random numbers below.", font=(14))
l2=Label(window,text="First Number:", font=(14))
l3=Label(window, text="Second Number:", font=(14))
l4=Label(window,text="Third Number:", font=(14))
l1.grid(row=0,column=0,padx=5,pady=5)
l2.grid(row=1,column=0,padx=5,pady=5)
l3.grid(row=2,column=0,padx=5,pady=5)
l4.grid(row=3,column=0,padx=5,pady=5)

first_num=StringVar()
second_num=StringVar()
third_num=StringVar()
t1=Entry(window,textvariable=first_num,font=(14))
t2=Entry(window,textvariable=second_num,font=(14))
t3=Entry(window,textvariable=third_num,font=(14))
t1.grid(row=1,column=1)
t2.grid(row=2,column=1)
t3.grid(row=3,column=1)

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
