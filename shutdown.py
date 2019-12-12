#requirement pip3 install psutil

import psutil
import time
import os
 
x=0
while x == 0:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if percent < 50 and plugged==False:
        print("Under threshold, shuuting down")
        print(os.system("shutdown now"))
    if plugged==False: plugged="Not Plugged In"
    else: plugged="Plugged In"
    print(str(percent)+'% | '+plugged)
    time.sleep(30)
    
