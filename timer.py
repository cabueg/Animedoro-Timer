import time 
import datetime as dt
import winsound
import openAnime
import websiteblocker
import alarm


timerDuration = int(input("How many minutes for timer?: ")) #user input for length of animedoro timer
breakDuration = int(input("How many minutes for break?: ")) #user input for length of animedoro break
t_now = dt.datetime.now()                                   #current time
t_pom = timerDuration*60                                    #Duration of animedoro in seconds
t_delta = dt.timedelta(0, t_pom)                            #Time delta in mins
t_fut = t_now + t_delta                                     #Future time, ending animedoro
delta_sec = breakDuration * 60                              #Break time, after animedoro
t_fin = t_now + dt.timedelta(0,t_pom + delta_sec)           #Time after animedoro, including break
breaks = 0                                                  #number of breaks
while True:
    if(t_now < t_fut):  #check if pomodoro is finished
        print("Pomodoro")
        websiteblocker.blockSites()
    elif (t_fut <= t_now <= t_fin):
        websiteblocker.unblockSites()
        print('break time')
        alarm.alarmLoop()
        breaks += 1
        openAnime.openWebsite()
        time.sleep(delta_sec)
        alarm.alarmLoop()
        ans = int(input("Would you like to start another one (0/1)?: "))
        
        if(ans == True):
            print("Alright! Good luck!")
            t_now = dt.datetime.now()
            t_fut = t_now + t_delta
            t_fin = t_now + dt.timedelta(0,t_pom + delta_sec)

        elif(ans == False):
            print("Congrats! You made it.")
            break

    print("sleeping")
    time.sleep(20)
    t_now = dt.datetime.now()

