import tkinter as tk
from tkinter.constants import ANCHOR, BOTTOM, CENTER, DISABLED, LEFT, N, RIGHT, S, TOP
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.studyTimer()
        self.root.mainloop()

    def studyCountdown(self):
        totalTime = tk.IntVar()
        totalTime = self.timerVar.get()

        #destroys all the labels and entries and replaces with counter
        self.root.geometry('250x250')
        self.timerLabel.pack_forget()
        self.submitButton.pack_forget()
        self.timerEntryArea.pack_forget()
        self.countdownLabel = tk.Label(self.root,font=("Arial", 25), text = totalTime)
        self.countdownLabel.place(relx=0.5,rely=0.5, anchor=CENTER)

        #countdown timer 
        while (totalTime > 0):
            self.countdownLabel['text'] = totalTime
            self.root.update()
            totalTime-=1
            time.sleep(1)
        self.countdownLabel.destroy()
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
        self.root.geometry('250x250')
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

        #Countdown timer
        self.countdownLabel = tk.Label(self.root,font=("Arial", 25), text = totalTime)
        self.countdownLabel.place(relx=0.5,rely=0.5, anchor=CENTER)

        while (totalTime > 0):
            self.countdownLabel['text'] = totalTime
            self.root.update()
            totalTime-=1
            time.sleep(1)
        self.countdownLabel.destroy()
        self.watchingLabel.destroy()
        self.studyTimer()

#Implement Stop button during Timer
    

app = App()


#create dio background for fun
'''
dioImage = PhotoImage(file = "dio.png")
backgroundDio = Canvas(root, width = 100, height = 100)
backgroundDio.pack(fill = BOTH, expand = True)
backgroundDio.create_image(250,250, image = dioImage)
'''
#create a radio buttons for what media to watch
'''
media =  ["Crunchyroll",
          "Netflix" ,
          "Disney+"]

for nameOfPlatform in media:
    tk.Radiobutton(root, text = nameOfPlatform, variable = radioVar, value = nameOfPlatform, padx = 20).pack()
'''
