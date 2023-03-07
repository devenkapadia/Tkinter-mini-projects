from tkinter import *
import tkinter.messagebox as tmsg

def newFile():
    pass
def openFile():
    pass
def saveFile():
    pass
def quitFile():
    pass

def cut():
    pass
def copy():
    pass
def paste():
    pass

def about():
    pass




if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("720x644")

    # Adding textarea
    textarea = Text(root,font = "arial 19",bg="light grey")
    file = None
    textarea.pack(expand=True,fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root,bg="dark grey")

    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    # To Open already existing file
    FileMenu.add_command(label="Open", command=openFile)

    # To save the current file

    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitFile)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # Edit Menu Ends


    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()
