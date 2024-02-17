## User uses Character User Interface (CUI) to execute a command.

## User uses Graphics User Interface (GUI) to execute a command

## Python uses 'tkinter' to create a graphics programs.

#! 'tkinter' represents 'tool kit interface'

#! 'TCL' represents 'Tool Command Language' - a dynamic programming language
#! 'TK' represents 'Tool Kit' language to generate graphic.

#% Basic steps involved in GUI programs:

#! Create a root window. The root window is the top level window that
#! provides rectangular space on the screen where one can display text,
#! colors, images, etc.

#! Allocate space for use by creating a canvas or frame. The canvas and
#! frame are child window.

#! Canvas is used for displaying drawing like lines, arcs circles, shapes,
#! etc. Frames are used for displaying components like push buttons, 
#! checkboxes, menus, etc. These components are called 'widgets'

#! User clicks on widget creates an event. One needs to respond to the
#! events by performing the desired tasks.


#@ Root Window

#! A program to create root window or top level window

# from tkinter import Tk

# ## create root window

# root = Tk()

# ## wait and watch for any events that may take place in the root window

# root.mainloop()


#! A program to create root window with some options

# from tkinter import Tk

# root = Tk()

# ## set window title
# root.title('My Window')

# ## set window size
# root.geometry('400x300')   ## leave no space between numbers.

# ## set window icon
# root.wm_iconbitmap('Apple.ico')

# ## display window and wait for any events
# root.mainloop()

#@ Fonts and colors

#! in Tkinter, fonts are mentioned using a Tuple that contains font
#! family name, size and font style.

#! if the font size is mentioned as Positive number, it indicates
#! size in points. If the size is a negative number, it indicates
#! size in pixels.

#& A program to know the available font families

# from tkinter import Tk
# from tkinter import font

# root = Tk()

# ## set window title
# root.title('My Window')

# ## set window size
# root.geometry('400x300')   ## leave no space between numbers.

# ## set window icon
# root.wm_iconbitmap('Apple.ico')

# ## get all supported font families
# list_fonts = list(font.families())

# ## display them
# print(list_fonts)

# ## display window and wait for any events
# root.mainloop()


#@ Working with containers

#! A container is a component that is used as a place where drawings or widgets can be displayed.
#! In other words, a container is a place that displays the output to the user.

#& Containers:
#% Canvas: used for drawing shapes like, lines, curves, arcs and circles.

#% Frames: used for displaying widgets like buttons, check_buttons and menus.

#@ Canvas

#* Cursor shape: arrow, box_spiral, center_ptr, clock, coffee_mug, cross, cross_reverse,
#* crosshair, diamond_cross, dot, double_arrow, exchange, hand1, hand2, heart, left_ptr,
#* mouse, pencil, plus, question_arrow, right_ptr, star, tcross, top_side, umbrella, watch,
#* xterm, X_cursor

#% colors in the canvas can be displayed directly by their names or specify colors using
#% hexadecimal numbers.

#~ Once the canvas is created, one draw any shapes on the canvas.

#~ To create a line, use create_line() method.

#~ id = c.create_line(50, 50, 200, 50, 200, 150, width=4, fill='white')

#% This create a line with the connecting points (50,50), (200,50) and (200,150).

#% 'width' specifies the width of the line. Default width is 1 pixel.

#% 'fill' specifies the color of the line.

#& To create an oval, we can use create_oval() method. An oval is also called eclipse.
#& id = c.create_oval(100, 100, 400,300, width=5, fill='yellow', outline='red', activefill='green')

#% Here, (100,100) represents top left co-ordinates and (400, 300) represents bottom lower
#% co-ordinates.

#% Width represents width of the oval in pixels.

#% fill represents the color to fill.

#% 'outline' represents the color to be used for the border.

#% 'activefill' represents the color to be filled when the mouse is placed on the oval.

#& To create a polygon, use create_polygon() method.

#% Here, (10,10), (200,200), (300,200) and then the last point is again connected to the 1st point
#% i.e (10,10)

#% The 'smooth' can become 0 to 1. If 0, it means polygon with sharp edges and 1 means polygon with
#% smooth edges.

#& To create a rectangle, use create_rectangle() method.

#% Here, (500,200) represent top left co-ordinates. (700,600) represent lower bottom coordinate.


#& To create text in the canvas, use create_text() method.

#& To create an arc, use create_arc() method

#% id = c.create-arc(100, 100, 400, 300, width=3, start=270, extent=180, outline='red', style='arc')

#% Here, the arc will start at 90 degrees and extend for another 180 degrees.

#! A GUI program that demonstrates the creation of various shapes in canvas.

# from tkinter import Tk
# from tkinter import Canvas

# root = Tk()

# ## Create Canvas as a chile to root window

# c =  Canvas(root, bg='blue', height= 700, width=1200, cursor='pencil')

# ## Create a line in the canvas
# id = c.create_line(50,50,200,50,200,150, width=4, fill='aqua')

# ## Create an oval in the canvas
# id = c.create_oval(100, 100, 400, 300, width=5, fill= 'yellow', outline = 'red', activefill='green')

# ## Create a polygon in the canvas
# id = c.create_polygon(10,10,200,200,300,200, width=3, fill='green', outline='red', smooth=1,
#      activefill='lightblue')

