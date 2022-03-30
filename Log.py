from tkinter import *
import subprocess


# Colors
# b9e7f0
# 4fadb5
# 71cccc
# 9adde1
# e2f2f7
# ffffff
# dbc7b3


def disableCloseButton():
    pass


mainWindowFrame = Tk()
mainWindowFrame.title('Enigma')
mainWindowFrame.geometry('1920x1080')
mainWindowFrame.resizable(0, 0)
# mainWindowFrame.overrideredirect(True)
# mainWindowFrame.geometry("{0}x{1}+0+0".format(mainWindowFrame.winfo_screenwidth(), mainWindowFrame.winfo_screenheight()))
mainWindowFrame.wm_iconbitmap('Filters\\Icons\\chat.ico')
mainWindowFrame.protocol("WM_DELETE_WINDOW", disableCloseButton)
backgroundImage = PhotoImage(file='Filters\\BackGround\\seaborn.png')


# Methods
def on_enter_startButton(e):
    startButton.config(fg="white", bg='#0dff7e')


def on_leaving_startButton(e):
    startButton.config(fg='black', bg='white')


def on_enter_aboutUsButton(e):
    aboutUsButton.config( fg="white", bg='#006dc7')


def on_leaving_aboutUsButton(e):
    aboutUsButton.config(fg='black', bg='white')


def on_enter_backButton(e):
    backButton.config(fg="white", bg='#a900c7')


def on_leaving_backButton(e):
    backButton.config(fg='black', bg='white')


def on_enter_quitButton(e):
    quitButton.config(fg="white", bg='black')


def on_leaving_quitButton(e):
    quitButton.config(fg='black', bg='white')


def quitMainFrame():
    try:
        with open("Data.txt", "w") as dataFile:
            dataFile.write("")
        mainWindowFrame.destroy()
    except IOError:
        errorLabel.config(text='Error quitting frame.')


def closeMainFrame():
    try:
        mainWindowFrame.destroy()
    except IOError:
        errorLabel.config(text='Error closing window.')


def aboutUs():
    teamInfoPanel = Toplevel(mainWindowFrame)
    teamInfoPanel.title('About Us')
    teamInfoPanel.geometry('320x250')
    teamInfoPanel.resizable(0, 0)
    teamInfoPanel.wm_iconbitmap('Filters\\Icons\\among_us_player_light_blue_icon.ico')
    teamInfoPanel.config(bg='#a3fffa')
    teamNameHeader = Label(
        teamInfoPanel,
        text='Enigma',
        bg='#a3fffa',
        fg='black'
    )
    teamNameHeader.place(x=15, y=20)
    teamNameHeader.config(font=("Courier New Bold Italic", 30))

    teamMembersLabel = Label(
        teamInfoPanel,
        justify=LEFT,
        text='Manthan Raj Rajoria\n'
             'Vedansh Chasta\n'
             'Mohit Agarwal\n'
             'Naveen Kumar Jangir',
        bg='#a3fffa',
        fg='black',
        font=("Courier New Bold Italic", 18, 'bold')
    )
    teamMembersLabel.place(x=15, y=75)


def dataConfirmation():
    userName = usernameField.get(1.0, "end-1c")
    email = emailField.get(1.0, "end-1c")
    password = passwordField.get()

    def usernameCheck():
        symbols = '!@#$%^&*()-+={}[]|\\:;\"\'<,>.?/~`'
        ini = True
        for i in symbols:
            if i in userName or ' ' in userName:
                ini = False
                break
            else:
                ini = True
        return ini

    def emailCheck():
        if '@' in email and '.' in email:
            emailPart1 = email.split('@')
            if '.' in emailPart1[0]:
                return False
            emailPart2 = emailPart1[1].split('.')
            totalParts = len(emailPart1) + len(emailPart2)
            if len(emailPart1[0]) >= 1 and len(emailPart2[0]) >= 1 and len(emailPart2[1]) >= 1 and totalParts == 4:
                symbols = '!#$%^&*()-+={}[]|\\:;\"\'<,>?/~`'
                for i in symbols:
                    if i in emailPart1[0] or ' ' in emailPart1[0] or i in emailPart2[0] or ' ' in emailPart2[0] or i in emailPart1[1] or ' ' in emailPart2[1]:
                        return False
                return True
            return False
        else:
            return False

    def passwordCheck():
        if len(password) >= 8:
            return True
        else:
            return False

    if userName != '' and email != '' and password != '' and usernameCheck() and emailCheck() and passwordCheck():
        with open("Data.txt", "w") as dataFile:
            text = userName + '\t' + email.lower() + '\t' + password
            dataFile.write(text)
        mainWindowFrame.destroy()
        subprocess.call(["python", "Catalogue.py"])
    else:
        if userName == '' or usernameCheck() is False:
            errorLabel.config(text='Enter a valid name')
        if emailCheck() is False or passwordCheck() is False:
            errorLabel.config(text='Enter a valid email and password !')


