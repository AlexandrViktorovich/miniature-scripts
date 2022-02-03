from tkinter import *
import pyglet, os
import pyautogui
import keyboard

pyglet.font.add_file('Helvetica-Rounded-LT-Black.ttf')

window = Tk()

window.resizable(width = False, height = False)
window.geometry("250x180")

window.title("test window")
window.iconbitmap("pic.png")

def get_data( event ):
    start = start_btn_inp.get()
    stop = stop_btn_inp.get()
    while True:
        if keyboard.is_pressed(start):
            pyautogui.tripleClick()
        if keyboard.is_pressed(stop):
            #break
            window.destroy()


start_btn_txt = Label(text = 'Start button',
                  font = 'Helvetica-Rounded-LT-Black 21 bold',
                  #fg = 'black',
                  #bg = 'white',
                  )

start_btn_inp = Entry(window, font = 'Helvetica-Rounded-LT-Black 14 bold',
                      fg = 'black',
                      bg = 'white',
                      relief = 'solid',
                      justify = 'center' )

stop_btn_txt = Label(text = 'Stop button',
                  font = 'Helvetica-Rounded-LT-Black 21 bold',
                  #fg = 'black',
                  #bg = 'white',
                  )

stop_btn_inp = Entry(window, font = 'Helvetica-Rounded-LT-Black 14 bold',
                      fg = 'black',
                      bg = 'white',
                      relief = 'solid',
                      justify = 'center' )

run = Button(text = 'Run!',
             font = 'Helvetica-Rounded-LT-Black 14 bold',
             width =18)

start_btn_txt.pack()
start_btn_inp.pack()
stop_btn_txt.pack()
stop_btn_inp.pack()
run.pack()

run.bind('<Button-1>', get_data )

window.mainloop()