# ## Create a rectangle in the canvas
# id = c.create_rectangle(500,20,700,600,width=2, fill='lightgrey', outline='white',
#      activefill = '#00BFFF')

# ## create some arc in the canvas
# id = c.create_arc(800, 100, 1200, 300, width=5, start=90, extent=180, outline='red', style='arc')

# ## create some text in the canvas
# fnt = ('hack', 40, 'bold italic underline')
# id = c.create_text(500,100, text='My Canvas', font= fnt, fill = 'green', activefill = 'purple')

# ## Add canvas to the root window
# c.pack()

# ## wait for any events
# root.mainloop()

#! create arc in different shapes

# from tkinter import Tk
# from tkinter import Canvas

# root = Tk()

# c = Canvas(root,bg='White', height=700, width=1200)

# id = c.create_arc(100, 100, 400, 300, width=5, start=270, extent= 180,
#      outline= 'red', style='arc')

# id = c.create_arc(500, 100, 800, 300, width=5, start=90, extent= 180,
#      outline= 'aqua', style='arc')

# id = c.create_arc(100, 400, 400, 600, width=5, start=0, extent= 180,
#      outline= 'blue', style='arc')

# id = c.create_arc(500, 400, 800, 600, width=5, start=180, extent= 180,
#      outline= 'pink', style='arc')

# id = c.create_arc(900, 400, 1200, 600, width=5, start=90, extent= 90,
#      outline= 'black', style='arc')

# c.pack()

# root.mainloop()


#! One can create an image in the canvas with the help of create_image() method

#% Load the image into a file using 'PhotoImage' class.

#! A program to display images in the canvas

# from tkinter import Tk
# from tkinter import Canvas
# from tkinter import PhotoImage
# from tkinter import NE, E, SE, S, SW, W, NW, N

# root = Tk()

# c = Canvas(root, bg='black', height=700, width=1200)

# ## Copy images into files

# file1 = PhotoImage(file='cat.gif')
# file2 = PhotoImage(file='husky.gif')

# ## Display the images in the canvas in NE direction
# ## When mouse placed on cat image, we can see the husky image

# id = c.create_image(500, 200, anchor=N, image=file1, activeimage=file2)

# ## Display some text below the image

# id = c.create_text(350, 150, text='This is a cute photo', font=('Times New Roman',
#      30, 'bold'), fill='blue')

# c.pack()

# root.mainloop()

#! A program to display drawing in the Canvas

# from tkinter import Tk
# from tkinter import Canvas
# from tkinter import PhotoImage
# from tkinter import NW

# root = Tk()

# c = Canvas(root, bg='#091e42', height=700, width=1200)

# ## Create the house

# c.create_polygon(600,350,700,300,800,350,800,500,600,500, width=2, fill='yellow',
#   outline='red')
# c.create_line(600, 350, 750, 475, fill='red')
# c.create_rectangle(650,375, 750,475, fill='red')

# ## create 3 bushes at left side of the house
# x1,y1 = 0,450
# x2,y2 = 200,550
# for i in range(3):
#     c.create_arc(x1,y1,x2,y2,start=0,extent=180,fill='green')
#     x1 += 200
#     x2 += 200
    
# ## create 2 bushes at the right of the house

# c.create_arc(800,450,1000,550, start=0, extent= 180, fill='green')
# c.create_arc(1000,450,1200,550, start=0, extent= 180, fill='green')

# ## Display moon image
# file1 = PhotoImage(file='moon.gif')
# c.create_image(10,10, anchor=NW, image=file1)

# ## Display some text below the image
# id = c.create_text(600, 600, text='My Sweet Home', font=('Hack', 30, 'bold'),
#      fill='magenta')

# ## Add canvas to the root
# c.pack()

# ## wait for any events
# root.mainloop()

#@ Frame

#! A frame is similar to a canvas that represents a rectangular area where some
#! text or widgets can be displayed.

#! To create a frame, we need to create an object of Frame class:

#% f= Frame(root, height=400, width=500, bg='yellow', cursor='crosshair')

#! A GUI program to display a frame in the root window

# from tkinter import Tk
# from tkinter import Frame


# root = Tk()

# ## Give a title to the root window
# root.title('My Frame')

# ## Create a Frame as child to the root window
# f = Frame(root, height=400, width=500, bg='yellow', cursor='crosshair')

# ## Attach the Frame to the root window
# f.pack()

# ## wait for any events
# root.mainloop()

#@ Widgets

#! A push button is a widget which is an object of Button Class.
#! label is a widget that is widget that is an object of Label Class.

#! Once a widget is created, it should be attached to Canvas or frame.

#* Working with widgets takes four steps:

#! Create the required widget.
#! To create a push button, we create an object of Button class as:
#% b= Button(f, text="My Button')
#! Here 'f' is a Frame to which a button is attached.
#! 'My Button' the text that is displayed on the button.

#! Upon user interaction with the widget, an event is generated.
#! clicking a push button is an event, which are handled by writing functions or
#! routines.
#! These functions are called in response to the event.
#! Hence, are known as 'callback handlers' or event handlers'.

#! A function that may be called in response to button click.
#% def button(self):
#% print('You clicked me!')

#! When the user clicks on the push button, that clicking event should be
#! linked with the callback handler' function. Then only the button widget
#! will appear as it is performing some task.

