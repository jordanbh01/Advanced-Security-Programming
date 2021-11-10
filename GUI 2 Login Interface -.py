from tkinter import *
import os

# Globals
global register_account_screen
global login_account_screen
global username
global password
global username_entry
global password_entry
global username_verify
global password_verify
global username_login_entry
global password_login_entry
global login_success_screen
global password_not_recognised_screen
global user_not_found_screen
global main_screen


def register():
    global register_account_screen
    register_account_screen = Toplevel(main_screen)
    register_account_screen.title("Register")
    register_account_screen.geometry("300x300")
    register_account_screen.resizable(True,True)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_account_screen, text="Please enter your account details below", bg="white").pack()
    Label(register_account_screen, text="").pack()
    username_label = Label(register_account_screen, text="Username * ")
    username_label.pack()
    username_entry = Entry(register_account_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(register_account_screen, text="Password * ")
    password_label.pack()
    password_entry = Entry(register_account_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_account_screen, text="").pack()
    Button(register_account_screen, text="Register for an account", width=20, height=1, bg="white",
           command=register_user).pack()


def login():
    global login_account_screen
    login_account_screen = Toplevel(main_screen)
    login_account_screen.title("Login")
    login_account_screen.geometry("300x300")
    login_account_screen.resizable(True,True)
    Label(login_account_screen, text="Please enter your account details below to login").pack()
    Label(login_account_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_account_screen, text="Username * ").pack()
    username_login_entry = Entry(login_account_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_account_screen, text="").pack()
    Label(login_account_screen, text="Password * ").pack()
    password_login_entry = Entry(login_account_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_account_screen, text="").pack()
    Button(login_account_screen, text="Login into your account", width=20, height=1, command=login_verify).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_account_screen, text="Registration Success", fg="green", font=("calibri", 16)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_account_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def password_not_recognised():
    global password_not_recognised_screen
    password_not_recognised_screen = Toplevel(login_account_screen)
    password_not_recognised_screen.title("Success")
    password_not_recognised_screen.geometry("150x100")
    Label(password_not_recognised_screen, text="Invalid Password ").pack()
    Button(password_not_recognised_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_account_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recognised_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x300")
    main_screen.title("Account Login page")
    Label(text="Login or Register for an account", bg="white", width="300", height="2", font=("Calibri", 16)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


if __name__ == '__main__':
    main_account_screen()
