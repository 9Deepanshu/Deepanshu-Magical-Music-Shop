#-----Deepanshu's Magical Music Shop----------------------------------#
#
#  This python app combines my knowledge of Python
#  programming, HTML-style mark-up languages, pattern matching,
#  database management, and Graphical User Interface design to produce
#  a robust, interactive app that allows its user to view and save
#  data from multiple online sources.
#
#--------------------------------------------------------------------#
#Set Up
from sys import exit as abort

from urllib.request import urlopen

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar
 
from re import *
 
from webbrowser import open as urldisplay
 
from sqlite3 import *


#import
from sqlite3 import *
from urllib.request import urlopen, Request
from re import findall, MULTILINE
from urllib.error import HTTPError
from urllib.error import URLError
#variable
char_set = 'UTF-8'
def opening_website(url = 'https://www.bettermusic.com.au/electric-guitars', incognito = False):
    #first product opening url
    try:
        if incognito:
            # Pretend to be a web browser instead of a Python script 
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; ' + \
                               'rv:91.0; ADSSO) Gecko/20100101 Firefox/91.0')
        else:
            # Behave ethically
            request = url
        product_web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        Messages_Text['text'] = f"\nCannot find requested document '{url}'\nError message was: {message}\n"
        return None
    except HTTPError as message: # possibly an authorisation problem
        Messages_Text['text'] = f"\nAccess denied to document at URL '{url}'\nError message was: {message}\n"
        return None
    except URLError as message: # probably the wrong server address
        Messages_Text['text'] = f"\nCannot access web server at URL '{url}'\nError message was: {message}\n"
        return None
    except Exception as message: # something entirely unexpected
        Messages_Text['text'] = f"\nSomething went wrong when trying to download the document at URL '{str(url)}'\nError message was: {message}\n"
        return None

    #First product reading the contents as a character string
    global product_web_page_contents
    try:
        product_web_page_contents = product_web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        Messages_Text['text'] = f"\nUnable to decode document from URL '{First_product_url}' as '{char_set}' characters\nError message was: {message}\n"
    except Exception as message:
        Messages_Text['text'] = f"\nSomething went wrong when trying to decode the document from URL '{First_product_url}'\nError message was: {message}\n"

def first_product_opening():
    opening_website(url = 'https://www.bettermusic.com.au/electric-guitars', incognito = False)
    
    #first product category data collection
    First_Products_and_Prices = findall('<a class=\"product-item-link\"\s+href=\"https://www\.bettermusic\.com\.au/.+\">\s+([A-Za-z0-9 -]+)\s+</a>\s+</strong>\s+<div[a-z? ?=?\"?A-Z-?0-9?:/.?]+></div>\s+<div[a-z? ?=?\"?A-Z-?0-9?:/.?_?]+>\s+<span[a-z? ?=?\"?A-Z-?0-9?:/.?_?&?#?;?]+\s+>\s+<span[a-z? ?=?\"?A-Z-?0-9?:/.?_?&?#?;?\s]+><span class=\"price\">\$([0-9,]+\.[0-9]+)</span></span>\s+</span>\s</div>', product_web_page_contents)
    global Guitar
    global GuitarPrice
    Guitar = First_Products_and_Prices[0][0].replace('  ','')
    GuitarPrice = float(First_Products_and_Prices[0][1])

def second_product_opening_incognito():
    opening_website(url = 'https://www.riffsandlicks.com.au/pa-live-sound', incognito = True)

    #Second product category data collection
    Second_Products_and_Prices = findall('<a href=\"https://www\.riffsandlicks\.com\.au/[a-z-0-9?]+\" title=\"[A-Z0-9?\"?a-z-?\/? ]+\">([A-Z0-9?\"?a-z-?\/? ]+)</a></div>\s<div class=\"price-box\" itemprop=\"offers\" itemscope=?\"?\"? itemtype=\"http://schema\.org/Offer\">\s<span class=\"special-price font text-orange\">\s<span class=\"price\" itemprop=\"price\">\s<span id=\"custom-our-price\" class=\"price\">[A-Za-z-? ]+ </span>\s<span class=\"specialPrice\" itemprop=\"price\" content=\"[0-9]+\">\$([0-9]+\.[0-9]+)</span>\s</span>', product_web_page_contents)
    global Hardware
    global HardwarePrice
    Hardware = Second_Products_and_Prices[0][0]
    HardwarePrice = float(Second_Products_and_Prices[0][1])