#! lets bind button click with the function as:
#% b.bind('<Button-1>', buttonClick)

#! Here, 'b' represents the push button.
#! <Button-1> represents the left mouse button.
#! When the user clicks left mouse button, the 'buttonClick' function is called.

#! Entering a text or pressing the mouse button is called events.
#! These events are continuously monitored with the help of a loop, called
#! 'event loop'.


#! The propagate() method in Python GUI is used to control how a widget's size
#! is determined. By default, widgets will propagate their size to their parent widget.
#! This means that if a widget is placed in a frame, the frame will resize itself to fit the widget.
#! The propagate() method can be used to disable this behavior.
#! To disable propagation, you can call the propagate() method with the argument False or 0.


#% root.mainloop()

#@ Button Widget

#% b = Button(f, text='My Button', width=15, height=2, bg='yellow', fg='blue',
#%     activebackground= 'green', activeforeground='red' )

# from tkinter import Tk
# from tkinter import Frame as f
# from tkinter import Button
# from tkinter import PhotoImage

# #! To display an image on the button as:
# file1 = PhotoImage(file='cat1.gif')

# ## Create a push button with image
# b = Button(f, image=file1, width=150, height=100, bg='yellow', fg='blue',
#     activebackground='green', activeforeground='red')

#! A program to create a push button and bind it with an event handler function.

# from tkinter import Tk
# from tkinter import Frame
# from tkinter import Button

# ## Method to be called when the button is clicked
# def ButtonClick(self):
#     print('You have clicked me!')

# ## Create a root window
# root = Tk()

# ## create frame as child to the root window
# f = Frame(root, height=200, width=300)

# ## ensure the frame does not shrink.
# f.propagate(0)

# ## attach frame to the root window
# f.pack()

# ## create a push button as child to the frame.
# b = Button(f, text='My Button', width=15, height=2, bg='yellow', fg='blue',
#     activebackground='green', activeforeground='red')

# ## attach button to the frame.
# b.pack()

# ## Bind the left mouse button with the method to be called.
# b.bind('<Button-1>', ButtonClick)

# ## the root window handles the mouse click event.
# root.mainloop()

#! A program to create a push button and bind it to an event handler
#! function using command option.

# from tkinter import Tk
# from tkinter import Frame
# from tkinter import Button

# class MyButton:
#     def __init__(self,root):
#         ## create a frame as chile to the root window
#         self.f = Frame(root, height=200, width=300)
#         self.f.propagate(0)
        
#         ## attach the frame to the root window
#         self.f.pack()
        
#         ## create a push button as a chile to frame and bind it to
#         ## frame.
        
#         self.b = Button(self.f, text='My Button', width=15, height=2,
#         bg='#DCDCDC', fg= 'blue', activebackground='green',
#         activeforeground='red',command=self.buttonClick)
        
#         ## attach button to the frame
#         self.b.pack()
        
#     ## method to be called when the button is clicked
#     def buttonClick(self):
#         print('You have clicked me!')
        
# ## create a root window
# root = Tk()

# ## Create an object to my class button

# mb = MyButton(root)

# ## The root window handles the mouse click event.
# root.mainloop()

#! a program to create three push buttons and change the background of the frame
#! according to the button clicked by the user.

# from tkinter import Tk
# from tkinter import Frame
# from tkinter import Button

# class MyButton:
#     def __init__(self, root):
#         self.f = Frame(root, height=400, width=500)
#         self.f.propagate(0)
#         self.f.pack()
#         ## Create three push buttons and bind them to buttonClick method and pass a number.
#         self.b1 = Button(self.f, text='Red', width=15, height=2,command=lambda : self.buttonClick(1))
#         self.b2 = Button(self.f, text='Green', width=15, height=2,command=lambda : self.buttonClick(2))
#         self.b3 = Button(self.f, text='Blue', width=15, height=2,command=lambda : self.buttonClick(3))
#         ## attach the buttons to the frame
#         self.b1.pack()
#         self.b2.pack()
#         self.b3.pack()
        
#     def buttonClick(self, num):
#         if num == 1:
#             self.f['bg'] = 'red'
#         elif num == 2:
#             self.f['bg'] = 'green'
#         else:
#             self.f['bg'] = 'blue'
            
# ## Create root window
# root = Tk()

# ## Create an object to the MyButton Class
# mb= MyButton(root)

# ## the root window handles the mouse click event
# root.mainloop()


#@ Arranging widgets in the Frame.

#* Pack layout manager:

#! Arranging the widgets in the Frame is called, 'layout management.' 
#! There are 3 types of layout management:

#! Pack layout manager
#! grid layout manager
#! place layout manager

#! Pack layout manager uses pack() method. This method is useful to associate a widget
#! with its parent component.

#! while using pack() method, we can mention the position of the widget using 'fill' or 'side'
#! options.
#% b.pack(fill=X)           ## Occupy the frame horizontally
#% b.pack(fill=Y)           ## Occupy the frame vertically
#% b.pack(fill=BOTH)        ## Occupy in both the directions.
#% b.pack(fill=NONE)        ## Widget should be displayed as it is. This is default value.



#! Along with 'fill' option, we can use 'padx' and 'pady' options that represent how much space
#! should be left around the widget horizontally and vertically.

