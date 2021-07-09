import tkinter as tk
from tkinter.constants import ANCHOR, BOTTOM, CENTER, DISABLED, LEFT, N, RIGHT, S, TOP

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('250x250')
        self.timerVar = tk.IntVar()
        self.radioVar = tk.StringVar()

        #created a label with an entry area for timer duration
        self.timerLabel = tk.Label(self.root, text = 'Timer Duration')
        self.timerLabel.pack(side=TOP)
        self.timerEntryArea = tk.Entry(self.root,textvariable = self.timerVar, width = 5)
        self.timerEntryArea.pack(side=TOP)

        #created submit button
        self.submitButton = tk.Button(self.root, text = 'Submit', command = self.submit)
        self.submitButton.pack(side=BOTTOM, pady=15)
        self.root.mainloop()

    def submit(self):
        print(self.timerVar.get())
        self.update()
    def update(self):
        self.root.geometry('250x125')
        self.timerLabel.pack_forget()
        self.submitButton.pack_forget()
        self.timerEntryArea.pack_forget()

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
