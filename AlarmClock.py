import sched
import time
import winsound as ws

def set_alarm(alarm_time, wav_file , message):
    s = sched.scheduler(time.time, time.sleep) #passing time modules time and sleep functions to control scheduled events
    s.enterabs(alarm_time, 1, print, argument=(message,)) #scheduler's enterabs function used to schedule an event to execute an absolute time (first alarm time should be compatible with the return type of the time function)
    s.enterabs(alarm_time, 1, ws.PlaySound, argument=(wav_file, ws.SND_FILENAME)) # high priority event by setting the priority to one| play the specified wav file using win sound module play function
    print('Alarm set for', time.asctime(time.localtime(alarm_time))) # helper message 
    s.run()# run scheduled events