#% b1.pack(fill=Y, padx=10, pady=15) ## occupy vertically. Space on x-axis 10 px & on y-axis 15 px

#% b2.pack(fill=X, padx=10, pady=15) ## occupy horizontally. Space on x-axis 10 px & on y-axis 15 px.

#% b3.pack(fill=X) ## occupy horizontally. No space outside the widget
#% b4.pack(fill=X) ## occupy horizontally. No space outside the widget



#! pack() method can take another option 'side' which is used to place the widgets side by side.
#! 'side' can take the values LEFT, RIGHT, TOP or BOTTOM. The default value is top.

#% b1.pack(side=LEFT, padx=10, pady=15) ## align towards left with 10px & 15px spaces.
#% b2.pack(side=LEFT, padx=10, pady=15) ## align towards left with 10px & 15px spaces.
#% b3.pack(side=RIGHT) ## align towards right with 0 px space around the widget.
#% b4.pack() ## align towards top with 0 px space around the widget

#* Grid Layout Manager:

#! The position of a widget is defined by a row and column number.
#! The size of the table is determined by the grid layout manager depending on the widget size.

#% b1.grid(row=0, column=0, padx=10, pady=15) ## display in 0th row, 0th column with spaces around.
#% b2.grid(row=0, column=1, padx=10, pady=15) ## display in 0th row, 1st column with spaces around.
#% b3.grid(row=0, column=2) ## display in 0th row, 2nd column without spaces around.
#% b4.grid(row=1, column=3) ## display in 1st row, 3rd column without spaces around.


#* Place Layout Manager

#! Uses place() method to arrange the widgets.
#! The place() method takes x and y coordinates of the widget along with width and height
#! of the window where the widget has to be displayed.

#% b1.place(x=20, y=30, width=100, height=50) ## display at (20, 30) co-ordinates in the
#%          window 100 pxwidth and 50 pxheight.
#% b2.place(x=20, y=100, width=100, height=50) ## display at (20, 100)
#% b3.place(x=200, y=100, width=100, height=50) ## display at (200, 100)
#% b4.place(x=200, y=200, width=100, height=50) ## display at (200, 100)



#@ Label Widget

#! A label can display one or more lines of text that can not be modified.
#! A label is created as an object of label class

#% lbl = Label(f, text='Welcome to Python', width=20, height=2, font=('Times New Roman', -30,
#%       'bold underline'),fg='blue', bg='yellow')

#! Here f represents the frame object to which the label object is created as child.
#! 'text' represents the the text to be displayed.
#! 'width' represents the width of the label in number of characters.
#! 'height' represents the height of the label in number of lines.
#! 'font' represents a tuple that contains font name, size and style.

#! A program to display a label upon clicking a push button.

# from tkinter import Tk
# from tkinter import Frame
# from tkinter import Button
# from tkinter import Label

# class MyButtons:
#     def __init__(self,root):
#         self.f = Frame(root, height=350, width=500)        
# ## Disable the frame from shrinking
#         self.f.propagate=False
# ## Attach the frame to the root window
#         self.f.pack()
# ## create a push button and bind it to the buttonClick method
#         self.b1 = Button(self.f, text='Click Me', width=15, height=2, command=self.buttonClick)
# ## Create another button that closes the root window upon clicking
#         self.b2 = Button(self.f, text='Close', width=15, height=2, command=root.destroy)
# ## attach buttons to the frame
#         self.b1.grid(row=0, column=1)
#         self.b2.grid(row=0, column=2)
# ## The event handler method
#     def buttonClick(self):
#         self.lbl = Label(self.f, text='Welcome to Python', width=20, height=2,
#             font=('Courier', -30, 'bold underline'), fg='blue')
# ## attach the label to the frame
#         self.lbl.grid(row=2, column=0)
# ## Create the root window
# root = Tk()

# ## create an object the MyButton class
# mb = MyButtons(root)

# ## The root handles the mouse click events
# root.mainloop()

#@ Message Widget

#! A message is displayed in multiple lines whereas a label is displayed in a single line.

#! To create a message, we need to create an object of the Message class as:

#% m = Message(f, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit,
#%     sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
#%     ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
#%     ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
#%     velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
#%     cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum',
#%     width=300, font=('Arial',20,'bold italic'),fg='dark goldenrod')

#! A program to display a message in the frame.

# from tkinter import Tk
# from tkinter import Frame
# from tkinter import Message
# from tkinter import LEFT

# class MyMessage:
#     def __init__(self, root):
#         self.f = Frame(root, height=500, width=500)
#         self.f.propagate = False
#         self.f.pack()
#         ## Create a message widget with Lorem Ipsum text
#         self.m = Message(self.f, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',width=500, font=('Fira Code', 20, 'bold italic'), fg='dark goldenrod')
#         ## Attach message to the frame
#         self.m.pack(side=LEFT)
# ## Create root window
# root = Tk()

# ## Create an object to MyMessage
# mm = MyMessage(root)

# ## root window handles the mouse click event
# root.mainloop()


#@ Text Widget

#! Text widget can display multiple lines of text in different colors and fonts.

#! It is possible to insert text into text widget, modify it or delete it.

#! Also display images in text widget.

#! Create a text widget by creating an object to Text class.

#% t = Text(root, width=20, height=10, font=('Fira Code', 14, bold), fg='blue', bg='yellow', wrap=WORD)

