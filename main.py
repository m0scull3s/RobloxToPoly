import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

mode = "rblx_to_pltr"
shirt_path = None
pants_path = None
poly_path = None

def crop_resize(img,x,y,w,h,nw,nh):
    return img.crop((x,y,x+w,y+h)).resize((nw,nh),Image.NEAREST)

def preview(path):
    img = Image.open(path)
    img.thumbnail((300,300))
    tkimg = ImageTk.PhotoImage(img)
    preview_label.config(image=tkimg)
    preview_label.image = tkimg

def set_rblx_mode():
    global mode
    mode = "rblx_to_pltr"
    status_label.config(text="mode: roblox to polytoria")

def set_pltr_mode():
    global mode
    mode = "pltr_to_rblx"
    status_label.config(text="mode: polytoria to roblox")

def select_shirt():
    global shirt_path
    shirt_path = filedialog.askopenfilename(filetypes=[("PNG","*.png")])
    if shirt_path:
        preview(shirt_path)

def select_pants():
    global pants_path
    pants_path = filedialog.askopenfilename(filetypes=[("PNG","*.png")])

def select_poly():
    global poly_path
    poly_path = filedialog.askopenfilename(filetypes=[("PNG","*.png")])
    if poly_path:
        preview(poly_path)

def convert_to_polytoria():

    if not shirt_path or not pants_path:
        status_label.config(text="select shirt and pants")
        return

    shirt = Image.open(shirt_path).convert("RGBA")
    pants = Image.open(pants_path).convert("RGBA")

    out = Image.new("RGBA",(1024,1024),(0,0,0,0))

  
    out.paste(crop_resize(shirt,231,74,128,128,148,292),(439,103))
    out.paste(crop_resize(shirt,427,74,128,128,148,292),(439,519))
    out.paste(crop_resize(shirt,361,74,64,128,90,292),(585,103))
    out.paste(crop_resize(shirt,165,74,64,128,90,292),(351,103))
    out.paste(crop_resize(shirt,231,8,128,64,148,99),(439,7))
    out.paste(crop_resize(shirt,231,204,128,64,148,98),(439,393))

   
    out.paste(crop_resize(shirt,308,355,64,128,68,292),(754,71))
    out.paste(crop_resize(shirt,374,355,64,128,68,292),(820,71))
    out.paste(crop_resize(shirt,440,355,64,128,68,292),(886,71))
    out.paste(crop_resize(shirt,506,355,64,128,68,292),(952,71))
    out.paste(crop_resize(shirt,308,289,64,64,66,64),(754,7))
    out.paste(crop_resize(shirt,308,485,64,64,66,64),(754,361))

    
    out.paste(crop_resize(shirt,217,355,64,128,68,292),(204,71))
    out.paste(crop_resize(shirt,19,355,64,128,68,292),(6,71))
    out.paste(crop_resize(shirt,85,355,64,128,68,292),(72,71))
    out.paste(crop_resize(shirt,151,355,64,128,68,292),(138,71))
    out.paste(crop_resize(shirt,217,289,64,64,66,64),(204,7))
    out.paste(crop_resize(shirt,217,485,64,64,66,64),(204,361))

    
    out.paste(crop_resize(pants,308,355,64,128,68,292),(754,661))
    out.paste(crop_resize(pants,19,355,64,128,68,292),(820,661))
    out.paste(crop_resize(pants,440,355,64,128,68,292),(886,661))
    out.paste(crop_resize(pants,506,355,64,128,68,292),(952,661))
    out.paste(crop_resize(pants,308,289,64,64,66,64),(754,597))
    out.paste(crop_resize(pants,308,485,64,64,66,64),(754,953))

    
    out.paste(crop_resize(pants,217,355,64,128,68,292),(204,661))
    out.paste(crop_resize(pants,19,355,64,128,68,292),(6,661))
    out.paste(crop_resize(pants,85,355,64,128,68,292),(72,661))
    out.paste(crop_resize(pants,151,355,64,128,68,292),(138,661))
    out.paste(crop_resize(pants,217,289,64,64,66,64),(204,597))
    out.paste(crop_resize(pants,217,485,64,64,66,64),(204,953))

    save = filedialog.asksaveasfilename(defaultextension=".png")
    if save:
        out.save(save)
        status_label.config(text="polytoria clothing created")

