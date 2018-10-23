
import cv2
from tkinter import *
import PIL.ImageTk
import PIL.Image

background="#f00f0f"
background2="#ff9000"
text="black"
width="200c"
w=None
image=None
C=None

top = Tk()
# photo=PhotoImage(file='thumbnail.jpg')
top.geometry(newGeometry="600x600")
top.title("Welcome to Your Own Virtual DressChecker")
top.configure(bg=background2)
# Message(top,text="Please ensure that you turn on your webcam \n Once it is On Click 'Start Webcam'",justify=LEFT,width=1000,  fg=background).place(height=100,width=600)

Message(top,text="Developed by Force GT  \n                  v1.0 \n                  BETA", justify=LEFT, width=1000, fg=background).place(height=1000,width=600)


def webcam():
    cap = cv2.VideoCapture(0)
    while 1:
     frame=cap.read()[1]
     cv2.imshow('Press Esc To Exit ', frame)
     k = cv2.waitKey(5) & 0xFF
     if k == 27:
        break
    cv2.destroyAllWindows()
    # m2=messagebox.showinfo("Webcam","Select Your Choice")

def match1():
     top.deiconify()
     C = Canvas(top,bg="black" , height=400, width=400)
     top.img=img=PIL.ImageTk.PhotoImage(PIL.Image.open("thumbnail.jpg"))
     b1=Button(text="Go Back",command=callback, padx=10, pady=10, activebackground=background, fg="BLACK").place(x=400,y=500)
     b2 = Button(text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
        x=400, y=550)
     image = C.create_image(50, 50,  image=img)
     b1_window=C.create_window(10,10,window=b1)
     b2_window=C.create_window(10,10,window=b2)
     C.pack()

     #TODO Add different method for different button events.Take match1() for reference.You should replace the attribute command (down there) with the respective function
     #TODO Add images for the different matches

def callback():
    top.withdraw()
    w = Toplevel()
    w.geometry(newGeometry="600x400")
    w.title("Let's Get You Dressed Up")
    Frame(w, width=50, height=250).place(x=800,y=600)
    Label(w, text="Found Some Matches  Here They Are!!",font=("Times New Roman", 16)).pack()
    Button(w, text="Match 1", command=match1 ,activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Match 2", command=quitting, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Match 3", command=quitting, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Match 4", command=quitting, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Go Back",command=initiate, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Quit" , command=quitting, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()


def quitting():
    exit(0)

def initiate():
    top.deiconify()
    top.tkraise()
    Button(top,text="Start Webcam",command=webcam, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200,y=200)
    Button(top,text="Suggest Clothes", command=callback, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200,y=250)
    Button(top,text="Quit", command=quitting, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200,y=300)

if __name__ == '__main__':
    initiate()

top.mainloop()