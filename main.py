import tkinter as tk
from tkinter.constants import ANCHOR, BOTTOM, CENTER, DISABLED, LEFT, N, RIGHT, S, TOP
import time

class App():
    
    def __init__(self):
        self.root = tk.Tk()
        self.screen = 1
        self.completedAnimedoros = 0
        self.studyTimer()
        self.root.mainloop()

    def studyCountdown(self):
        totalTime = tk.IntVar()
        totalTime = self.timerVar.get()
        self.screen = 0

        #destroys all the labels and entries and replaces with counter
        self.root.geometry('250x250')
        self.timerLabel.pack_forget()
        self.submitButton.pack_forget()
        self.timerEntryArea.pack_forget()
        self.studyCountdownLabel = tk.Label(self.root,font=("Arial", 25), text = totalTime)
        self.studyCountdownLabel.place(relx=0.5,rely=0.5, anchor=CENTER)

        #stop timer button
        self.stopButton = tk.Button(self.root, text = "Stop", command = self.stopTimer)
        self.stopButton.pack(side=BOTTOM, pady=15)

        #countdown timer 
        while (totalTime > 0):
            self.studyCountdownLabel['text'] = totalTime
            self.root.update()
            totalTime-=1
            time.sleep(1)
        self.studyCountdownLabel.destroy()
        self.stopButton.destroy()
        self.animeTimer()


    
    def studyTimer(self):
        self.root.geometry('250x250')
        self.root.title("Study Timer")
        self.timerVar = tk.IntVar()

        #created a label with an entry area for timer duration
        self.timerLabel = tk.Label(self.root, text = 'Timer Duration(Minutes)')
        self.timerLabel.pack(side=TOP)
        self.timerEntryArea = tk.Entry(self.root,textvariable = self.timerVar, width = 5)
        self.timerEntryArea.pack(side=TOP)

        #created submit button
        self.submitButton = tk.Button(self.root, text = 'Submit', command = self.studyCountdown)
        self.submitButton.pack(side=BOTTOM, pady=15)
    
    def animeTimer(self):
        self.root.geometry('300x250')
        self.root.title("Break Timer")
        self.timerVar = tk.IntVar()
        self.animeEntry = tk.StringVar()
        self.animeEP = tk.StringVar()

        #created a label with an entry area for timer duration
        self.timerLabel = tk.Label(self.root, text = 'Timer Duration(Minutes)')
        self.timerLabel.pack(side=TOP)
        self.timerEntryArea = tk.Entry(self.root,textvariable = self.timerVar, width = 5)
        self.timerEntryArea.pack(side=TOP)

        #Create a Entry for Anime watching
        self.animeLabel = tk.Label(self.root, text= "What are you watching?   EP #", pady=10)
        self.animeLabel.pack()
        self.animeEntryArea = tk.Entry(self.root, width=20, textvariable= self.animeEntry)
        self.animeEntryArea.pack()
        self.animeEPEntryArea = tk.Entry(self.root, width=5, textvariable= self.animeEP)
        self.animeEPEntryArea.place(in_= self.animeEntryArea, relx=1.1)

        #created submit button
        self.submitButton = tk.Button(self.root, text = 'Submit', command = self.animeCountdown)
        self.submitButton.pack(side=BOTTOM, pady=15)
        self.root.mainloop()

    def animeCountdown(self):
        #get() all my variables needed 
        self.screen = 1
        totalTime = tk.IntVar()
        totalTime = self.timerVar.get()
        currentAnime = self.animeEntry.get()
        currentEP = self.animeEP.get()

        #delete all labels
        self.timerLabel.pack_forget()
        self.timerEntryArea.pack_forget()
        self.submitButton.pack_forget()
        self.animeLabel.pack_forget()
        self.animeEntryArea.pack_forget()
        self.animeEPEntryArea.pack_forget()

        #create label with anime currently watching
        self.watchingLabel = tk.Label(self.root, text = ("Currently Watching " + currentAnime + " EP " + currentEP))
        self.watchingLabel.pack()

        #stop timer button
        self.stopButton = tk.Button(self.root, text = "Stop", command = self.stopTimer)
        self.stopButton.pack(side=BOTTOM, pady=15)

        #Countdown timer
        self.animeCountdownLabel = tk.Label(self.root,font=("Arial", 25), text = totalTime)
        self.animeCountdownLabel.place(relx=0.5,rely=0.5, anchor=CENTER)

        while (totalTime > 0):
            self.animeCountdownLabel['text'] = totalTime
            self.root.update()
            totalTime-=1
            time.sleep(1)
        self.animeCountdownLabel.destroy()
        self.watchingLabel.destroy()
        self.stopButton.destroy()
        self.completedAnimedoroScreen()

    #Implement Stop button during Timer
    def stopTimer(self):

        if (self.screen):
            self.animeCountdownLabel.destroy()
            self.watchingLabel.destroy()
            self.stopButton.destroy()
            self.animeTimer()
        else:
            self.studyCountdownLabel.destroy()
            self.stopButton.destroy()
            self.studyTimer()

    def completedAnimedoroScreen(self):
        self.completedAnimedoros += 1
       
        self.runsCompleted = tk.Label(self.root,font=("Arial", 13), text = 'You have completed ' + str(self.completedAnimedoros) + ' Animedoros')
        self.runsCompleted.place(relx=0.5,rely=0.4, anchor=CENTER)
       
        self.startOver = tk.Label(self.root,font=("Arial", 13), text = 'Would you like to do it again?')
        self.startOver.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.quitButton = tk.Button(self.root, text = "Quit", command = self.root.destroy)
        self.quitButton.pack(side=BOTTOM,pady=5)
        self.restartButton = tk.Button(self.root, text = "Restart", command = self.reset)
        self.restartButton.pack(side=BOTTOM,pady=5)
        
    def reset(self):
        self.runsCompleted.destroy()
        self.startOver.destroy()
        self.quitButton.destroy()
        self.restartButton.destroy()
        self.studyTimer()

        

            
            


app = App()
