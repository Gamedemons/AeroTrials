from tkinter import *
import random
import subprocess

startWindow = Tk()
startWindow.title('Enigma')
startWindow.geometry('1920x1080')
startWindow.resizable(0, 0)
# startWindow.overrideredirect(True)
# startWindow.geometry("{0}x{1}+0+0".format(startWindow.winfo_screenwidth(), startWindow.winfo_screenheight()))
startWindow.wm_iconbitmap('Filters\\Icons\\chat.ico')
backgroundImage = PhotoImage(file='Filters\\BackGround\\9.png')
slicer = PhotoImage(file='Filters\\BackGround\\t.gif')
startWindow.config(bg='#60616b')

# Global Variables
colorList = ['white', 'red', '#0dff7e', 'blue', 'pink', 'yellow', '#ff8d87',
             '#ffaa54', '#e0ff54', '#87ff54', '#54ff90', '#54ffe0', '#54aaff',
             '#9354ff', '#eda5fa', '#fcb6df', '#a6a1a2']
startHeaderColor = 1


# Functions
def aboutUs():
    teamInfoPanel = Toplevel(startWindow)
    teamInfoPanel.title('About Us')
    teamInfoPanel.geometry('320x230')
    teamInfoPanel.resizable(0, 0)
    teamInfoPanel.wm_iconbitmap('Filters\\Icons\\among_us_player_light_blue_icon.ico')
    teamInfoPanel.config(bg='white')

    def on_enter_aboutUs(e):
        teamInfoPanel.config(bg='#7c008f')
        teamNameHeader.config(bg='#7c008f', fg='white')
        teamMembersLabel.config(bg='#7c008f', fg='white')

    def on_leaving_aboutUs(e):
        teamInfoPanel.config(bg='white')
        teamNameHeader.config(bg='white', fg='black')
        teamMembersLabel.config(bg='white', fg='black')

    teamNameHeader = Label(
        teamInfoPanel,
        text='Enigma',
        bg='white',
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
        bg='white',
        fg='black'
    )
    teamMembersLabel.place(x=15, y=75)
    teamMembersLabel.config(font=("Courier New Bold Italic", 18))

    teamInfoPanel.bind('<Enter>', on_enter_aboutUs)
    teamInfoPanel.bind('<Leave>', on_leaving_aboutUs)


def on_enter_startHeader(e):
    global startHeaderColor
    startHeaderColor = randCorrection()
    if startHeaderColor is None:
        startHeader.config(bg='#60616b', fg='#00ffaa')
    else:
        startHeader.config(bg='#60616b', fg=colorList[startHeaderColor - 1])


# def on_leaving_startHeader(e):
#     startHeader.config(bg='#60616b', fg='white')


def on_enter_teamNameLabel(e):
    teamNameLabel.config(bg='#60616b', fg="#ffb152")


def on_leaving_teamNameLabel(e):
    teamNameLabel.config(bg='#60616b', fg='white')


def on_enter_aboutButton(e):
    aboutButton.config(bg='#0dff7e', fg="white")


def on_leaving_aboutButton(e):
    aboutButton.config(bg='white', fg='black')


def on_enter_enterButton(e):
    enterButton.config(bg='#52dcf7', fg="white")


def on_leaving_enterButton(e):
    enterButton.config(bg='white', fg='black')


def on_enter_quit(e):
    quitButton.config(bg='black', fg='white')


def on_leaving_quit(e):
    quitButton.config(bg='white', fg='black')


def on_enter_description(e):
    descriptionHead.config(fg='#ff541c')
    descriptionLabel.config(fg='yellow')


def on_leaving_description(e):
    descriptionHead.config(fg='white')
    descriptionLabel.config(fg='white')


def on_enter_contact(e):
    contactHead.config(fg='#ff541c')
    contactLabel.config(fg='yellow')


def on_leaving_contact(e):
    contactHead.config(fg='white')
    contactLabel.config(fg='white')


def quitStartFrame():
    startWindow.destroy()


def generateRandInt():
    randomColor = random.randint(1, len(colorList))
    return randomColor


def randCorrection():
    randomNumber = generateRandInt()
    if randomNumber != startHeaderColor:
        return randomNumber
    else:
        randCorrection()


def openLogForm():
    startWindow.destroy()
    subprocess.call(["python", "Log.py"])


