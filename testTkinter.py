import tkinter as tk
from tkinter.constants import ANCHOR, BOTTOM, CENTER, DISABLED, LEFT, N, RIGHT, S, TOP

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('250x250')
        self.timerVar = tk.IntVar()
        self.radioVar = tk.StringVar()

        #created a label with an entry area for timer duration
        self.timerLabel = tk.Label(self.root, text = 'Timer Duration(Minutes)')
        self.timerLabel.pack(side=TOP)
        self.timerEntryArea = tk.Entry(self.root,textvariable = self.timerVar, width = 5)
        self.timerEntryArea.pack(side=TOP)

        #created submit button
        self.submitButton = tk.Button(self.root, text = 'Submit', command = self.countdown)
        self.submitButton.pack(side=BOTTOM, pady=15)
        self.root.mainloop()

    def countdown(self):
        totalTime = tk.StringVar()
        totalTime = self.timerVar.get()
        
        self.root.geometry('250x250')
        self.timerLabel.pack_forget()
        self.submitButton.pack_forget()
        self.timerEntryArea.pack_forget()
        self.countdownLabel = tk.Label(self.root,font=("Arial", 25), text = totalTime*60)
        self.countdownLabel.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.updateCountdownScreen(totalTime*60)
    def updateCountdownScreen(self, count):
        self.countdownLabel['text'] = count
        self.root.update()
        if (count > 0):
            self.root.after(1000, self.updateCountdownScreen, count-1)

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
