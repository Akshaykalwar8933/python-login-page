from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")
#heading
Label(root, text="Python Registration Form",font="ar 15 bold").grid(row=1, column=3)

#field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
age= Label(root, text="Age")
gender = Label(root, text="Gender")
emergency= Label(root, text="Emergency")
payment = Label(root, text="Paymentmood")

#Packing fields
name.grid(row=2, column=2)
phone.grid(row=3, column=2)
age.grid(row=4, column=2)
gender.grid(row=5, column=2)
emergency.grid(row=6, column=2)
payment.grid(row=7, column=2)

#variable storing data
namevalue = StringVar
phonevalue = StringVar
agevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar

#creaing entry field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
ageentry = Entry(root, textvariable=agevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

#packing entry fields
nameentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)
ageentry.grid(row=4, column=3)
genderentry.grid(row=5, column=3)
emergencyentry.grid(row=6, column=3)
paymententry.grid(row=7, column=3)


#creating checkbox

checkbtn = Checkbutton(text="remember me?",variable = checkvalue)
checkbtn.grid(row=7, column= 3)

#subbmit button

Button(text="Submit",command=getvals).grid(row=8, column=3)

root.mainloop()