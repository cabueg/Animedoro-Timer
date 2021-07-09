import msvcrt, winsound, time

def alarmLoop():
    while True: 
        winsound.Beep(400,700)
        if msvcrt.kbhit():
            break
        time.sleep(2)