def third_product_opening():
    opening_website(url = 'https://www.gear4music.com/Music-Software-deals', incognito = False)

    #Third product category data collection
    Third_Products_and_Prices = findall('<h3 class=\"product-card-title\" data-xplr=\"inv-[0-9]+-[0-9]+\" data-test=\"desktop/plp/product-card-title\">([A-Za-z -]+)</h3><div class=\"product-card-image-wrapper\"><picture><source srcset=\"[A-Za-z:/;,0-9 ]+\"><img src=\"[A-Za-z:/;,0-9 ]+\" alt=\"[A-Za-z0-9- ]+\" class=\"product-card-image\"></picture></div><div class=\"product-card-description\" data-test=\"desktop/plp/product-card-description\">[A-za-z0-9-+ ]+</div><div class=\"product-card-availability\"><div class=\"product-card-price\" data-test=\"desktop/plp/product-card-price\">£([0-9]+\.[0-9]+)</div>', product_web_page_contents)
    global Software
    Software = Third_Products_and_Prices[0][0]
    SoftwarePrice_PoundSterling = float(Third_Products_and_Prices[0][1])
    global SoftwarePrice_AUD
    SoftwarePrice_AUD = round(SoftwarePrice_PoundSterling * 1.91, 2)

# Create the main window
main_window = Tk()

# Your code goes here
main_window.configure(background='#272d2d', cursor="heart")
main_window.title('Deepanshu Magical Music Shop')

#logo on top of GUI
photo = PhotoImage(file= 'deepanshu_logo.png')
logo = Label(main_window, image = photo, bg = '#272d2d')
logo.grid(row = 0, column = 1, columnspan = 3)

#creating space between image and frame
Empty_Space = Label(main_window, text="", bg = '#272d2d')
Empty_Space.grid(row = 1, column = 1)

#Messages Frame
Messages_Frame = Frame(main_window, highlightbackground = '#d3a63f', highlightthickness = 1, bg = '#272d2d') #creating frame for messages area
Messages_Frame.grid(row = 2, column = 1, columnspan = 3, rowspan = 2)
#Messages Heading
Messages_Heading = Label(Messages_Frame, text = 'Messages', font = ('Microsoft Himalaya', 35, 'bold'), bg = '#272d2d', fg = '#d3a63f') #Messages title text
Messages_Heading.grid(row = 2, column = 1)
#Messages Text
Messages_Text = Label(Messages_Frame, text = 'Messages will appear here', font = ('Microsoft Himalaya', 30), bg = '#272d2d', fg = '#d3a63f') #messages text
Messages_Text.grid(row = 3, column = 1)

Empty_Space = Label(main_window, text="", bg = '#272d2d') #empty space before next frame
Empty_Space.grid(row = 4, column = 1)

#Prodcut Frame
Product_Frame = Frame(main_window, highlightbackground = '#d3a63f', highlightthickness = 1, bg = '#272d2d')
Product_Frame.grid(row = 5, column = 1, columnspan = 3, rowspan = 3)
#Product Heading
product = Label(Product_Frame, text = 'Product', font = ('Microsoft Himalaya', 35, 'bold'), bg = '#272d2d', fg = '#d3a63f')
product.grid(row = 5, column = 1, columnspan = 3)

choice_of_product = IntVar() #creating variable for radio button choices
def messages_info():
    if choice_of_product.get() == 1:
        first_product_opening()
        Messages_Text['text'] = f'{Guitar}\n${GuitarPrice}'
    elif choice_of_product.get() == 2:
        second_product_opening_incognito()
        Messages_Text['text'] = f'{Hardware}\n${HardwarePrice}'
    else:
        third_product_opening()
        Messages_Text['text'] = f'{Software}\n${SoftwarePrice_AUD}'
        
#first choice
Musical_Instruments = Radiobutton(Product_Frame, text = 'Musical Instruments', font = ('Microsoft Himalaya', 30), variable = choice_of_product, value = 1, bg = '#272d2d', fg = '#d3a63f', selectcolor = '#272d2d', activebackground = '#d3a63f', activeforeground = '#272d2d', command = messages_info)
Musical_Instruments.grid(row = 6, column = 1)
#second choice
Music_Hardware = Radiobutton(Product_Frame, text = 'Music Hardware', font = ('Microsoft Himalaya', 30), variable = choice_of_product, value = 2, bg = '#272d2d', fg = '#d3a63f', selectcolor = '#272d2d', activebackground = '#d3a63f', activeforeground = '#272d2d', command = messages_info)
Music_Hardware.grid(row = 6, column = 2)
#third choice
Music_Software = Radiobutton(Product_Frame, text = 'Music Software', font = ('Microsoft Himalaya', 30), variable = choice_of_product, value = 3, bg = '#272d2d', fg = '#d3a63f', selectcolor = '#272d2d', activebackground = '#d3a63f', activeforeground = '#272d2d', command = messages_info)
Music_Software.grid(row = 6, column = 3)

