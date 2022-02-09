from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import pygame
import numpy

# Constants
_HEIGHT, _WIDTH = 500, 900
GAME_TITLE = "Snake Trivia"
BACKDROP_PATH = "drawable/backdrop.png"
LOGO_PATH = "drawable/logo.png"
MAIN_MENU_SNAKE_PATH = "drawable/snake_main_menu.png"
MAIN_MUSIC_PATH = "music/snake_music.mp3"
VOLUME_STATE = "On"


# In game music
pygame.init()
pygame.mixer.music.load(MAIN_MUSIC_PATH)
pygame.mixer.music.play()


# Functions
def toggle_volume():
    if mButtonVolume['text'] == "On":
        pygame.mixer.music.pause()
        mButtonVolume['text'] = "Off"
    else:
        mButtonVolume['text'] = "On"
        pygame.mixer.music.play()


def load_game():
    canvas_Main_Menu.grid_forget()
    mButtonStart.grid_forget()
    mButtonVolume.place_forget()
    pygame.mixer.music.pause()
    to_main_window()
    score_frame_block()


# Init Window
main_window = Tk()

# Init Title, Geometry
main_window.title(GAME_TITLE)
main_window.geometry("900x500")
main_window.resizable(False, False)

# Init Icon
main_window.iconphoto(False, PhotoImage(file=LOGO_PATH))

"""
m     m     a     i i i i  n     n
m m m m    a a       i     n n   n
m  m  m   a a a      i     n   n n
m     m  a     a  i i i i  n     n
"""
# Setting Canvas image
canvas_Main_Menu = Canvas(main_window, width=_WIDTH, height=_HEIGHT)
canvas_Main_Menu.grid(column=0, row=0)
main_backdrop_img = ImageTk.PhotoImage(Image.open(BACKDROP_PATH).resize((_WIDTH, _HEIGHT), Image.ANTIALIAS))
canvas_Main_Menu.background = main_backdrop_img  # Keep a reference in case this code is put in a function.
backdrop_bg = canvas_Main_Menu.create_image(0, 0, anchor=NW, image=main_backdrop_img)

# Main menu snake
# snake_Main_Menu = Canvas(main_window, width=750, height=300)
# snake_Main_Menu.place(relx=0, rely=0, anchor=CENTER)
# main_snake_img = ImageTk.PhotoImage(Image.open(MAIN_MENU_SNAKE_PATH).resize((750, 287), Image.ANTIALIAS))
# snake_Main_Menu.background = main_snake_img  # Keep a reference in case this code is put in a function.
# snake_bg = snake_Main_Menu.create_image(400, 10, anchor=NW, image=main_snake_img)

# Styles
style = Style()
style.configure(
    "mButtonStart.TButton",
    font=("Calibri", 20, "bold"),
    foreground="Green",
    background="white",
    borderwidth=0
)

style.configure(
    "myBoardFrame.TFrame",
    background="red",
    borderwidth=1
)

style.configure(
    "myBoardScoreFrame.TFrame",
    background="blue"
)

# Buttons
"""Start Button"""
mButtonStart = Button(main_window, text="Start", style="mButtonStart.TButton", command=load_game)
mButtonStart.grid(row=0, column=0)

"""Volume Button"""
mButtonVolume = Button(main_window, text="On", command=toggle_volume)
mButtonVolume.place(relx=0.05, rely=0.04, anchor=CENTER)


"""
b          o         a     r r r r       d
b  b    o     o    a   a   r          d  d
b    b  o     o   a a a a  r       d     d
b b b      o     a       a r         d d d
"""


def to_main_window():
    board_frame = Frame(height=500, width=500, style="myBoardFrame.TFrame")
    board_frame.grid(row=0, column=0)
    score_label = Label(board_frame, text='Score = ', font=("Helvetica", 5), height=10, width=100)
    score_label.grid(row=0, column=0, padx=2, pady=2)


def score_frame_block():
    score_frame = Frame(height=500, width=400, style="myBoardScoreFrame.TFrame")
    score_frame.grid(row=0, column=1)


main_window.mainloop()
