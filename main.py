from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Face_recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 

# first img
        img=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\second.jpg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)


# secong img
        img1=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\first.jpg")
        img1=img1.resize((450,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)
        
#  third img 
        
        img2=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\third.jpg")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=130)
        
        
        # bg image
        
        img3=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\sixth.jpg")
        img3=img3.resize((1400,690),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=690)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION BASED ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        
        
        # student button
        img4=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\student.jpg")
        img4=img4.resize((190,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=150,y=100,width=190,height=190)
    
        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=280,width=190,height=40)    
        
        
        
                # Detect face button
        img5=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\fifth.jpg")
        img5=img5.resize((190,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=450,y=100,width=190,height=190)
    
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=280,width=190,height=40) 
        
                 # Attendance face button
        img6=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\attendance.jpg")
        img6=img6.resize((190,190),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=750,y=100,width=190,height=190)
    
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=280,width=190,height=40) 
        
                    # Help face button
        img7=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\help.jpg")
        img7=img7.resize((190,190),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1050,y=100,width=190,height=190)
    
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=280,width=190,height=40) 
        
        
                  # Train face button
        img8=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\train.png")
        img8=img8.resize((190,190),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=150,y=335,width=190,height=190)
    
        b1_1=Button(bg_img,text="Train data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=515,width=190,height=40) 
        
        
                  # photo button
        img9=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\photo.jpg")
        img9=img9.resize((190,190),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=450,y=335,width=190,height=190)
    
        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=515,width=190,height=40) 
        
                  # Developer button
        img0=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\dev.jpg")
        img0=img0.resize((190,190),Image.ANTIALIAS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        
        b1=Button(bg_img,image=self.photoimg0,cursor="hand2")
        b1.place(x=750,y=335,width=190,height=190)
    
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=515,width=190,height=40) 
        
        
                  # Exit button
        img10=Image.open(r"C:\Users\lenovo\Desktop\Face_recognition_system\images\exit.jpg")
        img10=img10.resize((190,190),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=1050,y=335,width=190,height=190)
    
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=515,width=190,height=40) 
                
if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
