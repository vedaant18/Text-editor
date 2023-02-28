
from tkinter import *
from tkinter import filedialog as fd,font,PhotoImage
import PIL.Image

import tkinter as tk    
import os 

canvas= tk.Tk()
canvas.title("Text Editor")
canvas.geometry("820x680")
canvas.config(bg="white")
canvas.resizable(True, True)

global open_name_status
open_name_status=False
global selected
selected=False
def full_screen():
  canvas.attributes('-fullscreen',True)
def small_screen():
   canvas.attributes('-fullscreen',False)
   canvas.geometry("820x680")


def cut_text(x):
   
   global selected
   if x:
      selected=canvas.clipboard_get()
   elif text_widget.selection_get():
      selected=text_widget.selection_get()
      text_widget.delete("sel.first","sel.last")
      canvas.clipboard_clear()
      canvas.clipboard_append(selected)


def select(x):
   global selected
   if x:
      selected=canvas.clipboard_get()
      
   if text_widget.selection_get():
      selected=text_widget.selection_get()
      

 


def bolder():
   bold_font=font.Font(text_widget,text_widget.cget("font"))
   bold_font.configure(weight="bold")
   text_widget.tag_configure("bold",font=bold_font)
   current_text=text_widget.tag_names("sel.first")
   if "bold" in current_text:
      text_widget.tag_remove("bold","sel.first","sel.last")
   else:
      text_widget.tag_add("bold","sel.first","sel.last")

def italic():
   italic_font=font.Font(text_widget,text_widget.cget("font"))
   italic_font.configure(slant="italic")
   text_widget.tag_configure("italic",font=italic_font)
   current_text=text_widget.tag_names("sel.first")
   if "italic" in current_text:
      text_widget.tag_remove("italic","sel.first","sel.last")
   else:
      text_widget.tag_add("italic","sel.first","sel.last")




   
def copy_text(x):
   global selected
   if x:
      selected=canvas.clipboard_get()
      
   if text_widget.selection_get():
      selected=text_widget.selection_get()
      canvas.clipboard_clear()
      canvas.clipboard_append(selected)
      
   
def paste_text(x):
   global selected
   if x:
      selected=canvas.clipboard_get()
   else:
        if selected:
            position=text_widget.index(INSERT)
            text_widget.insert(position,selected)

def undo_text(x):
   pass
def redo_text(x):
   pass
   
def save_file():
   global open_name_status
   if open_name_status:
      text_file=open(open_name_status,'w')
      text_file.write(text_widget.get(1.0,END))
      text_file.close()
   else:
      save_as_file()
      
      

def save_as_file():
   text_file=fd.asksaveasfilename(defaultextension=".*",title="Save file",filetypes=[("Python file","*.py"),("Text","*.txt"),("HTML","*.html"),("ALL FILES","*.*")])
   if text_file:
      name=text_file
      canvas.title(f"{name} - Textpad")
      #save file  
      text_file=open(text_file,'w')
      text_file.write(text_widget.get(1.0,END))
      text_file.close()
      
      

    
def add_file():
   text_widget.delete("1.0",END)
   canvas.title("New file")
open_name_status=False
#    status_bar.config("Untitled file")

def open_file():
   
   text_widget.delete("1.0",END)
   text_file= fd.askopenfilename(title="Select file",filetypes=[("Python file","*.py"),("Text","*.txt"),("HTML","*.html"),("ALL FILES","*.*")])
   if text_file:
     global open_name_status
     open_name_status=text_file
   name=text_file
   canvas.title(f"{name} - Textpad") 
   text_file=open(text_file,'r')
   stuff=text_file.read()
   text_widget.insert(END,stuff)
   text_file.close()      
#Xscrollbar 
X_text_scroll=Scrollbar(canvas,orient=HORIZONTAL)

X_text_scroll.pack(side=BOTTOM,fill=X)




#y view scrollbar 
text_scroll=Scrollbar(canvas,orient=VERTICAL)

text_scroll.pack(side=RIGHT,fill=Y)


text_scroll.pack()
#crate text
text_widget=Text(canvas,width=1,height=1,font=("Helvetica",16),selectbackground="#5bb9ff",selectforeground="black",undo=True,yscrollcommand=text_scroll.set,xscrollcommand=X_text_scroll.set,wrap="none")
text_widget.pack(side='top',expand=True,fill='both')
#congig scrollbar 
text_scroll.config(command=text_widget.yview)
X_text_scroll.config(command=text_widget.xview)

#Menu 
app_menu=Menu(canvas)
canvas.config(menu=app_menu)
#File menu 
file_menu= Menu(app_menu,tearoff=False)
app_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=add_file)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=save_file)
file_menu.add_command(label="Save as",command=save_as_file)
file_menu.add_separator()

file_menu.add_command(label="Exit",command=canvas.quit)
#Edit menu
edit_menu= Menu(app_menu,tearoff=False)
app_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=lambda:cut_text(False))
edit_menu.add_command(label="Copy",command=lambda:copy_text(False))
edit_menu.add_command(label="Paste",command=lambda:paste_text(False))
edit_menu.add_command(label="Undo",command=text_widget.edit_undo)
edit_menu.add_command(label="Redo",command=text_widget.edit_redo)
#view menu
view_menu= Menu(app_menu,tearoff=False)
app_menu.add_cascade(label="View",menu=view_menu)
view_menu.add_command(label="Fullscreen",command=full_screen)
view_menu.add_command(label="Restore origin",command=small_screen)

#Format menu 
format_menu= Menu(app_menu,tearoff=False)
app_menu.add_cascade(label="Text",menu=format_menu)
format_menu.add_command(label="Bold",command=bolder)
format_menu.add_command(label="Italic",command=italic)











#edit binding
canvas.bind('<Control-Key-x>',cut_text)
canvas.bind('<Control-Key-c>',copy_text)
canvas.bind('<Control-Key-v>',paste_text)


canvas.mainloop()