from tkinter import *


def create_main():
    main = Tk()
    main.title("GUI shop")
    main.geometry("700x600")
    main.resizable(False, False)

    return main


def create_frame():
    frame = Canvas(main, width=700, height=600)
    frame.grid(row=0, column=0)

    return frame


main = create_main()
frame = create_frame()