#! The option 'wrap' specifies where to cut the line.

#! wrap= CHAR represents that any line too long should be broken at any character.
#! wrap= WORD represents that any line too long should be broken after the last word that fits the line.
#! wrap= NONE will not wrap the lines.

#! Once the text widget is created, one can insert any text using the insert() method as:

#% t.insert(END, 'Text widget\nThis text is inserted into the text widget. \n This is the second line in the text widget \n and this is the third line.\n'

#! here, the 'END' represents that the text is added to the end of the previous text.
#! The 'CURRENT' represents that the text is added at the current cursor position.


#! Use image_create() method to display an image in the text widget.

#% img = PhotoImage(file='moon.gif')  ## store moon.gif into img obj.
#% t.img_create((END, image=self.img) ## Append img to text widget at the end.

#! A program to create a text widget with a vertical scrollbar attached to it. Also highlight the
#! first line of the text and display an image in the text widget.

# from tkinter import Tk
# from tkinter import Text
# from tkinter import PhotoImage
# from tkinter import WORD, END, LEFT,RIGHT, Scrollbar, VERTICAL, HORIZONTAL

# class MyText:
#         def __init__(self,root):
#                 self.t = Text(root, width= 30, height= 20, font=('Fira Code', 14, 'bold'), fg='blue', bg='yellow',wrap=WORD)
#         ## Insert some text into the text widget
#                 self.t.insert(END,'Text Widget\nLorem ipsum dolor sit amet, consectetur adipiscing elit.\n This is second line\n and this is the third line\n')
#         ## Attach text to the root
#                 self.t.pack(side=LEFT)
#         ## Show image in the text widget
#                 self.img = PhotoImage(file='moon.gif')
#                 self.t.image_create(END, image=self.img)
#         ## create a tag with a name 'start'
#                 self.t.tag_add('start','0.5','1.11')
#         ## apply colors to the tag
#                 self.t.tag_config('start',background='red', foreground='white', font=('Fira Code',20, 'bold italic'))
#         ## Create a scroll bar widget to move the text vertically
#                 self.s =Scrollbar(root, orient=VERTICAL, command=self.t.yview)
#         ## attach the scroll bar to the text widget
#                 self.t.configure(yscrollcommand=self.s.set)
#         ## attach the scroll bar to the root window
#                 self.s.pack(side=RIGHT, fill='y')
# ## Create a root window
# root = Tk()

# ## Create an object to the MyText
# mt = MyText(root)

# ## the root window handles the mouse click event
# root.mainloop()

#@ Scrollbar Widget

#! A scroll bar is a widget that is useful to scroll the text in another widget.

#! The text in the Text, Canvas, Frame or Listbox can be scrolled from top to bottom
#! or from left to right using scroll bars.



#! To create a scroll bar, need to create a Scrollbar class object as:

#% h = Scrollbar(root, orient= HORIZONTAL, bg='green', command=t.xview)

#! 't.xview' represents scroll bar is executed on the text widget 't' along 'x' axis.

#% y = Scrollbar(root, orient= VERTICAL, bg='green', command=t.yview)

#! 't.yview' represents scroll bar is executed on the text widget 't' along 'y' axis.



#! After creating a scroll bar, it should be attached to the widget like Text widget
#! or Listbox as:

#% t.configure(xscrollcommand=h.set)

#! Here, 't' indicates Text widget. xscrollcommand calls the set() method of
#! horizontal scroll bar.

#% t.configure(yscrollcommand=v.set)

#! Here, 't' indicates Text widget. yscrollcommand calls the set() method of
#! vertical scroll bar.



#! Finally, the scroll bar should be attached to the root window using the pack() method
#! or grid() method as:

#% h.pack(side=BOTTOM, fill=x)

#! Here, we are attaching the scroll bar to the at the bottom of the widget and
#! it spreads across x-axis. 

#! Similarly, the scroll bar should be attached to the root window using the pack() method#! or grid() method as:

#% v.pack(side=RIGHT, fill=y)

#! A program to create a horizontal scroll bar and attach it to a Text widget to view the text from
#! left to right.

# from tkinter import Tk
# from tkinter import Text, END, TOP, Scrollbar, HORIZONTAL, X, BOTTOM, NONE


# class MyScrollbar:
#         def __init__(self,root):
#                 self.t = Text(root, width=70, height=15, wrap=NONE)
#         ## insert some text into the Text widget
#                 for i in range(50):
#                         self.t.insert(END, 'Lorem ipsum dolor sit amet')
#         ## attach text widget to the root window at the top
#                 self.t.pack(side=TOP, fill=X)
#         ## create a horizontal scrollbar and attach it to text widget
#                 self.h = Scrollbar(root, orient=HORIZONTAL, command=self.t.xview)
#         ## text widget is configured to respond to scroll commands
#                 self.t.configure(xscrollcommand=self.h.set)
#         ## attach scrollbar to root window at the bottom
#                 self.h.pack(side=BOTTOM, fill=X)                
        
# root = Tk()

# ms = MyScrollbar(root)

# root.mainloop()


#@ Check Button Widget

#! One can create check Buttons using the Checkbutton class as:

#! cb = CheckButton(f, bg='yellow', fg='green', font=('hack', 20, 'underline'),text='Python', variable=var1,
#! command=display)

