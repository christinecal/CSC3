from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Sentence Detective')
root.geometry("800x500")

# Define Image
bg = PhotoImage(file="photoimages/homewindow_resized.png")

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame 
my_frame = Frame(root)
my_frame.pack(pady=20)

# Add some buttons and now put buttons inside the frame just added

"--------Exit button-------"
my_button1 = Button(root, text="Exit",command = root.destroy)
# Set the position of button to top right hand side
my_button1.place(x=760, y=5)

"--------Start button-------"
my_button2 = ttk.Button(root, text="Start")
# Set the position of button to bottom centre
my_button2.place(x=350, y=310)

# Initialising image
root.mainloop()
