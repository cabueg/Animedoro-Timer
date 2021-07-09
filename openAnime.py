import webbrowser

def openWebsite():
    anime = input("What anime do you want to watch: ")
    animePlus = anime.replace(" ", "+")

    url = 'https://www.crunchyroll.com/search?from=&q=' + animePlus
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