#! Option variable represents an object of IntVar() class.

#! Class IntVar is useful to know the state of the check button, whether it is clicked or not.



#! A program to create 3 check buttons and know which options are selected by the user.

# from tkinter import Tk, Frame, IntVar, Checkbutton,Label

# class MyCheck:
#         def __init__(self, root):
#                 self.f = Frame(root, height=350, width=500)
#                 self.f.propagate(0)
#                 self.f.pack()
#                 self.var1 = IntVar()
#                 self.var2 = IntVar()
#                 self.var3 = IntVar()
#         ## create check boxes and bind them to display method
#                 self.c1 = Checkbutton(self.f, bg= 'pink',text='Python', variable=self.var1, command=self.display)
#                 self.c2 = Checkbutton(self.f, bg= 'red', text='C++',variable=self.var2, command=self.display)
#                 self.c3 = Checkbutton(self.f, bg= 'blue',text='Java',variable=self.var3, command=self.display)
#         ## Place check boxes in the frame
#                 self.c1.place(x=50, y=100)
#                 self.c2.place(x=200, y=100)
#                 self.c3.place(x=350, y=100)                
#         def display(self):
#                 ## Retrieve the control variable values
#                 x = self.var1.get()
#                 y = self.var2.get()
#                 z = self.var3.get()
#         ## String is empty initially
#                 str = ''
#         ## Accept user's choice
#                 if x == 1:
#                   str += 'Python\t'
#                 if y == 1:
#                   str += 'C++\t'
#                 if z == 1:
#                   str += 'Java'
#         ## Display the user selection as label
#                 Label(text=str, fg='black').place(x=50, y=150, width=200, height=100)
# root = Tk()

# mc = MyCheck(root)

# root.mainloop()



#@ Radio Button Widget

#! Useful to select one option from a group of available options.

#! Create radio buttons and know which button is selected by the user

# from tkinter import Tk, Frame, IntVar, Radiobutton, Label

# class MyRadio:
#       def __init__(self, root):
#               self.f = Frame(root, height=350, width=500)
#               self.f.propagate(0)
#               self.f.pack()
#       ## create IntVar class variable.
#               self.var = IntVar()
#       ## create radio buttons and bind them to display method
#               self.r1 = Radiobutton(self.f, bg='#00FFFF',text= 'Male', variable=self.var, value=1, command=self.display)
#               self.r2 = Radiobutton(self.f,bg='#DEB887', text='Female', variable=self.var, value=2,command=self.display)
#               self.r1.place(x=50, y=100)
#               self.r2.place(x=200, y=100)
#       def display(self):
#               x= self.var.get()
#               str = ''
#               if x == 1:
#                       str += 'Male'
#               if x == 2:
#                       str += 'Female'
#               Label(text=str, fg='blue').place(x=50, y=150, width=200, height=20)
              
# root = Tk()

# mr = MyRadio(root)

# root.mainloop()


#@ Entry Widget

#! Entry Widget is useful to create a rectangular box (input field).

#% e1 = Entry(f, width=25, fg='blue', bg='yellow', font=('Arial',14), show='*')

#! Here, show= '*' represents 'star' character that replaces the originally typed character while displaying user entered info.
#! e.g. as while entering password.

#! when user hits enter button after typing in the entry widget, that event should be linked with the Entry Widget using bind().
#% e1.bind('<return>', self.display)

#! Now this event is passed to the display function.
#% def display(self, event):


#! Create Entry widgets for entering user name, password and displaying the entered text.

# from tkinter import Tk, Entry, Frame, Label

# class MyEntry:
#         def __init__(self, root):
#                 self.f = Frame(root, height=350, width=500)
#                 self.f.propagate(0)
#                 self.f.pack()
                
#                 self.l1 = Label(text='Enter User Name: ')
#                 self.l2 = Label(text='Enter Password: ')
#                 ## Create Entry widget for user name
#                 self.e1 = Entry(self.f, width=25, fg='blue', bg='yellow', font=('Arial', 14))
#                 ## Create Entry widget for password
#                 self.e2 = Entry(self.f, width=25, fg='blue', bg='yellow', font=('Aerial',14),show='*')
                
#                 ## When user presses enter, bind that event to display method
#                 self.e2.bind('<Return>',self.display)
                
#                 ## Now place labels and entry widgets in the frame
#                 self.l1.place(x=50, y=100)
#                 self.e1.place(x=200, y=100)
#                 self.l2.place(x=50, y=150)
#                 self.e2.place(x=200, y=150)
#         def display(self, event):
#                 str1 = self.e1.get()
#                 str2 = self.e2.get()
                
#                 ## Display the values using labels
#                 Label(text = 'Your name is: '+str1).place(x=50, y=200)
#                 Label(text = 'Your password is: '+str2).place(x=50, y=220)
# root = Tk()

# me = MyEntry(root)

# root.mainloop()

#@ Spinbox Widget

#! A spinbox widget is nothing but a dropdown menu.

#% s1 = Spinbox(f, from=5, to=15, textvariable= val1, width=15, fg='blue', bg='yellow',
#%      font=('Arial', 14, 'bold'))

#! Here 'from' indicates starting value and 'to' indicates ending value in the spinbox.

#% val1 = IntVar()      ## Integer variable

#! Spinbox with strings

