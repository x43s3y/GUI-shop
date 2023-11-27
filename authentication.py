from json import loads, dump
from buying_page import display_products
from helper import clean_screen
from canvas import *


def get_all_users_data():
    info_data = []
    with open("..\\db\\users_data.json", "r") as f:
        for line in f:
            info_data.append(loads(line))
        
    return info_data


def render_entry():
    login_btn = Button(
        main,
        text= "Login",
        bg= "purple",
        fg= "white",
        borderwidth= 0,
        width= 20,
        height= 3,
        command= login
    )

    register_btn = Button(
        main,
        text= "Registration",
        bg= "white",
        fg= "purple",
        borderwidth= 0.5,
        width= 20,
        height= 3,
        command= register
    )

    frame.create_window(350, 320, window=login_btn)
    frame.create_window(350, 260, window=register_btn)

def login():
    clean_screen()

    frame.create_text(100, 100, text="Username")
    frame.create_text(100, 150, text="Password")

    frame.create_window(200, 100, window=username_box)
    frame.create_window(200, 150, window=password_box)

    loggin_btn = Button(
        main,
        text= "Login",
        bg = "purple",
        fg = "white",
        command = loggin
    )

    frame.create_window(350, 200, window=loggin_btn)

def loggin():
    if check_login():
        display_products()
    else:
        frame.create_text(200, 200, text="SOMETHING WENT BAD...", fill="red")

def check_login():
    info_data = get_all_users_data()

    for idx in range(len(info_data)):
        username = info_data[idx]["username"]
        password = info_data[idx]["password"]

        if username == username_box.get() and password == password_box.get():
            return True

    return False


def register():
    clean_screen()
    
    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Nickname:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    reg_btn = Button(
        main,
        text="Register",
        bg = "white",
        fg = "purple",
        command = registration
    )
    frame.create_window(300, 250, window=reg_btn)

def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get(),
        "products": []
    }

    if check_reg(info_dict):
        with open("..\\db\\users_data.json", "a") as f:
            dump(info_dict, f)
            f.write('\n')
            display_products()

def check_reg(info):
    for el in list(info.values())[:-1]:
        if el.strip == '':
            frame.create_text(
                300,
                300,
                text = "MISSING IMPORTANT INFO...",
                fill = "red",
                tag = "error",
            )  # type: ignore

            return False

    frame.delete("error")

    return True



first_name_box = Entry(main, bd=0)
last_name_box = Entry(main, bd=0)
username_box = Entry(main, bd=0)
password_box = Entry(main, bd=0, show='*')