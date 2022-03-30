from detection import giveInp
import mysql.connector
from mysql.connector import errorcode
from tkinter import *
import subprocess
from PIL import Image, ImageTk


# Color
# #98daea
# #00a2e8
# #3e47cc
# #00a2e8
# #98daea


def disableCloseButton():
    pass


selectionWindow = Tk()
selectionWindow.title('AeroTrial')
selectionWindow.geometry('1920x1080')
# selectionWindow.resizable(0, 0)
# selectionWindow.overrideredirect(True)
# selectionWindow.geometry("{0}x{1}+0+0".format(selectionWindow.winfo_screenwidth(), selectionWindow.winfo_screenheight()))
selectionWindow.wm_iconbitmap('Filters\\Icons\\chat.ico')
selectionWindow.protocol("WM_DELETE_WINDOW", disableCloseButton)
backgroundImage = PhotoImage(file='Filters\\BackGround\\Blue.png')
username = ''
email = ''
password = ''
with open('Data.txt') as DataFile:
    contents = DataFile.read().split('\t')
    username = contents[0]
    email = contents[1]
    password = contents[2]
iList = ['Regular Black Goggles',
         'Blue Aviator Goggles',
         'Rectangular Goggles',
         'Circular Goggles',
         'Dark Goggles',
         'CatEar Goggles',
         'Thug Life Mask',
         'Bunny Ears HandBand']
srcList = ['',
           'Filters\\Converted\\glasses.png',
           'Filters\\Converted\\glasses2.png',
           'Filters\\Converted\\glasses3.png',
           'Filters\\Converted\\glasses4.png',
           'Filters\\Converted\\glasses5.png',
           'Filters\\Converted\\glasses6.png',
           'Filters\\Converted\\fun.png',
           'Filters\\Converted\\bunny.png']

# PhotoImage Button
# image1 = Image.open('Filters\\BackGround\\9.png')
# image1 = ImageTk.PhotoImage(image1.resize((120, 120)))


def on_enter_historyButton(e):
    historyButton.config(bg='#0d1f7e', fg='white')


def on_leaving_historyButton(e):
    historyButton.config(bg='white', fg='black')


def on_enter_logoutButton(e):
    logoutButton.config(fg="white", bg='#a900c7')


def on_leaving_logoutButton(e):
    logoutButton.config(fg='black', bg='white')


def on_enter_quit(e):
    quitButton.config(bg='black', fg='white')


def on_leaving_quit(e):
    quitButton.config(bg='white', fg='black')


def openUserDetailsForm():
    selectionWindow.destroy()
    subprocess.call(["python", "UserDetails.py"])


def openLogForm():
    selectionWindow.destroy()
    subprocess.call(["python", "Log.py"])


def quitSelectionWindow():
    try:
        with open("Data.txt", "w") as dataFile:
            dataFile.write("")
        selectionWindow.destroy()
    except EXCEPTION:
        print('Error')


def sqlCon(itemName):
    if username != '':
        try:
            sqlConnector = mysql.connector.connect(user='root', database='hackathon', host='localhost', passwd='abcde')
            cursorObject = sqlConnector.cursor()
            sqlQuery = 'INSERT INTO cd (CustomerName, Product) VALUES (%s, %s)'
            valuePlaceholder = (username, itemName)
            cursorObject.execute(sqlQuery, valuePlaceholder)
            sqlConnector.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            sqlConnector.close()
    elif username == '':
        print('Empty Username')
    else:
        print('No Product')


def enterItem1():
    sqlCon(iList[0])
    giveInp(1)


def enterItem2():
    sqlCon(iList[1])
    giveInp(2)


def enterItem3():
    sqlCon(iList[2])
    giveInp(3)


def enterItem4():
    sqlCon(iList[3])
    giveInp(4)


def enterItem5():
    sqlCon(iList[4])
    giveInp(5)


def enterItem6():
    sqlCon(iList[5])
    giveInp(6)


def enterItem7():
    sqlCon(iList[6])
    giveInp(7)


def enterItem8():
    sqlCon(iList[7])
    giveInp(8)


backgroundLabel = Label(
    selectionWindow,
    image=backgroundImage
)
backgroundLabel.place(x=-2, y=-20)

labelHeader = Label(
    selectionWindow,
    text='Catalogue',
    font=('Gothic', 90, 'bold'),
    bg='#98daea',
)
labelHeader.place(x=270, y=30)
labelHeader.pack(side=TOP, pady=50)

userHead = Label(
    selectionWindow,
    justify=LEFT,
    text='Account Details',
    bg='#00a2e8',
    fg='white',
    font=('Gothic', 40, 'bold')
)
userHead.place(x=30, y=205)

