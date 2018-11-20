#Klementinus Kennyvito Salim , 2201811391
#Final Project : Food For Folks

from tkinter import *
from PIL import ImageTk, Image
import webbrowser
#import necessary APIs


#Making a Class for application
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    #Creating widgets such as text boxes and buttons
    def create_widgets(self):

        self.header = Label(f, text="Welcome to Food for Folks Application!\n"
                     "To start using this app, just type your ingredients that you would like to cook with, and click on the search button. It's that simple!\n"
                                    "To add more items, just include a space between every ingredients.(Maximum 10 ingredients)",
          fg="floral white",font=("Helvetica",16))
        self.header.config(bg="OrangeRed4")
        self.header.grid(row=5,column=100,sticky=E)
        self.header.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.enteringredients = Label(self, text = "Enter Ingredients",bg="honeydew2")
        self.enteringredients.grid(row = 0, column = 0 , sticky = W)

        self.ingredients  = Entry(self,width=60)
        self.ingredients.grid(row=0, column=4, sticky = W)

        self.search_button= Button(self, text="Search", command = self.reveal,background="DeepSkyBlue2",fg="honeydew2")
        self.search_button.grid(row=0,column=12,sticky = W)

        self.text = Text(self, width = 60, height=7, wrap = WORD)
        self.text.grid(row=3,column=4 ,columnspan=2, sticky =W)

        self.about_button = Button(f, text="About Us",command=self.aboutwindow
                      ,background = "coral1", fg="gray9",font=("Times New Roman",16))
        self.about_button.config(height=1,width=10)
        self.about_button.grid(row=1000,column=8,sticky=W)
        self.about_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    #The "Core" of the program to search for recipes
    def reveal(self):
        content = self.ingredients.get()
        cs = content.split(" ")
        if len(cs) == 1:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}'.format(cs[0])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 2:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}'.format(cs[0],cs[1])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 3:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}+{}'.format(cs[0],cs[1],cs[2])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 4:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}+{}+{}'.format(cs[0],cs[1],cs[2],cs[3])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 5:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}+{}+{}+{}'.format(cs[0],cs[1],cs[2],cs[3],cs[4])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 6:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}+{}+{}+{}+{}'.format(cs[0],cs[1],cs[2],cs[3],cs[4],cs[5])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 7:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}+{}+{}+{}+{}+{}'.format(cs[0],cs[1],cs[2],cs[3],cs[4],cs[5],cs[6])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 8:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}+{}+{}+{}+{}+{}+{}'.format(cs[0],cs[1],cs[2],cs[3],cs[4],cs[5],cs[6],cs[7])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 9:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}+{}+{}+{}+{}+{}+{}+{}'.format(cs[0],cs[1],cs[2],cs[3],cs[4],cs[5],cs[6],cs[7],cs[8])
            webbrowser.open_new_tab(tab)

        elif len(cs) == 10:
            m = "Please hold a moment, Opening On your browser..."
            tab = 'https://api.edamam.com/recipes/{}+{}+{}+{}+{}+{}+{}+{}+{}+{}'.format(cs[0],cs[1],cs[2],cs[3],cs[4],cs[5],cs[6],cs[7],cs[8],cs[9])
            webbrowser.open_new_tab(tab)

        else:
            m = "Sorry, please re-check your search format."


        self.text.delete(0.0, END)
        self.text.insert(0.0,m)

    #defines another window that describes about the program
    def aboutwindow(self):
        window = Toplevel(f)
        window.geometry("940x627")

        #Background image of "About" window
        can = Canvas(window)
        imgw = ImageTk.PhotoImage(Image.open("cutleryys.jpg"))
        can.create_image(100,100, anchor=CENTER, image=imgw)

        #Text input
        background_label2 = Label(window, image=imgw)
        background_label2.place(x=0, y=0, relwidth=1, relheight=1)
        can.grid(row=0,column=0,sticky=W)
        desc = Label(window, text="Food for Folks, Created by\n Klementinus Kennyvito Salim - CS 2022\n"
                     
                            "This program is meant for everyone who wants to cook ,\nbut could not decide what to cook,\n hence this program is created for those certain of people.\n",
          fg="red",font=("Times New Roman",18))
        desc.config(bg="white")
        desc.grid(row=5,column=100,sticky=E)
        desc.place(relx=0.3, rely=0.3, anchor=CENTER)

        window.mainloop()

class Program:
    def background(self):
        f.title("Food for Folks")
        f.geometry("1920x1080")
        img = ImageTk.PhotoImage(Image.open("fg.jpg"))              #Adds background image to the window
        ca = Canvas(f)
        ca.create_image(100,100, anchor=CENTER, image=img)
        bgimage = Label(f, image=img)
        bgimage.place(x=0, y=0, relwidth=1, relheight=1)
        ca.grid(row=0,column=0,sticky=W)

        app = Application(f)                            #Calls out the Application class to generate all the widgets such as the buttons and headers
        app.place(relx=0.5, rely=0.5, anchor=CENTER)    #the position of the widgets
        f.mainloop()

    def main(self):
        self.background()


#Tkinter command to make window
f = Tk()

#Main program
p = Program()
p.main()


#Special Thanks to Excelino

#Thanks to https://api.edamam.com/recipes/ for making this project possible.
