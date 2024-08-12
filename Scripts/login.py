# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import os
from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import re
import MySQLdb
from dotenv import load_dotenv
from student_example import set_the_login_or_signup_details
from constants import Constants

load_dotenv()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def check_details_validation(email, password, change_frame, log_canvas, valid_text):
    global values
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    connection = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        passwd=os.getenv("PASSWD"),
        db=os.getenv("DB")
    )
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                   FROM sgdb.studentlogin
                   where Email = %s 
                   AND Password = %s;""", (email, password))

    fetchAll = cursor.fetchall()

    if not fetchAll:
        log_canvas.itemconfig(valid_text, text="Wrong Login information")
    else:
        values = [i for i in fetchAll[0]]
        Constants.studentID = values[0]

        cursor.execute("""SELECT Gender
                FROM sgdb.studentinfo
                Where studentID = %s;""", (Constants.studentID,))
        sex = cursor.fetchall()[0]

        name = values[1] + " " + values[2]
        email = values[3]
        password = values[4]
        dob = values[5]
        grade = values[6]
        gender = "Male" if sex == 0 else "Female"
        list_det = [name, grade, email, gender, dob, password]
        set_the_login_or_signup_details(list_det)
        change_frame("main", values[1])
    """if not email or not password or not re.fullmatch(regex, email):
        log_canvas.itemconfig(valid_text, text="One or more fields are not valid")"""

    connection.close()

# def get_data_from_entries(email, password):
# send the details to a query to find the student and get his details


# window = Tk()
#
# window.geometry("1440x1024")
# window.configure(bg="#FFFFFF")

def show_login_frame(login_frame, show_frame, show_frame_log):
    login_canvas = Canvas(
        login_frame,
        bg="#FFFFFF",
        height=886,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    login_canvas.grid(row=0, column=0, sticky=NSEW)

    login_canvas.image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = login_canvas.create_image(
        720.0,
        512.0 - 70,
        image=login_canvas.image_image_1
    )

    login_canvas.image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = login_canvas.create_image(
        719.0,
        608.0 - 138,
        image=login_canvas.image_image_2
    )

    login_canvas.entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = login_canvas.create_image(
        729.5,
        717.5 - 138,
        image=login_canvas.entry_image_1
    )
    entry_1 = Entry(
        login_frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        show='*',
        highlightthickness=0,
        font=("Intern", 18)
    )
    entry_1.place(
        x=519.0,
        y=698.0 - 138,
        width=421.0,
        height=37.0
    )

    login_canvas.entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = login_canvas.create_image(
        729.5,
        602.5 - 138,
        image=login_canvas.entry_image_2
    )
    entry_2 = Entry(
        login_frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Intern", 18)
    )
    entry_2.place(
        x=519.0,
        y=583.0 - 138,
        width=421.0,
        height=37.0
    )

    login_canvas.button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        login_frame,
        image=login_canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#86BEC9",
        command=lambda: check_details_validation(entry_2.get(), entry_1.get(),
                                                 show_frame_log, login_canvas, validation_text),
        relief="flat"
    )
    button_1.place(
        x=661.0,
        y=792.0 - 138,
        width=118.0,
        height=52.0
    )

    login_canvas.create_text(
        516.0,
        424.0 - 138,
        anchor="nw",
        text="Sign in",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    login_canvas.create_text(
        516.0,
        649.0 - 138,
        anchor="nw",
        text="Enter your password",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    login_canvas.create_text(
        516.0,
        533.0 - 138,
        anchor="nw",
        text="Enter your email",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    validation_text = login_canvas.create_text(
        585.0,
        620.0,
        anchor="nw",
        text="",
        fill="red",
        font=("Inter", 20 * -1)
    )
# window.resizable(False, False)
# window.mainloop()