def deconvert():

    if not poly_path:
        status_label.config(text="select polytoria clothing")
        return

    poly = Image.open(poly_path).convert("RGBA")

    shirt = Image.new("RGBA",(585,559),(0,0,0,0))
    pants = Image.new("RGBA",(585,559),(0,0,0,0))

    def pcrop(x,y,w,h,nw,nh):
        return poly.crop((x,y,x+w,y+h)).resize((nw,nh),Image.NEAREST)

    
    shirt.paste(pcrop(439,103,148,292,128,128),(231,74))   
    shirt.paste(pcrop(439,519,148,292,128,128),(427,74))   
    shirt.paste(pcrop(585,103,90,292,64,128),(361,74))     
    shirt.paste(pcrop(351,103,90,292,64,128),(165,74))     
    shirt.paste(pcrop(439,7,148,99,128,64),(231,8))        
    shirt.paste(pcrop(439,393,148,98,128,64),(231,204))  

    
    shirt.paste(pcrop(204,71,68,292,64,128),(217,355))     
    shirt.paste(pcrop(72,71,68,292,64,128),(85,355))       
    shirt.paste(pcrop(6,71,68,292,64,128),(19,355))        
    shirt.paste(pcrop(138,71,68,292,64,128),(151,355))     
    shirt.paste(pcrop(204,7,66,64,64,64),(217,289))        
    shirt.paste(pcrop(204,361,66,64,64,64),(217,485))      

    
    shirt.paste(pcrop(754,71,68,292,64,128),(308,355))     
    shirt.paste(pcrop(886,71,68,292,64,128),(440,355))     
    shirt.paste(pcrop(820,71,68,292,64,128),(374,355))    
    shirt.paste(pcrop(952,71,68,292,64,128),(506,355))    
    shirt.paste(pcrop(754,7,66,64,64,64),(308,289))        
    shirt.paste(pcrop(754,361,66,64,64,64),(308,485))      

    
    pants.paste(pcrop(204,661,68,292,64,128),(217,355))    
    pants.paste(pcrop(72,661,68,292,64,128),(85,355))     
    pants.paste(pcrop(6,661,68,292,64,128),(19,355))       
    pants.paste(pcrop(138,661,68,292,64,128),(151,355))    
    pants.paste(pcrop(204,597,66,64,64,64),(217,289))      
    pants.paste(pcrop(204,953,66,64,64,64),(217,485))     

    
    pants.paste(pcrop(754,661,68,292,64,128),(308,355))   
    pants.paste(pcrop(886,661,68,292,64,128),(440,355))   
    pants.paste(pcrop(820,661,68,292,64,128),(374,355))    
    pants.paste(pcrop(952,661,68,292,64,128),(506,355))    
    pants.paste(pcrop(754,597,66,64,64,64),(308,289))      
    pants.paste(pcrop(754,953,66,64,64,64),(308,485))      

    os.makedirs("converted_rblx",exist_ok=True)

    shirt.save("converted_rblx/shirt.png")
    pants.save("converted_rblx/pants.png")

    status_label.config(text="roblox shirt and pants exported")

def generate():
    if mode == "rblx_to_pltr":
        convert_to_polytoria()
    else:
        deconvert()

root = tk.Tk()
root.title("roblox to polytoria converter")
root.geometry("520x520")

title = tk.Label(root,text="roblox to polytoria clothing converter",font=("Arial",18))
title.pack(pady=10)

mode1 = tk.Button(root,text="roblox to polytoria",command=set_rblx_mode)
mode1.pack()

mode2 = tk.Button(root,text="polytoria to roblox",command=set_pltr_mode)
mode2.pack()

preview_label = tk.Label(root)
preview_label.pack(pady=10)

shirt_button = tk.Button(root,text="select roblox shirt",command=select_shirt)
shirt_button.pack()

pants_button = tk.Button(root,text="select roblox pants",command=select_pants)
pants_button.pack()

poly_button = tk.Button(root,text="select polytoria clothing",command=select_poly)
poly_button.pack()

generate_button = tk.Button(root,text="GENERATE",bg="blue",fg="white",font=("Arial",20),command=generate)
generate_button.pack(pady=20)

status_label = tk.Label(root,text="")
status_label.pack()

root.mainloop()