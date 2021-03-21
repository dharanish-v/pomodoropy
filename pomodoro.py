from plyer import notification
import time
import os
import traceback


file_path = os.path.dirname(__file__)


total_time_active = 0
total_productive_time = 0
total_break_time = 0


def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1


print("\nHappy Productive Hours!\n")


print(r'{}'.format(file_path))
folder_path = file_path+"/pomodoro_logs"

if not os.path.exists(folder_path):
    print("dsflkjs", folder_path)
    os.makedirs(folder_path)
else:
    print("folder exists!")

log_file = open(file_path+"\pomodoro_logs\logs.txt",'wt')

long_break_time = 4

while True:

    print("Productive Time Starts!")
    notification.notify(app_name='Pomodoro',title='Pomodoro',message='Productive Time Starts!',ticker='pomodoro coming...!',toast=True)
    countdown(1500) #25 mins in seconds
    total_productive_time += 25

    if total_productive_time != 25 * long_break_time:
        print("Take A Small Break!")
        notification.notify(title='Pomodoro', message='Take A Small Break!')
        countdown(300) #5 mins in seconds
        total_break_time += 5
        total_time_active += 30
        long_break_time += 4
    else:
        print("Take A Long Break!")
        notification.notify(title='Pomodoro', message='Take A Small Break!')
        countdown(900) #5 mins in seconds
        total_break_time += 15
        total_time_active += 40


    log_file.write("========================================\n")
    log_file.write("total_break_time : " + str(total_break_time))
    log_file.write("\ntotal_time_active : " + str(total_time_active))
    log_file.write("\ntotal_productive_time : " + str(total_productive_time))
    log_file.write("\n========================================\n\n")
    