def openStartForm():
    mainWindowFrame.destroy()
    subprocess.call(["python", "Start.py"])


# Window Controls
mainFrameBackground = Label(
    mainWindowFrame,
    image=backgroundImage
)
mainFrameBackground.place(x=-2, y=-2)

infoHeader = Label(
    mainWindowFrame,
    text="Product Trials",
    height=1,
    width=20,
    bg='#b9e7f0'

)
infoHeader.config(font=("Gothic", 90))
infoHeader.pack(side=TOP, pady='40')

teamInfo = Label(
    mainWindowFrame,
    text="by Enigma",
    height=1,
    width=20,
    bg='#4fadb5'
)
teamInfo.config(font=("Gothic", 26, 'bold'))
teamInfo.place(x=1100, y=220)

usernameLabel = Label(
    mainWindowFrame,
    text='Username',
    font=("Gothic", 30),
    bg='#71cccc'
)
usernameLabel.place(x=230, y=348)

usernameField = Text(
    mainWindowFrame,
    height=0,
    width=40,
    font=("Gothic", 30)
)
usernameField.place(x=500, y=348)

emailLabel = Label(
    mainWindowFrame,
    text='Email',
    font=("Gothic", 30),
    bg='#71cccc'
)
emailLabel.place(x=230, y=427)

emailField = Text(
    mainWindowFrame,
    height=0,
    width=40,
    font=("Gothic", 30)
)
emailField.place(x=500, y=428)

passwordLabel = Label(
    mainWindowFrame,
    text='Password',
    font=("Gothic", 30),
    bg='#9adde1'
)
passwordLabel.place(x=230, y=508)

passwordField = Entry(
    mainWindowFrame,
    show='*',
    width='40',
    font=("Gothic", 30)
)
passwordField.place(x=500, y=508)

errorLabel = Label(
    mainWindowFrame,
    text='',
    font=('Gothic', 20, 'bold'),
    fg='#ff7a7a',
    bg='#9adde1',
    width='38',
)
errorLabel.place(x=500, y=620)

startButton = Button(
    mainWindowFrame,
    text='Log In',
    height='3',
    width='15',
    bg='white',
    fg='black',
    bd='7',
    relief=RAISED,
    command=dataConfirmation
)
startButton.config(font=("Gothic", 20))
startButton.place(x=1080, y=620)

blackbox = Label(
    mainWindowFrame,
    bg='black',
    # height=0,
    width=2,
)
blackbox.place(x=240, y=920)

terms = Label(
    mainWindowFrame,
    text='Using out services means that you agree to our terms and conditions.\n'
         'Any violation of these will result in severe action.',
    font=('Gothic', 20),
    justify=LEFT,
    bg='#dbc7b3',
)
terms.place(x=260, y=900)

backButton = Button(
    mainWindowFrame,
    text='<- Back',
    height='3',
    width='15',
    bg='white',
    fg='black',
    bd='7',
    relief=RAISED,
    font=('Gothic', 20),
    command=openStartForm,
)
backButton.place(x=1666, y=660)

aboutUsButton = Button(
    mainWindowFrame,
    text='About Us',
    height='3',
    width='15',
    bg='white',
    fg='black',
    bd='7',
    relief=RAISED,
    font=('Gothic', 20),
    command=aboutUs
)
aboutUsButton.place(x=1666, y=790)

quitButton = Button(
    mainWindowFrame,
    text='Quit',
    height='3',
    width='15',
    relief=RAISED,
    bd='7',
    bg='white',
    fg='black',
    font=("Gothic", 20),
    command=quitMainFrame
)
quitButton.place(x=1666, y=920)

# Code
aboutUsButton.bind('<Enter>', on_enter_aboutUsButton)
aboutUsButton.bind('<Leave>', on_leaving_aboutUsButton)

startButton.bind('<Enter>', on_enter_startButton)
startButton.bind('<Leave>', on_leaving_startButton)

backButton.bind('<Enter>', on_enter_backButton)
backButton.bind('<Leave>', on_leaving_backButton)

quitButton.bind('<Enter>', on_enter_quitButton)
quitButton.bind('<Leave>', on_leaving_quitButton)

try:
    mainWindowFrame.mainloop()
except EXCEPTION:
    errorLabel.config(text='Unknown Error !')
