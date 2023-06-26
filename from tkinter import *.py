from tkinter import *

root = Tk()
root.title('Set Image as Background')
root.geometry("800x500")

# Define Image
bg = PhotoImage(file="downloads/homewindow.png")

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add something to the top of our image
my_text = Label(root, text="Welcome!", font=("Helvetica", 50), fg="black")
my_text.pack(pady=50)

# Create a frame - for background to stand out
my_frame = Frame(root)
my_frame.pack(pady=20)


# Add some buttons and now put buttons inside the frame just added
my_button1 = Button(my_frame, text="Exit")
my_button1.grid(row=0, column=0, padx=20)

my_button2 = Button(my_frame, text="Start")
my_button2.grid(row=0, column=1, padx=20)

my_button3 = Button(my_frame, text="Reset")
my_button3.grid(row=0, column=2, padx=20)

root.mainloop()