#% s2 = Spinbox(f, values=('Mumbai','Chandigarh','Lucknow', 'Vadodara', 'Pune'), textvariable= val1, width=15, fg='black', bg='white',
#%      font=('Arial', 14, 'bold italic'))

#% val2 = stringvar()

#! Create two spin boxes and retrieve the values displayed in the spin boxes when the user click on
#! the mouse.

# from tkinter import Tk, Frame, IntVar, StringVar, Spinbox, Button, Label

# class MySpinbox:
#         def __init__(self, root):
#                 self.f = Frame(root, height=350, width=500)
#                 self.f.propagate(0)
#                 self.f.pack()
                
#                 self.var1 = IntVar()
#                 self.var2 = StringVar()
                
#                 ## Create Spinbox from number 5 to 15
#                 self.s1 = Spinbox(self.f, from_= 5, to=15, textvariable=self.var1,
#                         width= 15, fg='blue', bg='yellow', font=('Arial',14,'bold'))
#                 self.s2 = Spinbox(self.f, values=('Mumbai','Chandigarh','Lucknow', 'Vadodara', 'Pune'),
#                         textvariable=self.var2, width=15, fg='white', bg='red', font=('Arial',14,'bold italic'))
                
#                 ## Create a button and bind iy with display() method
#                 self.b = Button(self.f, text='Get values from Spin boxes',command=self.display)
                
#                 ## place spin boxes and button in the frame
#                 self.s1.place(x=50, y=50)
#                 self.s2.place(x=50, y=100)
#                 self.b.place(x=50, y=150)
                
#         def display(self):
#                 a = self.var1.get()
#                 s = self.var2.get()
                        
#                 ## Display the values using the labels
#                 lbl1 =Label(text= 'Selected value is: '+str(a)).place(x=50, y=200)
#                 lbl2 =Label(text= 'Selected value is: '+s).place(x=50, y=220)
                        
# root = Tk()

# ms = MySpinbox(root)

# root.mainloop()

#@ Listbox Widget

#! A list box widget is useful to display list of items in a box so that the user can select 1
#! or more items.

#% lb = Listbox(f, font='Arial,12,bold',fg='blue', bg='yellow', height=8, width=24,
#%      activestyle= 'underline', selectmode='MULTIPLE)

#! Here, 'activestyle' indicates the appearance of the selected item. It may be underline, dotbox
#! or NONE. Default is 'underline'

#! Selectmode options: 'BROWSE', 'SINGLE', 'MULTIPLE', 'EXTENDED'. Default is 'BROWSE'.

#! Create a list box with Universities names and display the selected universities names in a
#! a text box.

# from tkinter import Tk, Frame, Label, Listbox, MULTIPLE, END,Text, WORD

# class ListboxDemo:
#         def __init__(self, root):
#                 self.f = Frame(root, width=700, height= 400)
#                 self.f.propagate(0)
#                 self.f.pack()
#                 ## Create a label
#                 self.lbl = Label(self.f, text= 'Click one or more universities below: ',font='Arial 14')
#                 self.lbl.place(x=50, y=50)
#                 ## create list box with universities names.
#                 self.lb = Listbox(self.f, font='Arial 12 bold', fg='white', bg='green', height=8,selectmode=MULTIPLE)
#                 self.lb.place(x=50, y=100)
#                 ## using for loop, insert items into list box.
#                 lst = ['Stanford University', 'Howard University', 'Oxford University', 'Alabama State University', 'University of Washington', 'University of California', 'Michigan State University']
#                 for i in lst:
#                         self.lb.insert(END, i)
#                 ## bind the listbox select event to on_select() method.
#                 self.lb.bind('<<ListboxSelect>>',self.on_select)
#                 ## create text box to display selected items.
#                 self.t = Text(self.f, width=40, height=6,wrap=WORD)
#                 self.t.place(x=300, y=100)
#         def on_select(self, event):
#                 ## create an empty list box
#                 self.lst1 = []
#                 ## know the indexes of the selected items
#                 indexes = self.lb.curselection()
#                 ## retrieve the items names depending on the indexes
#                 ## append the item names to the list box.
#                 for i in indexes:
#                         self.lst1.append(self.lb.get(i))
#                 ## delete the previous content of the text box
#                 self.t.delete(0.0, END)
#                 ## insert the new contents into the text box
#                 self.t.insert(0.0,self.lst1)
# root = Tk()

# ## Title for the root Window
# root.title('Listbox Demonstration')

# ld = ListboxDemo(root)

# root.mainloop()

#@ Menu Widget

#! Create a Menu bar and adding File and edit menu items.

# from tkinter import Tk, Menu

# class MyMenuDemo:
#         def __init__(self, root):
#                 ## create a menu bar from Menu(root)
#                 self.menubar = Menu(root)
                
#                 ## Attach the menu bar to the root window
#                 root.config(menu=self.menubar)
                
#                 ## Create file menu
#                 self.filemenu = Menu(root, tearoff=0) ## filemenu is Menu class object
#                 ## Option 'tearoff' can be 0 or 1. Default is 0
                
#                 ## Create items in the file menu
#                 self.filemenu.add_command(label='New',command=self.donothing)
#                 self.filemenu.add_command(label='Open',command=self.donothing)
#                 self.filemenu.add_command(label='Save',command=self.donothing)
                
