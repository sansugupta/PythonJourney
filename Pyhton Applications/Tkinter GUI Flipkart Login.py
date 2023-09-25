#!/usr/bin/env python
# coding: utf-8

# In[18]:


from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
def handle_login():
    email=email_input.get()
    password=password_input.get()
    print(email,password)
    if email=="Nitish@gmail.com" and password=="1234":
        messagebox.showinfo("yayyy","Login Successful")
    else:
        messagebox.showerror("Error","Login Failed")
# Pip intsall pillow
root=Tk()
root.title('Login Form')
root.iconbitmap("favicon.ico")
# root.minsize(500,500)
root.geometry("450x500")
root.configure(background="#0096DC")

img = Image.open("flipkart-logo.png")
resized_img = img.resize((150,100))

img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img) #To print Image
img_label.pack(pady=(10,10)) #To set Image at a Particular Place

text_label=Label(root,text="Flipkart",fg="white",bg="#0096DC")
text_label.pack()
text_label.config(font=("verdana",24))

email_label=Label(root,text="Enter Email", fg="white" , bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",14))

email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15)) #ipady = height

password_label=Label(root,text="Enter Password" ,fg="white",bg="#0096DC")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",14))

password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text="Login Here",bg="white",fg="black",width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))

root.mainloop() #Keeps Gui on the Stuck Screen


# In[ ]:





# In[ ]:




