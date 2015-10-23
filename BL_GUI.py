################################################
# Author: Robert Hosking,Guillermo Ramos-Macias
################################################
# Acknowledgements: Bluetooth code borrowed from "An Introduction to Bluetooth Programming" by Albert Huang
#                   Tkinter Code used from thenewboston's series "Python GUI with Tkinter" on YouTube
#                   How to set up Tkinter in a class: Brian Oakley on Stack Exchange
################################################
import bluetooth
import ctypes
import webbrowser
from Tkinter import *
import time


class GUI(Frame):

    def __init__(self, master):
        '''
        Initializes the class
        '''
        # make Frame our root
        Frame.__init__(self, master)
        self.grid()

        self.create_widgets()

    def create_widgets(self):
        '''
        Makes all the visible widgets and assigns functionality to them
        '''
        # ***** Frames *****
        self.topframe = Frame(self, width=355, height=50)
        self.topframe.pack(side=TOP)

        self.topframeA = Frame(self.topframe)
        self.topframeA.grid(row=0, column=0)

        self.midframe = Frame(self, width=355, height=50)
        self.midframe.pack()

        self.midframeA = Frame(self.midframe)
        self.midframeA.grid(row=1, column=0)

        self.midframeB = Frame(self.midframe)
        self.midframeB.grid(row=2, column=0)

        self.midframeC = Frame(self.midframe)
        self.midframeC.grid(row=0, column=0)

        self.bottomframe = Frame(self)
        self.bottomframe.pack(side=BOTTOM)

        self.bottomframeA = Frame(self.bottomframe)
        self.bottomframeA.pack(side=BOTTOM)

        self.bottomframeB = Frame(self.bottomframe)
        self.bottomframeB.pack(side=BOTTOM)

        # ***** Labels *****
        self.directionLabel = Label(self.midframeC, text="Device to connect:")
        self.directionLabel.grid()

        BTC = "1ABRMSCKPtVFfKigzGUGzyXngL3TZcNvEi" #This is my Bitcoin Wallet address. Donate!
        self.BTCaddress = Label(self.bottomframeA, text=BTC)
        self.BTCaddress.grid(column=1, row=3)

        # ***** Drop-Down Menu  *****
        lst1 = self.chop_Scan()
        self.var = StringVar(self.midframeC)
        self.var.set("[Choose a Device]")
        def refresh():                                          # Refresh the devices in the drop down menu
            self.stvariable.set("Refreshed list of devices!")
            import Tkinter as tk
            self.var.set('')
            self.drop['menu'].delete(0, 'end')

            #insert new choices
            new_choices = self.chop_Scan()
            for choice in new_choices:
                self.drop['menu'].add_command(label=choice, command=tk._setit(self.var, choice))

        self.drop = OptionMenu(self.midframeC, self.var, *lst1)
        self.drop.grid(row=0, column=1)


        # ***** Images *****
        banner = PhotoImage(file=("blulocker.gif"))
        self.banner_image = Label(self.topframe, image=banner)
        self.banner_image.image = banner
        self.banner_image.grid()

        # ***** Buttons *****
        self.scanButton = Button(self.midframeA, padx=121, text="Refresh", bg="#0099FF", fg="white", command=refresh)
        self.scanButton.grid(row=1)

        self.connectButton = Button(self.midframeB, padx=118, text="Connect", bg="#0099FF", fg="white",command=self.Connect)
        self.connectButton.grid(row=1)

        twitter_icon = PhotoImage(file=("twitter-icon.gif"))
        self.twitterButton = Button(self.bottomframeA, image=twitter_icon, command=self.TwitterOpenURL)
        self.twitterButton.image = twitter_icon
        self.twitterButton.grid(column=3, row=3)

        bitcoin_icon = PhotoImage(file="BTC-icon.gif")
        self.BTC_image = Button(self.bottomframeA, image=bitcoin_icon, command=self.BTCOpenURL)
        self.BTC_image.image = bitcoin_icon
        self.BTC_image.grid(row=3)

        # ***** Checkbutton *****
        self.remember = Checkbutton(self.midframe, text="Remember Device")
        self.remember.grid()

        # ***** Status Bar ******
        self.stvariable = StringVar()
        self.status = Label(self, textvariable=self.stvariable, bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

        # ***** Function Definitions ******



    def Scan(self):
        '''
        returns a list of lists. Each list is formatted as following: (User-friendly-name, Bluetooth Address)
        '''
        nearby_devices = bluetooth.discover_devices()
        open_devices = []
        for bdaddr in nearby_devices:
            device = ((bluetooth.lookup_name(bdaddr)), bdaddr)
            open_devices.append(device)

        return open_devices

    def chop_Scan(self):
        '''
        returns only the user-friendly names from the devices in Scan()
        '''
        list_of_names = []
        for i in self.Scan():
            list_of_names.append(i[0])

        return list_of_names

    def Connect(self):
        self.stvariable.set(("Lost connection with " + self.var.get()+"and locked workstation!"))
        self.sleep_state()

    def sleep_state(self):
        '''
        This is the process that checks if the device is in range
        '''
        if self.var.get() == "[Choose a Device]":
            self.stvariable.set("No device chosen!")
        else:
            if self.var.get() not in self.chop_Scan():
                self.lock()

            else:
                self.sleep_state()

    def lock(self):
        '''
        Locks the computer
        '''
        ctypes.windll.user32.LockWorkStation()

    def TwitterOpenURL(self):
        '''
        Opens my twitter page... Follow me!
        '''
        url="http://goo.gl/wWtBif"
        webbrowser.open_new(url)

    def BTCOpenURL(self):
        '''
        opens the URL for the bitcoin information webpage
        '''
        url="https://bitcoin.org/en/"
        webbrowser.open_new(url)