#                 ## Add horizontal line as separator
#                 self.filemenu.add_separator()
                
#                 ## Create another menu item below the separator
#                 self.filemenu.add_command(label='Exit',command=root.destroy)
                
#                 ## create another menu with a name 'file' to the menu bar
#                 self.menubar.add_cascade(label='File', menu=self.filemenu)
                
#                 ## Create edit menu
#                 self.editmenu = Menu(root, tearoff=0)
                
#                 ## create menu items in the edit menu
#                 self.editmenu.add_command(label='Cut',command=self.donothing)
#                 self.editmenu.add_command(label='Copy',command=self.donothing)
#                 self.editmenu.add_command(label='Paste',command=self.donothing)
                
#                 ## add edit menu with a name 'Edit' to the menu bar
#                 self.menubar.add_cascade(label='Edit', menu=self.editmenu)
#         def donothing(self):
#                 pass
# root = Tk()

# root.title('A Menu Example')

# md = MyMenuDemo(root)

# ## Define the size of the root window
# root.geometry('600x350')

# root.mainloop()

#! A GUI program to display a menu and also to open a file and save it through the dialogue box.

# from tkinter import Tk, filedialog, Text, WORD, END, Menu

# class MyMenuDemo:
#         def __init__(self, root):
#                 self.menubar = Menu(root)
#         ## attach a menubar to the root window
#                 root.config(menu=self.menubar)                  ## Step one attaching menubar to root.
#         ## create file menu
#                 self.filemenu = Menu(root,tearoff=0)            ## Creating file menu & attaching items
#         ## create menu items in file menu
#                 self.filemenu.add_command(label='New',command=self.donothing)
#                 self.filemenu.add_command(label='Open',command=self.open_file)
#                 self.filemenu.add_command(label='Save',command=self.save_file)
#         ## Add a horizontal line separator
#                 self.filemenu.add_separator()                   ## Adding a separator
#         ## Create another menu item below the separator
#                 self.filemenu.add_command(label='Exit',command=root.destroy)
#         ## Add the file menu with a name 'File' to the Menubar.
#                 self.menubar.add_cascade(label='File',menu=self.filemenu)  ## Adding file menu to cascade
#         ## create edit menu
#                 self.editmenu = Menu(root,tearoff=0)            ## Creating edit menu & attaching items
#         ## create menu items in edit menu
#                 self.editmenu.add_command(label='Cut',command=self.donothing)
#                 self.editmenu.add_command(label='Copy',command=self.donothing)
#                 self.editmenu.add_command(label='Paste',command=self.donothing)
#         ## Add the edit menu with a name 'Edit' to the Menubar
#                 self.menubar.add_command(label='Edit',command=self.editmenu)
#         def donothing(self):
#                 pass
#         ## Method for opening a file and display its contents in a text box
#         def open_file(self):
#                 self.filename = filedialog.askopenfilename(parent=root, title='Select a File',filetypes=(('Python files','*.py'),('All files','*.*')))
#         ## if cancel button is not clicked in the dialog box
#                 if self.filename != None:
#                 ## open the file in read mode.
#                         f = open(self.filename, 'r')
#                 ## read the contents of the file
#                         contents =f.read()
#                 ## create a text box and add it to root window
#                 self.t = Text(root, width=80, height=20, wrap=WORD)
#                 self.t.pack()
#                 self.t.insert(1.0, contents)
#                 ## close the file
#                 f.close()
#         ## method to save a file that is already in the Text Box
#         def save_file(self):
#                 ## Open a file dialog box and type a file name
#                 self.filename = filedialog.asksaveasfilename(parent=root, defaultextension='txt')
#                 ## if cancel button is not clicked in the dialog box
#                 if self.filename != None:
#                         f = open(self.filename,'w')
#                         ## get the contents of the text box
#                         contents =str(self.t.get(1.0, END))
#                         ## write the contents into the file
#                         f.write(contents)
#                         ## close the file
#                         f.close()
# ## Create a root window
# root = Tk()

# ## Title for the root window
# root.title('My Documents')

# md = MyMenuDemo(root)

# root.geometry('600x350')

# root.mainloop()

#@ Creating Tables

#! Python does not provide a Table Widget to create a table.

#! H'ever, we can make a table by repeatedly displaying Entry widgets in the form of rows and columns.

#! To create a table with 5 rows and 4 columns, we can use 2 for loops as;

#% for i in range(5):
#%      for j in range(4):

#! A GUI program to display a table with several rows and columns

from tkinter import Tk, Entry, END

class MyTable:
        def __init__(self, root):
                ## code for creating the table
                for i in range(total_rows):
                        for j in range(total_cols):
                                self.e = Entry(root, width=20, fg='blue', font=('Arial',15, 'bold'))
                                self.e.grid(row=i, column=j)
                                self.e.insert(END, lst[i][j])
## Take the data
lst = [(1001, 'Veronica', 'Gettysburg', 120780.88),(1002, 'Betty', 'Mississippi', 221000.50), (1003, 'Sandra', 'Baton Rouge', 98048.75), (1004, 'Catherine', 'Memphis', 145210.00), (1005, 'Michael', 'Arkansas', 185054.10)]
## Find number of rows and cols in the list
total_rows = len(lst)
total_cols = len(lst[0])

## Create root window

root = Tk()

mt = MyTable(root)
