from tkinter import *
from time import sleep
from random import randint
from threading import Thread
from PIL import Image, ImageTk


class Window():
    def __init__(self, master) -> None: #This contains most of the variables and widgets in the game
        self._master = master
        self._master.attributes("-fullscreen", True)
        self._width = self._master.winfo_screenwidth()
        self._height = self._master.winfo_screenheight()
        self._master.bind("<Escape>", quit)
        self.level = 1
            
        '''For the main interface'''
        self._mainmenu = Canvas(self._master, width=self._width,
                                height=self._height, highlightthickness=0)

        self._gameTitle = Label(self._mainmenu, bg="black", text=
"""Five Nights at Freddy's""",
                                font=("Helvetica", 50), fg='white')
        
        self._gameTitle_width = self._gameTitle.winfo_reqwidth()

        self._mainmenuFrame = Frame(self._mainmenu)

        self._newGameButton = Button(self._mainmenuFrame, text="New Game",
                                     fg="white", bg="black", font=("Helvetica", 30), command=self.newgame)

        self._continueButton = Button(self._mainmenuFrame, text="Continue",
                                      fg="white", bg="black", font=("Helvetica", 30), command=self.continueButton)

        self._quitButton = Button(self._mainmenuFrame, text="Quit",
                                  fg="white", bg="black",font=("Helvetica", 30), command=quit)

        '''For displaying what night it is'''
        self._nightCanvas = Canvas(self._master,
                                   width=self._width,
                                   height=self._height,
                                   highlightthickness=0)
        
        self._showNight = Label(self._nightCanvas, text=f'Night {self.level}', font=(
            'helvetica', 30), fg='white', bg='black')

        self._gameCanvas = Canvas(self._master, bg='black',
                                  highlightthickness=0,
                                  scrollregion=(-300, 0, self._width+300, self._height))
        
        self._gameCanvas.bind("<Motion>", self.scrollEffectAndCams)

        #initializing the images used in the game
        self.mainmenu_image = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\mainmenu.png")
        
        self.resized_mainmenu = self.mainmenu_image.resize(
            (int(self._width), int(self._height)))
        self.adjusted_mainmenu = ImageTk.PhotoImage(self.resized_mainmenu)
        self._mainmenu.create_image(0, 0, anchor=NW, image=self.adjusted_mainmenu)
        
        self.background_image1 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg1.png")
        self.background_image2 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg2.png")
        self.background_image3 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg3.png")
        self.background_image4 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg4.png")
        self.background_image5 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg5.png")
        self.background_image6 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg6.png")
        self.background_image7 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg7.png")
        self.background_image8 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg8.png")
        self.background_image9 = Image.open(
            "C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\bg9.png")
        
        # Resize the image based on screen dimensions
        self.resized_bgimage = self.background_image1.resize(
            (int(self._width)+600, int(self._height)))
        self.adjusted_bgimage = ImageTk.PhotoImage(self.resized_bgimage)
        self.bg = self._gameCanvas.create_image(-300, 0,anchor=NW, image=self.adjusted_bgimage)
        
        self.cam1pic1 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam1pic1.png")
        self.cam1pic2 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam1pic2.png")
        self.cam1pic3 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam1pic3.png")
        self.cam1pic4 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam1pic4.png")

        self.cam2pic1 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam2pic1.png")
        self.cam2pic2 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam2pic2.png")
        self.cam2pic3 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam2pic3.png")
        self.cam2pic4 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam2pic4.png")

        self.cam3pic1 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam3pic1.png")
        self.cam3pic2 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam3pic2.png")

        self.cam4pic1 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam4pic1.png")
        self.cam4pic2 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam4pic2.png")

        self.cam5pic1 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam5pic1.png")
        self.cam5pic2 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam5pic2.png")
        self.cam5pic3 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam5pic3.png")
        
        self.cam6pic1 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam6pic1.png")
        self.cam6pic2 = PhotoImage(
            file="C:\\Users\\joshu\\OneDrive\\Desktop\\Python\\Practice\\tkinter\\Images\\cam6pic2.png")


        self.turnOnThread = False
        self.foxyAnger = 0
        self.bonniesLocation = {
            "inShowStage": True,
            "inDiningArea": False,
            "inSupplyCloset": False,
            "inLeftHallway": False,
            "outsideLeftDoor": False,
            "atLeftDoor": False
        }
        
        self.chicasLocation = {
            "inShowStage": True,
            "inDiningArea": False,
            "inRightHallway": False,
            "outsideRightDoor": False,
            "atRightDoor": False
        }

        self.leftDoorOpen = True
        self.rightDoorOpen = True
        self.leftLightOn = False
        self.rightLightOn = False

        self.batteryLife = 1003
        self.showBattery = Label(self._gameCanvas, text=f"{100}%",
                                 foreground='white', background='black')

        self.timePassed = 0
        self.officeTime = Label(
            self._gameCanvas, foreground="white", background="black")

        self.leftDoor = Button(self._gameCanvas, text="Open",
                               background="black", foreground="white", command=self.closeLeftDoor)

        self.rightDoor = Button(self._gameCanvas, text="Open",
                                background="black", foreground="white", command=self.closeRightDoor)

        self.leftLight = Button(self._gameCanvas, text="Off",
                                background="black", foreground="white", command=self.turnOnLeftLight)

        self.rightLight = Button(self._gameCanvas, text="Off",
                                 background="black", foreground="white", command=self.turnOnRightLight)


        self._camOn = False
        self.cctvs = Frame(self._gameCanvas, background="black")
        self.cam1Label = Label(self.cctvs, background="black")
        self.cam2Label = Label(self.cctvs, background="black")
        self.cam3Label = Label(self.cctvs, background="black")
        self.cam4Label = Label(self.cctvs, background="black")
        self.cam5Label = Label(self.cctvs, background="black")
        self.cam6Label = Label(self.cctvs, background="black")
        self.cam1 = Button(self.cctvs, background="blue",
                           text="Stage", command=self.toggleCam1)
        self.cam2 = Button(self.cctvs, background="white",
                           text="Dining Hall", command=self.toggleCam2)
        self.cam3 = Button(self.cctvs, background="red",
                           text="Supply Room", command=self.toggleCam3)
        self.cam4 = Button(self.cctvs, background='green',
                           text="Left Hallway", command=self.toggleCam4)
        self.cam5 = Button(self.cctvs, background="yellow",
                           text="Pirate's Cove", command=self.toggleCam5)
        self.cam6 = Button(self.cctvs, background="pink",
                           text="Right Hallway", command=self.toggleCam6)
        self.camButton = Button(self.cctvs, background="white", command=self.resetCams)
        self.checkCams = False
            
            
    def backgroundImage(self): #Changes the background image depends onf 
        while self.turnOnThread:
            if self.bonniesLocation["outsideLeftDoor"] and self.leftLightOn and self.chicasLocation["outsideRightDoor"] and self.rightLightOn:
                self.resized_bgimage = self.background_image4.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(
                    self.resized_bgimage)
                self._gameCanvas.delete(self.bg)
                self.bg1 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)
                
            
            elif not self.leftDoorOpen and not self.rightDoorOpen:
                self.resized_bgimage = self.background_image7.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(
                    self.resized_bgimage)
                self._gameCanvas.delete(self.bg)
                self.bg2 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)
            
            elif not self.leftDoorOpen and self.chicasLocation["outsideRightDoor"] and self.rightLightOn:
                self.resized_bgimage = self.background_image9.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(
                    self.resized_bgimage)
                self._gameCanvas.delete(self.bg)
                self.bg3 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)
            
            elif not self.rightDoorOpen and self.bonniesLocation["outsideLeftDoor"] and self.leftLightOn:
                self.resized_bgimage = self.background_image9.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(
                    self.resized_bgimage)
                self._gameCanvas.delete(self.bg)
                self.bg4 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)
                
            elif not self.leftDoorOpen:
                self.resized_bgimage = self.background_image8.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(
                    self.resized_bgimage)
                self._gameCanvas.delete(self.bg)
                self.bg5 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)
                
            elif not self.rightDoorOpen:
                self.resized_bgimage = self.background_image6.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(
                    self.resized_bgimage)
                self._gameCanvas.delete(self.bg)
                self.bg6 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)
                
            elif self.chicasLocation["outsideRightDoor"] and self.rightLightOn:
                self.resized_bgimage = self.background_image3.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(
                    self.resized_bgimage)
                self._gameCanvas.delete(self.bg)
                self.bg7 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)

            elif self.bonniesLocation["outsideLeftDoor"] and self.leftLightOn:
                self.resized_bgimage = self.background_image2.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(
                    self.resized_bgimage)
                self._gameCanvas.delete(self.bg)
                self.bg8 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)
                
            else:
                self.resized_bgimage = self.background_image1.resize(
                    (int(self._width)+600, int(self._height)))
                self.adjusted_bgimage = ImageTk.PhotoImage(self.resized_bgimage)
                self.bg9 = self._gameCanvas.create_image(-300, 0,
                                                         anchor=NW, image=self.adjusted_bgimage)
            
            sleep(0.1)
            
    def run(self): #Runs the game
        self._mainmenu.pack(expand=YES, fill=BOTH)
        self._gameTitle.place(x=(self._width-self._gameTitle_width)//7, y=250)
        self._mainmenuFrame.place(x=(self._width-235)//3.5, y=400)
        self._newGameButton.pack(expand=YES, fill=BOTH)
        self._continueButton.pack(expand=YES, fill=BOTH)
        self._quitButton.pack(expand=YES, fill=BOTH)
        self._master.mainloop()

    def displayNight(self): #Displays the night (Night 1, Night 2, Night 3)
        self._mainmenu.pack_forget()
        self._nightCanvas.pack(expand=YES, fill=BOTH)
        self._showNight.pack(expand=YES, fill=BOTH)
        self._master.after(5000, self._nightCanvas.pack_forget)
        self._master.after(5000, self.runGame)

    def runGame(self): #Starts the game
        self._gameCanvas.pack(expand=YES, fill=BOTH)
        self.officeTime.place(x=(self._width)//2, y=0)
        self.showBattery.place(x=0, y=0)
        self.leftDoor_window = self._gameCanvas.create_window(
            (0), self._height//2, anchor=NW, window=self.leftDoor)
        self.rightDoor_window = self._gameCanvas.create_window(
            (self._width), self._height//2, anchor=NE, window=self.rightDoor)
        self.leftDoor_window = self._gameCanvas.create_window(
            (0), (self._height//2)+50, anchor=NW, window=self.leftLight)
        self.leftDoor_window = self._gameCanvas.create_window(
            (self._width), (self._height//2) + 50, anchor=NE, window=self.rightLight)

        self.turnOnThread = True
        self.gamethread()
        
    def newgame(self):
        self.level = 1
        self._showNight.config(text=f"Night {self.level}")
        self.displayNight()
        
    def continueButton(self):
        if self.level == 1:
            pass
        else:
            self.displayNight()
        
    def cameraFunction(self): #Contains all of the widgets for the camera system
        self.cam1.grid(row=0, column=0, sticky=NSEW)
        self.cam2.grid(row=0, column=1, sticky=NSEW)
        self.cam3.grid(row=0, column=2, sticky=NSEW)
        self.cam4.grid(row=1, column=0, sticky=NSEW)
        self.cam5.grid(row=1, column=1, sticky=NSEW)
        self.cam6.grid(row=1, column=2, sticky=NSEW)
        self.camButton.grid(row=2, column=0, columnspan=3, sticky=NSEW)
        self.cctvs.rowconfigure(0, weight=1)
        self.cctvs.rowconfigure(1, weight=1)
        self.cctvs.columnconfigure(0, weight=1)
        self.cctvs.columnconfigure(1, weight=1)
        self.cctvs.columnconfigure(2, weight=1)
        
    def scrollEffectAndCams(self, event): #Allows scrolling when the cursor is on the sides

        x = event.x
        y = event.y

        if x < 1:
            self._gameCanvas.xview_scroll(-1, "units")

        if x > self._width-2:
            self._gameCanvas.xview_scroll(1, "units")

        if y > self._height-2:
            self._camOn = True
            self.cctvs.pack(expand=YES, fill=BOTH)
            self.cameraFunction()

    def gridForget(self): #forgets the six cams
        self.cam1.grid_forget()
        self.cam2.grid_forget()
        self.cam3.grid_forget()
        self.cam4.grid_forget()
        self.cam5.grid_forget()
        self.cam6.grid_forget()
    
    def camLabelForget(self):#includes the labels where the images will be shown
        self.cam1Label.grid_forget()
        self.cam2Label.grid_forget()
        self.cam3Label.grid_forget()
        self.cam4Label.grid_forget()
        self.cam5Label.grid_forget()
        self.cam6Label.grid_forget()
        
    def resetCams(self): #this function will be the one incharge for the back button in the camera system
        if self.checkCams:
            self.camLabelForget()
            self.cameraFunction()
            self.checkCams = False
        else:
            self.camLabelForget()
            self.cctvs.pack_forget()
            self._camOn = False

    def cam1Update(self): #Updates the image shown when opening the cams based on the location of the enemies
        while self.turnOnThread:
            if self.bonniesLocation["inShowStage"] and self.chicasLocation["inShowStage"]:
                self.cam1Label.config(image=self.cam1pic1)
            elif self.chicasLocation["inShowStage"]:
                self.cam1Label.config(image=self.cam1pic2)
            elif self.bonniesLocation["inShowStage"]:
                self.cam1Label.config(image=self.cam1pic3)
            else:
                self.cam1Label.config(image=self.cam1pic4)
            sleep(0.1)

    def cam2Update(self):
        while self.turnOnThread:
            if self.bonniesLocation["inDiningArea"] and self.chicasLocation["inDiningArea"]:
                self.cam2Label.config(image=self.cam2pic4)
            elif self.bonniesLocation["inDiningArea"]:
                self.cam2Label.config(image=self.cam2pic2)
            elif self.chicasLocation["inDiningArea"]:
                self.cam2Label.config(image=self.cam2pic3)
            else:
                self.cam2Label.config(image=self.cam2pic1)
            sleep(0.1)

    def cam3Update(self):
        while self.turnOnThread:
            if self.bonniesLocation["inSupplyCloset"]:
                self.cam3Label.config(image=self.cam3pic2)
            else:
                self.cam3Label.config(image=self.cam3pic1)
            sleep(0.1)

    def cam4Update(self):
        while self.turnOnThread:
            if self.bonniesLocation["inLeftHallway"]:
                self.cam4Label.config(image=self.cam4pic2)
            else:
                self.cam4Label.config(image=self.cam4pic1)
            sleep(0.1)

    def cam5Update(self): #Updates what phase of foxy is shown in the pirate's cove
        while self.turnOnThread:
            if self.foxyAnger < 75:
                self.cam5Label.config(image=self.cam5pic1)
            elif self.foxyAnger < 100:
                self.cam5Label.config(image=self.cam5pic2)
            else:
                self.cam5Label.config(image=self.cam5pic3)
            sleep(0.1)

    def cam6Update(self):
        while self.turnOnThread:
            if self.chicasLocation["inRightHallway"]:
                self.cam6Label.config(image=self.cam6pic2)
            else:
                self.cam6Label.config(image=self.cam6pic1)
            sleep(0.1)

    def toggleCam1(self): #Opens respective camera when clicked
        self.gridForget()
        self.cam1Label.grid(row=0, column=0, rowspan=3,
                            columnspan=3, sticky=NSEW)
        self.checkCams = True

    def toggleCam2(self):
        self.gridForget()
        self.cam2Label.grid(row=0, column=0, rowspan=3,
                            columnspan=3, sticky=NSEW)
        self.checkCams = True

    def toggleCam3(self):
        self.gridForget()
        self.cam3Label.grid(row=0, column=0, rowspan=3,
                            columnspan=3, sticky=NSEW)
        self.checkCams = True

    def toggleCam4(self):
        self.gridForget()
        self.cam4Label.grid(row=0, column=0, rowspan=3,
                            columnspan=3, sticky=NSEW)
        self.checkCams = True

    def toggleCam5(self):
        self.gridForget()
        self.cam5Label.grid(row=0, column=0, rowspan=3,
                            columnspan=3, sticky=NSEW)
        self.checkCams = True

    def toggleCam6(self):
        self.gridForget()
        self.cam6Label.grid(row=0, column=0, rowspan=3,
                            columnspan=3, sticky=NSEW)
        self.checkCams = True

    def closeLeftDoor(self): 
        if self.leftDoorOpen:
            self.leftDoorOpen = False
            self.leftDoor.config(text="Close")
        else:
            self.leftDoorOpen = True
            self.leftDoor.config(text="Open")

    def closeRightDoor(self):
        if self.rightDoorOpen: 
            self.rightDoorOpen = False
            self.rightDoor.config(text="Close")
        else:
            self.rightDoorOpen = True
            self.rightDoor.config(text="Open")

    def turnOnLeftLight(self):
        if self.leftLightOn:
            self.leftLightOn = False
            self.leftLight.config(text="Off")
        else:
            self.leftLightOn = True
            self.leftLight.config(text="On")

    def turnOnRightLight(self):
        if self.rightLightOn:
            self.rightLightOn = False
            self.rightLight.config(text="Off")
        else:
            self.rightLightOn = True
            self.rightLight.config(text="On")

    def battery(self): #Shows battery and decrements the battery as time goes by
        while self.turnOnThread:
            batDepletion = 0.09
            if not self.leftDoorOpen:
                batDepletion += 0.27
            if not self.rightDoorOpen:
                batDepletion += 0.27
            if self.leftLightOn:
                batDepletion += 0.18
            if self.rightLightOn:
                batDepletion += 0.18
            if self._camOn:
                batDepletion += 0.2

            self.batteryLife -= batDepletion
            self.showBattery.config(text=f"{int(self.batteryLife//10)}%")
            sleep(0.1)

            if self.batteryLife <= 0:
                self.jumpScare()

    def gameTime(self): #Shows and updates the time in the game
        while self.turnOnThread:
            if self.timePassed < 50:
                timeInGame = 12
            else:
                timeInGame = self.timePassed//50

            self.timePassed += 1
            self.officeTime.config(text=f"{timeInGame}:00AM")
            sleep(1)
            
            if self.timePassed == 300:
                self.winning()

    def foxxyMoving(self): #In charge of Foxxy's actions in the game
        while self.turnOnThread:
            if self.foxyAnger > 100:
                sleep(3)
                if not self.leftDoorOpen:
                    self.batteryLife -= 20 + (self.level*10)
                    self.foxyAnger = 0
                    
                else:
                    self.jumpScare()

            if not self._camOn:
                self.foxyAnger += 0.08*self.level  # Set this to 0.08 if foxxy is already animated
            sleep(0.1)

    def bonnieMoving(self): #In charge of Bonnie's actions in the game
        bonnie = "inShowStage"
        randomNumBonnie = 0
        while self.turnOnThread:
            if self.level == 1:
                rand = 3
            elif self.level == 2:
                rand = 6
            else:
                rand = 10
            print(self.level, "Bon")

            # Bonnies Transition

            if self.bonniesLocation["inShowStage"] and 0 < randomNumBonnie < rand:
                bonnie = "inDiningArea"
            elif self.bonniesLocation["inDiningArea"] and 0 < randomNumBonnie < rand:
                bonnie = "inSupplyCloset"
            elif self.bonniesLocation["inSupplyCloset"] and 0 < randomNumBonnie < rand:
                bonnie = "inLeftHallway"
            elif self.bonniesLocation["inLeftHallway"] and 0 < randomNumBonnie < rand:
                self.bonniesLocation["inLeftHallway"] = False
                self.bonniesLocation["outsideLeftDoor"] = True
                sleep(6)
                continue
            elif self.bonniesLocation["outsideLeftDoor"]:
                self.bonniesLocation["outsideLeftDoor"] = False
                self.bonniesLocation["atLeftDoor"] = True
                sleep(4)
                continue
            elif self.bonniesLocation["atLeftDoor"]:
                bonnie = "inShowStage"

            for location in self.bonniesLocation:
                if bonnie == location:
                    self.bonniesLocation[location] = True
                    print(location)
                else:
                    self.bonniesLocation[location] = False
            sleep(3)
            randomNumBonnie = randint(1, 20)
            print(randomNumBonnie)
            # Chicas Transitions

    def chicaMoving(self): #In charge of Chica's actions in the game
        chica = "inShowStage"
        randomNumChica = 0
        while self.turnOnThread:
            if self.level == 1:
                rand = 3
            elif self.level == 2:
                rand = 6
            else:
                rand = 10

            if self.chicasLocation["inShowStage"] and 0 < randomNumChica < rand:
                chica = "inDiningArea"
            elif self.chicasLocation["inDiningArea"] and 0 < randomNumChica < rand:
                chica = "inRightHallway"
            elif self.chicasLocation["inRightHallway"] and 0 < randomNumChica < rand:
                self.chicasLocation["inRightHallway"] = False
                self.chicasLocation["outsideRightDoor"] = True
                sleep(6)
                continue
            elif self.chicasLocation["outsideRightDoor"]:
                self.chicasLocation["outsideRightDoor"] = False
                self.chicasLocation["atRightDoor"] = True
                sleep(3)
                continue
            elif self.chicasLocation["atRightDoor"]:
                chica = "inShowStage"

            for location in self.chicasLocation:
                if chica == location:
                    self.chicasLocation[location] = True
                    print(location)
                else:
                    self.chicasLocation[location] = False

            sleep(5)
            randomNumChica = randint(1, 20)
            print(randomNumChica)

    def bonnieDoorInteraction(self): #In charge checking if you closed the door on animatronics or what
        while self.turnOnThread:
            if self.bonniesLocation["atLeftDoor"] and self.leftDoorOpen:
                self.jumpScare()

            sleep(0.1)

    def chicaDoorInteraction(self):
        while self.turnOnThread:
            if self.chicasLocation["atRightDoor"] and self.rightDoorOpen:
                self.jumpScare()

            sleep(0.1)

    def gamethread(self): #Contains all the threads that are used in the game
        background_thread = Thread(target=self.backgroundImage, daemon=True)
        background_thread.start()
        
        bonnies_movement_thread = Thread(target=self.bonnieMoving, daemon=True)
        bonnies_movement_thread.start()

        chicas_movement_thread = Thread(target=self.chicaMoving, daemon=True)
        chicas_movement_thread.start()

        battery_usage_thread = Thread(target=self.battery, daemon=True)
        battery_usage_thread.start()

        game_time_thread = Thread(target=self.gameTime, daemon=True)
        game_time_thread.start()

        foxyGameplay_thread = Thread(target=self.foxxyMoving, daemon=True)
        foxyGameplay_thread.start()

        bonnieGameplay_thread = Thread(
            target=self.bonnieDoorInteraction, daemon=True)
        bonnieGameplay_thread.start()

        chicaGameplay_thread = Thread(
            target=self.chicaDoorInteraction, daemon=True)
        chicaGameplay_thread.start()

        cam1_thread = Thread(target=self.cam1Update, daemon=True)
        cam1_thread.start()

        cam2_thread = Thread(target=self.cam2Update, daemon=True)
        cam2_thread.start()

        cam3_thread = Thread(target=self.cam3Update, daemon=True)
        cam3_thread.start()

        cam4_thread = Thread(target=self.cam4Update, daemon=True)
        cam4_thread.start()

        cam5_thread = Thread(target=self.cam5Update, daemon=True)
        cam5_thread.start()

        cam6_thread = Thread(target=self.cam6Update, daemon=True)
        cam6_thread.start()

    def winning(self): #Called if you survive until 6am, shows the congrats interface
        
        self.turnOnThread = False
        self.resetAll()
        self._gameCanvas.pack_forget()
        self.level += 1
        winningCanvas = Canvas(
            self._master, background="black", highlightthickness=0)
        winningCanvas.pack(expand=YES, fill=BOTH)

        congrats = Label(winningCanvas, text='CONGRATS', font=(
            'helvetica', 30), fg='white', bg='black')
        congratsHeight = congrats.winfo_reqheight()
        congratsWidth = congrats.winfo_reqwidth()
        congrats.place(x=(self._width-congratsWidth)//2,
                       y=(self._height-congratsHeight)//2)
        self._master.after(5000, winningCanvas.destroy)
        self._showNight.config(text=f"Night {self.level}") #For some reason, if we did not config the text, it will always show Night 1 even if the level changed
        sleep(5)
        winningCanvas.pack_forget()
        
        if self.level == 4:
            self.level = 3
            self._showNight.config(text=f"Night {self.level}")
            self.gameComplete()
        else:
            self.displayNight()

    def jumpScare(self): #Called if an animatronic entered your room or if your battery runs out
        self.turnOnThread = False
        self.resetAll()
        self._gameCanvas.pack_forget()
        losingCanvas = Canvas(
            self._master, background="black", highlightthickness=0)
        losingCanvas.pack(expand=YES, fill=BOTH)

        jumpscare = Label(losingCanvas, text='RAWR', font=(
            'helvetica', 30), fg='white', bg='black')
        jumpHeight = jumpscare.winfo_reqheight()
        jumpWidth = jumpscare.winfo_reqwidth()
        jumpscare.place(x=(self._width-jumpWidth)//2,
                        y=(self._height-jumpHeight)//2)

        self._master.after(5000, losingCanvas.destroy)
        sleep(5)
        self.run()

    def gameComplete(self):
        CompletionCanvas = Canvas(
            self._master, background="blue", highlightthickness=0)
        CompletionCanvas.pack(expand=YES, fill=BOTH)

        completed = Label(CompletionCanvas, text='CONGRATS', font=(
            'helvetica', 30), fg='white', bg='black')
        completed.pack()
        congratsHeight = completed.winfo_reqheight()
        congratsWidth = completed.winfo_reqwidth()
        completed.place(x=(self._width-congratsWidth)//2,
                       y=(self._height-congratsHeight)//2)
        self._master.after(5000, CompletionCanvas.destroy)
        sleep(5)
        self.run()
    
    def resetAll(self): #Resets all states
        self.batteryLife = 1003
        self. timePassed = 0
        self.checkCams = False
        self._camOn = False
        self.cctvs.pack_forget()
        self.gridForget()
        self.camLabelForget()
        self.leftDoor.config(text="Open")
        self.rightDoor.config(text="Open")
        self.leftLight.config(text="Off")
        self.rightLight.config(text="Off")
        self.foxyAnger = 0
        self.bonniesLocation = {
            "inShowStage": True,
            "inDiningArea": False,
            "inSupplyCloset": False,
            "inLeftHallway": False,
            "outsideLeftDoor": False,
            "atLeftDoor": False
        }
        self.chicasLocation = {
            "inShowStage": True,
            "inDiningArea": False,
            "inRightHallway": False,
            "outsideRightDoor": False,
            "atRightDoor": False
        }

        self.leftDoorOpen = True
        self.rightDoorOpen = True
        self.leftLightOn = False
        self.rightLightOn = False

def firstgame(): #Calls the game
    if __name__ == "__main__":
        game = Tk()
        fnaf = Window(game)
        fnaf.run()

firstgame()
