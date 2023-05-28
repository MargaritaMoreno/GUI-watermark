from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk()
window.title("Add a watermark")


def open_image():
    global image_label,image
    file_path = filedialog.askopenfilename(title="Select Image")
    image = Image.open(file_path)
    image = image.resize((int(image.width/2), int(image.height/2)))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(window, image=photo)
    image_label.image = photo
    image_label.place(x=400,y=10)

def open_water():
    global water_label,water
    file_path = filedialog.askopenfilename(title="Select Image")
    water = Image.open(file_path)
    water = water.resize((int(water.width/2), int(water.height/2)))
    photo = ImageTk.PhotoImage(water)
    water_label = Label(window, image=photo)
    water_label.image = photo
    water_label.config(bg="#A6BB8D")
    water_label.place(x=400,y=10)
    scale = Scale(window, label="Modify size", bg="#E5BEEC", from_=0, to=200, orient=HORIZONTAL, length=200, command=lambda x: resize_image(water_label, water, int(x)))
    scale.place(x=50,y=150)
    
               
def resize_image(label, image, scale_value):
    resized_image = image.resize((int(image.width*scale_value/100), int(image.height*scale_value/100)))
    photo = ImageTk.PhotoImage(resized_image)
    label.config(image=photo)
    label.image = photo 

def set_position():
    global water_label
    global image_label
    x = 400
    y = 10
    
    if r1_var.get() == 1: 
        x += image_label.winfo_width() - water_label.winfo_width()
           
    if r2_var.get() == 1: 
        x += image_label.winfo_width() - water_label.winfo_width()
        y += image_label.winfo_height() - water_label.winfo_height()
          
    if r3_var.get() == 1:  
        x = 400
        y = 10  
      
    if r4_var.get() == 1:  
        y += image_label.winfo_height() - water_label.winfo_height()
       
    if r5_var.get() == 1:  
        x += (image_label.winfo_width() - water_label.winfo_width()) / 2
        y += (image_label.winfo_height() - water_label.winfo_height()) / 2
        
    water_label.place(x=x, y=y)
    
def save_images():
    global image, water
    if image and water:
        merged_image = Image.new('RGB', (image.width, image.height))
        merged_image.paste(image, (0, 0))
        merged_image.paste(water, (0, 0))
        file_path = filedialog.asksaveasfilename(title="Save Image", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        if file_path:
            merged_image.save(file_path)
            print("Images saved successfully.")
    
#Display
window.geometry("800x500")
window.config(bg="#E5BEEC")
welcome = Label(text="Hi, welcome to the Watermarking Desktop App \n please select the image and watermark file :) ",
                font=("Garamond",12), padx=5, pady=20)
welcome.config(bg="#E5BEEC")
welcome.place(x=2,y=10)
open_button = Button(window, text="Select Image", command=open_image)
open_button.place(x=50,y=100)

water_button = Button(window, text="Select watermark", command=open_water)
water_button.place(x=50,y=150)

    
r1_var = IntVar()
r2_var = IntVar()
r3_var = IntVar()
r4_var = IntVar()
r5_var = IntVar()

r1 = Checkbutton(window, text="Upper right", bg="#E5BEEC", variable=r1_var, command=set_position)
r2 = Checkbutton(window, text="Lower right", bg="#E5BEEC", variable=r2_var, command=set_position)
r3 = Checkbutton(window, text="Upper left", bg="#E5BEEC", variable=r3_var, command=set_position)
r4 = Checkbutton(window, text="Lower left", bg="#E5BEEC", variable=r4_var, command=set_position)
r5 = Checkbutton(window, text="Center", bg="#E5BEEC", variable=r5_var, command=set_position)

r1.place(x=50, y=300)
r2.place(x=220, y=300)
r3.place(x=50, y=350)
r4.place(x=220, y=350)
r5.place(x=50, y=400)

save_button = Button(window, text="Save Image", command=save_images)
save_button.place(x=145, y=450)

window.mainloop()