# Start Window Background
# mainFrameBackground = Label(
#     startWindow,
#     image=backgroundImage
# )
# mainFrameBackground.place(x=-30, y=-70)


startHeader = Label(
    startWindow,
    text='AeroTrials',
    bg='#60616b',
    fg='white',
    font=('Gothic', 90, 'bold')
)
startHeader.pack(side=TOP, pady=50)

teamNameLabel = Label(
    startWindow,
    text='by Enigma',
    bg='#60616b',
    fg='white',
    font=('Gothic', 20, 'bold')
)
teamNameLabel.place(x=1123, y=180)

descriptionHead = Label(
    startWindow,
    justify=LEFT,
    text='What we do...',
    bg='#60616b',
    fg='white',
    font=('Gothic', 40, 'bold')
)
descriptionHead.place(x=30, y=270)

descriptionLabel = Label(
    startWindow,
    justify=LEFT,
    text='AeroTrials is a groundbreaking \n\napp built by the developers of \n\nEnigma. '
         'It allows a user to try \n\non products using in a virtual \n\nworld making it '
         'easier to make \n\ndecisions. We here at Enigma \n\ntry our best to make your lives '
         '\n\neasier and better',
    bg='#60616b',
    fg='white',
    font=('Gothic', 20)
)
descriptionLabel.place(x=30, y=360)

contactHead = Label(
    startWindow,
    justify=LEFT,
    text='Contact Us',
    bg='#60616b',
    fg='white',
    font=('Gothic', 40, 'bold')
)
contactHead.place(x=30, y=830)

contactLabel = Label(
    startWindow,
    justify=LEFT,
    text='Email : manthanrajrajoria@gmail.com\n\n'
         'Ph.No : 7689904767',
    bg='#60616b',
    fg='white',
    font=('Gothic', 20)
)
contactLabel.place(x=30, y=910)

enterButton = Button(
    startWindow,
    text="Start the journey",
    justify=LEFT,
    height='4',
    width='20',
    bg='white',
    fg='black',
    bd='7',
    relief=RAISED,
    font=('Gothic', 30, 'bold'),
    command=openLogForm
)
enterButton.pack(side=TOP, pady=300)

errorLabel = Label(
    startWindow,
    text='',
    width='29',
    font=('Gothic', 20, 'bold'),
    bg='#60616b',
    fg='#ff7a7a',
)
errorLabel.place(x=740, y=740)

aboutButton = Button(
    startWindow,
    text="About Us",
    height='4',
    width='20',
    bg='white',
    fg='black',
    bd='7',
    relief=RAISED,
    font=('Gothic', 20),
    command=aboutUs
)
aboutButton.place(x=1583, y=740)

quitButton = Button(
    startWindow,
    height='4',
    width='20',
    text='Quit',
    bg='white',
    fg='black',
    bd='7',
    relief=RAISED,
    command=quitStartFrame
)
quitButton.config(font=("Gothic", 20))
quitButton.place(x=1583, y=882)


# Code
startHeader.bind('<Enter>', on_enter_startHeader)
# startHeader.bind('<Leave>', on_leaving_startHeader)

teamNameLabel.bind('<Enter>', on_enter_teamNameLabel)
teamNameLabel.bind('<Leave>', on_leaving_teamNameLabel)

aboutButton.bind('<Enter>', on_enter_aboutButton)
aboutButton.bind('<Leave>', on_leaving_aboutButton)

descriptionHead.bind('<Enter>', on_enter_description)
descriptionHead.bind('<Leave>', on_leaving_description)

descriptionLabel.bind('<Enter>', on_enter_description)
descriptionLabel.bind('<Leave>', on_leaving_description)

contactHead.bind('<Enter>', on_enter_contact)
contactHead.bind('<Leave>', on_leaving_contact)

contactLabel.bind('<Enter>', on_enter_contact)
contactLabel.bind('<Leave>', on_leaving_contact)

enterButton.bind('<Enter>', on_enter_enterButton)
enterButton.bind('<Leave>', on_leaving_enterButton)

quitButton.bind('<Enter>', on_enter_quit)
quitButton.bind('<Leave>', on_leaving_quit)

try:
    startWindow.mainloop()
except EXCEPTION:
    errorLabel.config(text='We encountered a error.')