userInfo = Label(
    selectionWindow,
    text='User  : ' + username + '\n\n' + 'Email : ' + email + '\n\n' + '',
    font=('Gothic', 20),
    justify=LEFT,
    bg='#00a2e8',
    fg='white',
)
userInfo.place(x=30, y=270)

infoHead = Label(
    selectionWindow,
    justify=LEFT,
    text='Info',
    bg='#3e47cc',
    fg='white',
    font=('Gothic', 40, 'bold')
)
infoHead.place(x=30, y=435)

info = Label(
    selectionWindow,
    text='We welcome you to our catalogue page. We have a \n\nfine collection of items handpicked just for you.\n\n'
         'Click on any item to try it (Press \'q\' to stop \n\nvirtualisation. '
         'You can add a item in the cart if \n\nit suits your taste.',
    font=('Gothic', 20),
    justify=LEFT,
    bg='#3e47cc',
    fg='white',
)
info.place(x=30, y=500)

importantHead = Label(
    selectionWindow,
    justify=LEFT,
    text='Important',
    bg='white',
    fg='black',
    font=('Gothic', 40, 'bold')
)
importantHead.place(x=30, y=760)

importantLabel = Label(
    selectionWindow,
    text='Press \'q\' to stop virtualisation.',
    font=('Gothic', 20),
    justify=LEFT,
    bg='white',
    fg='black',
)
importantLabel.place(x=30, y=825)

ItemBack = Label(
    bg='white',
    width='120',
    height='26',
)
ItemBack.place(x=850, y=205)

ItemNameColumn1 = Label(
    text='Name',
    font=('Gothic', 20),
    height='1',
    width='19',
    bd=4,
    bg='#0d1f7e',
    fg='white',
)
ItemNameColumn1.place(x=850, y=196)

ItemImageColumn1 = Label(
    text='Product',
    font=('Gothic', 20),
    height='1',
    width='19',
    bd=4,
    bg='yellow',
)
ItemImageColumn1.place(x=1120, y=196)

ItemColumnSeparator = Label(
    font=('Gothic', 20),
    height='20',
    bd=2,
    bg='black',
)
ItemColumnSeparator.place(x=1390, y=196)
ItemColumnShortSeparator = Label(
    font=('Gothic', 20),
    height='10',
    bd=2,
    bg='black',
)
ItemColumnShortSeparator.place(x=1390, y=482)

ItemNameColumn2 = Label(
    text='Name',
    font=('Gothic', 20),
    height='1',
    width='19',
    bd=4,
    bg='#0d1f7e',
    fg='white',
)
ItemNameColumn2.place(x=1396, y=196)

ItemImageColumn2 = Label(
    text='Product',
    font=('Gothic', 20),
    height='1',
    width='19',
    bd=4,
    bg='yellow',
)
ItemImageColumn2.place(x=1672, y=196)

#############################
# Placement Variables
defaultLabelX = 850
defaultLabelY = 242
incX = 546
incY = 103
defaultButtonX = 1121
defaultButtonY = 242
# Attribute Variables
labelBackGround = 'white'
buttonBackGround = 'white'

itemButton1 = Button(
    selectionWindow,
    text='Normal Goggles',
    height=3,
    width=20,
    font=('Gothic', 19),
    relief=FLAT,
    bg=buttonBackGround,
    command=enterItem1,
)
itemButton1.place(x=defaultLabelX, y=defaultLabelY)
img1 = PhotoImage(file=srcList[1])
itemLabel1 = Label(
    selectionWindow,
    height=90,
    width=265,
    bg=labelBackGround,
    image=img1
)
itemLabel1.place(x=defaultButtonX, y=defaultButtonY)

###############

itemButton2 = Button(
    selectionWindow,
    text='Blue Aviators',
    height=3,
    width=20,
    font=('Gothic', 19),
    relief=FLAT,
    bg=buttonBackGround,
    command=enterItem2
)
itemButton2.place(x=defaultLabelX, y=defaultLabelY + incY)
img2 = PhotoImage(file=srcList[2])
itemLabel2 = Label(
    selectionWindow,
    height=90,
    width=265,
    bg=labelBackGround,
    image=img2
)
itemLabel2.place(x=defaultButtonX, y=defaultButtonY + incY)

###############

itemButton3 = Button(
    selectionWindow,
    text='Rectangular Glasses',
    height=3,
    width=20,
    font=('Gothic', 19),
    relief=FLAT,
    bg=buttonBackGround,
    command=enterItem3
)
itemButton3.place(x=defaultLabelX, y=defaultLabelY + (2 * incY))
img3 = PhotoImage(file=srcList[3])
itemLabel3 = Label(
    selectionWindow,
    height=90,
    width=265,
    bg=labelBackGround,
    image=img3
)
itemLabel3.place(x=defaultButtonX, y=defaultButtonY + (2 * incY))

