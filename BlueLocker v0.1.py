#######################################################################################################################
# Authors: Robert Hosking, Guillermo Ramos-Macias
#######################################################################################################################
# Acknowledgements: Tkinter Code used from thenewboston's series "Python GUI with Tkinter" on YouTube
#######################################################################################################################

from Tkinter import *

import BL_GUI


Version = "V1.0"


def main():
    root = Tk()
    root.title("BlueLocker " + Version)  # title for window

    root.geometry("355x300")  # Dimensions of window
    root.resizable(0,0)  # Disables resizing
    gui = BL_GUI.GUI(root)

    root.mainloop()

main()



