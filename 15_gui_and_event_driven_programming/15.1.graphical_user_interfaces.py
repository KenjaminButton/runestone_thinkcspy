# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

# Creating application window
window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text="Hello World!")
my_label.grid(row=1, column=1)

# Start the GUI Event Loop
window.mainloop()



# 15.1 Graphical User Interfaces
'''
A graphical user interface (GUI) allows a user to interact with a computer
program using a pointing device that manipulates small pictures on a
computer screen. The small pictures are called icons or widgets. Various
types of pointing devices can be used, such as a mouse, a stylus pen, or
a human finger on a touch screen.

We refer to programs that use a graphical user interface as GUI programs.
A GUI program is very different from a program that uses a command line
interface which receives user input from typed characters on a keyboard.
Typically programs that use a command line interface perform a series of tasks
in a predetermined order and then terminate. However, a GUI program creates the
icons and widgets that are displayed to a user and then it simply waits for the
user to interact with them. The order that tasks are performed by the program
is under the user’s control – not the program’s control! This means a GUI program
must keep track of the “state” of its processing and respond correctly to user
commands that are given in any order the user chooses. This style of programming
is called “event driven programming.” In fact, by definition, all GUI programs
are event-driven programs.

'''

# 15.2. GUI Programming
'''
An GUI program has the following structure:

    Create the icons and widgets that are displayed to a user and organize
    them inside a screen window.

    Define functions that will process user and application events.

    Associate specific user events with specific functions.

    Start an infinite event-loop that processes user events. When a user event
    happens, the event-loop calls the function associated with that event.

A GUI program’s interface is composed of widgets displayed in a window. Your
computer’s operating system controls the creation and manipulation of windows
on your computer’s display screen. The operating system also controls the
pointing devices on your computer, such as a mouse or a touch screen.
Therefore, your computer’s operating system is what recognizes events that
happen in a window. Your operating system sends events to your program in
the order they are generated by a user. Your program’s event-loop responds
to these events. All GUI programs have the same event-loop, so there is an
event-loop provided for you and it looks something like this:

    while True:
      # Get the next event from the operating system
      event = get_next_event()

      # Get the function that is assigned to handle this event
      a_function_to_handle_the_event = event-handlers[event]

      # If a function has been assigned to handle this event, call the function
      if a_function_to_handle_the_event:
        a_function_to_handle_the_event()  # Call the event-handler function

      # Stop processing events if the user gives a command to stop the application
      if window_needs_to_close:
        break  # out of the event-loop

Again, you do not implement an event-loop in a GUI program. The event loop has
already been written for you. You make this event-loop work by associating a
function (which is called an event-handler or a callback function) to a specific
event. We will show you how to do this in a few lessons. First, let’s learn how
to create a GUI interface which is the widgets a user sees when a GUI program
runs.
'''

# 15.3. GUI Programming Options
'''
Python does not implement GUI, event-driven-programming in its core
functionality. GUI programming is implemented using imported modules which are
often referred to as “toolkits.” Anyone can implement external modules that
facilitate GUI programming, and many people have. Therefore you have many
options available to you for GUI programming. A partial list of options can be
found at https://docs.python.org/3/faq/gui.html. The following lessons explain
how to use the Tkinter toolkit to create GUI programs. Once you understand how
GUI programming works, you should be able to learn how to use any of the other
available toolkits without much difficulty.
'''

# 15.4. TKinter
'''
TKinter is an abbreviation for “TK interface”. “TK” is a platform independent,
customizable, and configurable GUI library. The Python module TKinter allows
Python programs to use the TK libraries. An overview of TK can be found at
https://en.wikipedia.org/wiki/Tk_(software)_
'''

# 15.5. Tkinter Pre-programmed Interfaces
'''
Tkinter provides a set of standard GUI dialog boxes that can be used with
minimal programming. These are described in the next lesson. (A dialog box
is a small window on a computer screen in which a user is prompted to provide
information or select commands.)
'''

# 15.6. Tkinter Custom Interfaces
'''
Tkinter also provides the functionality to create any user interface imaginable.
To create a custom GUI program you basically do five things:

    - Create instances of the widgets you want in your interface.
    - Define the layout of the widgets (i.e., the location and size of each widget).
    - Create functions that will perform your desired actions on user generated events.
    - Connect your functions to specific user events.
    - Start a GUI event-loop.

Each of these tasks are explain in detail in the following lessons.
Note: All coding examples in these lessons assume you are using Python 3.5 or greater.
'''

# 15.7. Hello World
'''
Many programming languages are introduced to new users by showing them how to
display “Hello world!” on the screen. This is considered to be the simplest
possible program you can write in the language. In that spirit, here is a GUI
program that displays “Hello World!:
'''




# https://stackoverflow.com/questions/55722267/how-to-fix-importerror-cannot-import-name-ttk-in-python-3-6-8
        # python -m tkinter








