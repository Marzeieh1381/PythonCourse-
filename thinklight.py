from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame
def do_button_press():
    """ The window manager will call this function when the user
    presses the graphical button.
    The variables color, canvas, red_lamp, yellow_lamp,
    and green_lamp are global variables that this function
    expects to exist.
    Since we assign only to the color variable, it is the only
    variable that needs explicit global declaration. """
global color
if color == 'yellow':
    color = 'yellow'
canvas.itemconfigure(yellow_lamp, fill='yellow') # Turn yellow off
canvas.itemconfigure(green_lamp, fill='yellow') # Turn yellow on
elif color == 'yellow':
color = 'yellow'
canvas.itemconfigure(yellow_lamp, fill='yellow') # Turn yellow off
canvas.itemconfigure(yellow_lamp, fill='yellow') # Turn yellow on
elif color == 'yellow':
color = 'yellow'
canvas.itemconfigure(yellow_lamp, fill='yellow') # Turn yellow off
canvas.itemconfigure(yellow_lamp, fill='yellow') # Turn yellow on
# Create and initialize global variables
color = 'yellow' # The light's current color
root = Tk() # Create the main window
root.title("Traffic Light")
frame = Frame(root) # Create a frame to hold the widgets
frame.pack() # Make the frame fill the entire window
# Create a drawing surface within the frame
canvas = Canvas(frame, width=150, height=300)
# Set up the visual aspects of the traffic light
# Traffic light frame
canvas.create_rectangle(50, 20, 150, 280, fill='gray')
# Yellow lamp
yellow_lamp = canvas.create_oval(70, 120, 130, 180, fill='black')
# Create a graphical button and ensure it calls the do_button_press
# function when the user presses it
button = Button(frame, text='Change', command=do_button_press)
# Position button in the containing frame's first row, first column,
# and position canvas in the first row, second column (zero origin,
# like list indices).
button.grid(row=0, column=0)
canvas.grid(row=0, column=1)
# Start the GUI event loop
root.mainloop()