def open_website():
    if choice_of_product.get() == 1:
        urldisplay('https://www.bettermusic.com.au/electric-guitars')
        Messages_Text['text'] = 'Website opened in default browser'
    elif choice_of_product.get() == 2:
        urldisplay('https://www.riffsandlicks.com.au/pa-live-sound')
        Messages_Text['text'] = 'Website opened in default browser'
    elif choice_of_product.get() == 3:
        urldisplay('https://www.gear4music.com/Music-Software-deals')
        Messages_Text['text'] = 'Website opened in default browser.'
    else:
        Messages_Text['text'] = 'No product category selected to show details.'

#details button
Details_Button = Button(Product_Frame, text = 'Show Details', font = ('Microsoft Himalaya', 30), bg = '#272d2d', fg = '#d3a63f', activebackground = '#d3a63f', activeforeground = '#272d2d', relief=GROOVE, command = open_website)
Details_Button.grid(row = 7, column = 1, columnspan = 3)

Empty_Space = Label(main_window, text="", bg = '#272d2d') #empty space before next frame
Empty_Space.grid(row = 8, column = 1)

#Place Order Button
def PlaceOrder():
    try:
        connection = connect(database = 'orders.db')
        orders_db = connection.cursor()
        
        if choice_of_product.get() == 1:
            sql_code = f"INSERT INTO products_ordered VALUES ('{Guitar}', '{GuitarPrice}')"
            orders_db.execute(sql_code)
            connection.commit()
            Messages_Text['text'] = 'Your order has been placed.'
        elif choice_of_product.get() == 2:
            sql_code = f"INSERT INTO products_ordered VALUES ('{Hardware}', '{HardwarePrice}')"
            orders_db.execute(sql_code)
            connection.commit()
            Messages_Text['text'] = 'Your order has been placed.'
        elif choice_of_product.get() == 3:
            sql_code = f"INSERT INTO products_ordered VALUES ('{Software}', '{SoftwarePrice_AUD}')"
            orders_db.execute(sql_code)
            connection.commit()
            Messages_Text['text'] = 'Your order has been placed.'
        else:
            Messages_Text['text'] = 'No product selected for placing order.'
            
        orders_db.close()
        connection.close()
    except OperationalError as message:
        Messages_Text['text'] = f"\nSomething went wrong when trying to place an order\nError message was: {message}\n"

Place_Order_Button = Button(main_window, text = 'Place an order', font = ('Microsoft Himalaya', 30), bg = '#272d2d', fg = '#d3a63f', activebackground = '#d3a63f', activeforeground = '#272d2d', relief=GROOVE, command = PlaceOrder)
Place_Order_Button.grid(row = 9, column = 2)

#Show bill button
def show_bill():
    try:
        connection = connect(database = 'orders.db')
        orders_db = connection.cursor()
        
        orders_db.execute('''SELECT product, price_AUD
                              FROM products_ordered''')

        # Fetching list of orders and prices
        orders_prices = []
        prices= []
        for product, price in orders_db.fetchall():
            orders_prices.append([product, price])
            prices.append(price)

        Total_price = sum(prices)
        bill = '\n'.join(map(str,orders_prices)).replace('[', '').replace(']', '').replace("'", '').replace(", ", ': $') #string of products and their prices on seperate lines
        Messages_Text['text'] = f'Your Bill\n{bill}\nTotal: ${Total_price}'

        orders_db.close()
        connection.close()
    except OperationalError as message:
        Messages_Text['text'] = f"\nSomething went wrong when trying to access the bill\nError message was: {message}\n"
        
    
Show_Bill_Button = Button(main_window, text = 'Show my Bill', font = ('Microsoft Himalaya', 30), bg = '#272d2d', fg = '#d3a63f', activebackground = '#d3a63f', activeforeground = '#272d2d', relief=GROOVE, command = show_bill)
Show_Bill_Button.grid(row = 9, column = 3)

# Start the event loop to detect user inputs
main_window.mainloop()

