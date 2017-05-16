#!/usr/bin/env python

# GUI for DryVR
# Ver 0
# Provides Graphical Environment to enter input and get the verification results back graphically

import sys, os
from Tkinter import *


class Application(Frame):
    # Initialize MainFrame
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.init_vars()
        self.create_widgets()
        self.display()

    def init_vars(self):
        self.gen_flag = 0                                                   # flag variable to prevent repetitive work
        self.oldfilename = StringVar()                                      # stores old filename to prevent repetitive work
        self.message = StringVar()                                          # message to display to UI after verification
        self.v1 = StringVar()                                               # filename

        # set it to some value
        self.v1.set("Enter input file name")

    def create_widgets(self):
        # Quit Button
        self.QUIT = Button(self, text='Quit', fg="blue", bg="white", command=self.quit)
        self.QUIT.bind('<Enter>', lambda e: self.QUIT.configure(activeforeground="white", activebackground="blue"))

        # Generate Button
        self.GENERATE = Button(self, text="Generate", command=self.generate_graph)

        # Label to display output
        self.message_label = Label(self, text=self.message)

        # Canvas for graph
        self.cv = Canvas()

        # Input interface for filename of file containing data to verify
        self.file_entry = Entry(textvariable = self.v1)
        self.file_entry.bind('<Key-Return>', self.process)

    # for debudding
    def print_contents(self, event):
        print "hi. contents of entry is now ---->", \
              self.v1.get()

    def process(self, event):
        filename = self.v1.get()
        if self.oldfilename != filename:
            os.system('python main.py inputFile/' + filename)
            self.gen_flag = 1;
            self.display_op()

        self.oldfilename = filename

    def generate_graph(self):
        if self.gen_flag == 1:
            self.graph = PhotoImage(file = r"curgraph.png")
            self.cv.create_image(10, 10, image=self.graph, anchor='nw')
            self.gen_flag = 0
        else:
            pass

    def display_op(self):
        f = open('output/verification.txt', 'r')
        self.message = f.readline() + f.readline() + f.readline() + f.readline()
        f.close()
        # now message_label gets updated to show corresponding output

    def display(self):
        self.grid()
        self.QUIT.grid(row=0, column=3)
        self.GENERATE.grid(row=0, column=2)
        self.cv.grid(row=1, column=0)
        #self.cv.pack(side='top', fill='both', expand='yes')
        self.message_label.grid(row=1, column=2)
        self.file_entry.grid(row=0, column=1)

################################################################################
root = Tk()
app = Application(master=root)
app.master.minsize(1000, 400)
app.mainloop()
#root.destroy()
