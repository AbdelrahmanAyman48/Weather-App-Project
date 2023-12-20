# from tkinter import * 
# import webbrowser
# # https://youtu.be/urTOBIXII6s
# class MMenu:
#     def __init__(self, par): 
#         self.par = par
        
#         self.menubar = Menu(self.par)
#         self.file = Menu(self.menubar)
#         self.file.add_command()
        
#         self.menubar.add_cascade (label='Menu', command=self.connect)
#         self.par.config(menu=self.menubar) 
#     def connect(self):
#         webbrowser.open_new('https://www.facebook.com/alaa.jassim.mohammed/')
        
    # Refactoring Changes:
import tkinter as tk
import webbrowser

class MMenu:
    def __init__(self, parent): 
        self.parent = parent
        
        self.menu_bar = tk.Menu(self.parent)
        self.file_menu = tk.Menu(self.menu_bar)
        self.file_menu.add_command(label='Open')

        self.menu_bar.add_cascade(label='Menu', command=self.connect)
        self.parent.config(menu=self.menu_bar) 
    
    def connect(self):
        webbrowser.open_new('https://www.facebook.com/alaa.jassim.mohammed/')
        
# if __name__ == '__main__':
#     root = tk.Tk()
#     m_menu = MMenu(root) 
#     root.mainloop()



# Used import tkinter as tk for clarity and adherence to best practices.
# Renamed variables to follow PEP 8 conventions: par to parent, menubar to menu_bar, file to file_menu.
# Changed self.file.add_command() to self.file_menu.add_command(label='Open') to add a command with a label.
# Used tk.Tk() instead of from tkinter import * for better importing practices.
# Moved the instantiation of MMenu and the Tkinter root window inside an if __name__ == '__main__': guard for best practices regarding script execution.