###############

itemButton4 = Button(
    selectionWindow,
    text='Transparent\n\nCircular Glasses',
    height=3,
    width=20,
    font=('Gothic', 19),
    relief=FLAT,
    bg=buttonBackGround,
    command=enterItem4
)
itemButton4.place(x=defaultLabelX, y=defaultLabelY + (3 * incY))
img4 = PhotoImage(file=srcList[4])
itemLabel4 = Label(
    selectionWindow,
    height=90,
    width=265,
    bg=labelBackGround,
    image=img4
)
itemLabel4.place(x=defaultButtonX, y=defaultButtonY + (3 * incY))

###############

itemButton5 = Button(
    selectionWindow,
    text='Black\n\nCircular Glasses ',
    height=3,
    width=20,
    font=('Gothic', 19),
    relief=FLAT,
    bg=buttonBackGround,
    command=enterItem5
)
itemButton5.place(x=defaultLabelX, y=defaultLabelY + (4 * incY))
img5 = PhotoImage(file=srcList[5])
itemLabel5 = Label(
    selectionWindow,
    height=90,
    width=265,
    bg=labelBackGround,
    image=img5
)
itemLabel5.place(x=defaultButtonX, y=defaultButtonY + (4 * incY))

###############

itemButton6 = Button(
    selectionWindow,
    text='Cat Eye\n\nGlasses',
    height=3,
    width=20,
    font=('Gothic', 19),
    relief=FLAT,
    bg=buttonBackGround,
    command=enterItem6
)
itemButton6.place(x=defaultLabelX + incX, y=defaultLabelY)
img6 = PhotoImage(file=srcList[6])
itemLabel6 = Label(
    selectionWindow,
    height=90,
    width=265,
    bg=labelBackGround,
    image=img6
)
itemLabel6.place(x=defaultButtonX + incX, y=defaultButtonY)

###############

itemButton7 = Button(
    selectionWindow,
    text='Thug Life\n\nGlasses',
    height=3,
    width=20,
    font=('Gothic', 19),
    relief=FLAT,
    bg=buttonBackGround,
    command=enterItem7
)
itemButton7.place(x=defaultLabelX + incX, y=defaultLabelY + incY)
img7 = PhotoImage(file=srcList[7])
itemLabel7 = Label(
    selectionWindow,
    height=90,
    width=265,
    bg=labelBackGround,
    image=img7
)
itemLabel7.place(x=defaultButtonX + incX, y=defaultButtonY + incY)

###############

itemButton8 = Button(
    selectionWindow,
    text='Bunny Ears\n\nHeadband',
    height=3,
    width=20,
    font=('Gothic', 19),
    relief=FLAT,
    bg=buttonBackGround,
    command=enterItem8
)
itemButton8.place(x=defaultLabelX + incX, y=defaultLabelY + (2 * incY))
img8 = PhotoImage(file=srcList[8])
itemLabel8 = Label(
    selectionWindow,
    height=90,
    width=265,
    bg=labelBackGround,
    image=img8
)
itemLabel8.place(x=defaultButtonX + incX, y=defaultButtonY + (2 * incY))

#############################

historyButton = Button(
    selectionWindow,
    text='User Details\n\n(History)',
    font=("Gothic", 20),
    bg='white',
    fg='black',
    bd='7',
    height='4',
    width='20',
    relief=RAISED,
    command=openUserDetailsForm,
)
historyButton.place(x=30, y=882)

logoutButton = Button(
    selectionWindow,
    text='Log Out',
    height='4',
    width='20',
    bg='white',
    fg='black',
    bd='7',
    relief=RAISED,
    font=('Gothic', 20),
    command=openLogForm,
)
logoutButton.place(x=1270, y=890)

quitButton = Button(
    selectionWindow,
    text='Quit',
    font=("Gothic", 20),
    bg='white',
    fg='black',
    bd='7',
    height='4',
    width='20',
    relief=RAISED,
    command=quitSelectionWindow
)
quitButton.place(x=1590, y=890)

historyButton.bind('<Enter>', on_enter_historyButton)
historyButton.bind('<Leave>', on_leaving_historyButton)
logoutButton.bind('<Enter>', on_enter_logoutButton)
logoutButton.bind('<Leave>', on_leaving_logoutButton)
quitButton.bind('<Enter>', on_enter_quit)
quitButton.bind('<Leave>', on_leaving_quit)

selectionWindow.mainloop()
